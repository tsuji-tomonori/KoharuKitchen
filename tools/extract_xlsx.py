#!/usr/bin/env python3
"""全シートを保存し、話IDで統合する。実行: uv run --with openpyxl python tools/extract_xlsx.py

data_only のキャッシュを優先する。欠落時は、このブックで使う数式を元セルから
評価する。未対応の式は黙って欠落させず失敗する。--recalculate で全式を再評価できる。
原文・訳を含む sheets/ と episodes.json はローカル用（.gitignore 対象）。
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import operator
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.formula import Tokenizer
from openpyxl.utils.cell import range_boundaries

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / '.workspace/こはるキッチンの開発日誌｜SWEBOK 全458話・構成案.xlsx'


def normalize(value):
    if isinstance(value, str):
        return value.replace('⏎', '\n')
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def as_text(value):
    if value is None:
        return ''
    if isinstance(value, bool):
        return str(value).upper()
    return str(normalize(value))


def flatten(value):
    if isinstance(value, list):
        return [x for row in value for x in flatten(row)]
    return [value]


class FormulaError(ValueError):
    """Excel の参照不成立など、IFERROR の対象になるエラー。"""


class FormulaReader:
    """この入力で必要な演算子・17関数だけを扱う。Python eval は使用しない。"""
    PRECEDENCE = {'=': 1, '<>': 1, '<': 1, '>': 1, '<=': 1, '>=': 1,
                  '&': 2, '+': 3, '-': 3, '*': 4, '/': 4}

    def __init__(self, source, cached, recalculate=False):
        self.source, self.cached = source, cached
        self.recalculate = recalculate
        self.recomputed = []
        self.active = set()

    @staticmethod
    def formula(cell):
        return cell.value if isinstance(cell.value, str) else cell.value.text

    @lru_cache(maxsize=None)
    def cell(self, sheet, coordinate):
        c = self.source[sheet][coordinate]
        if c.data_type != 'f':
            return c.value
        cached = self.cached[sheet][coordinate]
        if cached.value is not None and not self.recalculate:
            if cached.data_type == 'e':
                raise FormulaError(f'{sheet}!{coordinate}: {cached.value}')
            return cached.value
        key = sheet, coordinate
        if key in self.active:
            raise RuntimeError(f'循環参照: {key}')
        self.active.add(key)
        try:
            result = self.evaluate(self.parse(self.formula(c)), sheet)
        finally:
            self.active.remove(key)
        self.recomputed.append({'sheet': sheet, 'cell': coordinate,
                                'reason': 'forced' if self.recalculate else 'missing_cache'})
        return result

    @staticmethod
    @lru_cache(maxsize=None)
    def parse(formula):
        tokens = [t for t in Tokenizer(formula).items if t.type != 'WHITE-SPACE']
        pos = 0

        def expression(minimum=0):
            nonlocal pos
            token = tokens[pos]
            pos += 1
            if token.type == 'FUNC' and token.subtype == 'OPEN':
                args = []
                while tokens[pos].subtype != 'CLOSE':
                    args.append(expression())
                    if tokens[pos].type == 'SEP':
                        pos += 1
                    else:
                        break
                if tokens[pos].subtype != 'CLOSE':
                    raise ValueError(f'関数終端がありません: {formula}')
                pos += 1
                left = ('call', token.value[:-1].upper(), args)
            elif token.type == 'PAREN' and token.subtype == 'OPEN':
                left = expression()
                if tokens[pos].subtype != 'CLOSE':
                    raise ValueError(formula)
                pos += 1
            elif token.type == 'OPERATOR-PREFIX':
                left = ('prefix', token.value, expression(5))
            elif token.type == 'OPERAND':
                left = ('operand', token.subtype, token.value)
            else:
                raise NotImplementedError(f'未対応トークン: {token} in {formula}')
            while pos < len(tokens) and tokens[pos].type == 'OPERATOR-INFIX':
                op = tokens[pos].value
                priority = FormulaReader.PRECEDENCE[op]
                if priority < minimum:
                    break
                pos += 1
                left = ('binary', op, left, expression(priority + 1))
            return left

        result = expression()
        if pos != len(tokens):
            raise NotImplementedError(f'未消費トークン: {formula}')
        return result

    @lru_cache(maxsize=None)
    def reference(self, sheet, ref):
        if '!' in ref:
            sheet, ref = ref.rsplit('!', 1)
            sheet = sheet.strip("'").replace("''", "'")
        ref = ref.replace('$', '')
        if ':' not in ref:
            return self.cell(sheet, ref)
        c1, r1, c2, r2 = range_boundaries(ref)
        return [[self.cell(sheet, c.coordinate) for c in row]
                for row in self.source[sheet].iter_rows(min_row=r1, max_row=r2,
                                                       min_col=c1, max_col=c2)]

    def evaluate(self, node, sheet):
        kind, value, *args = node
        ev = lambda n: self.evaluate(n, sheet)
        if kind == 'operand':
            raw = args[0]
            if value == 'TEXT':
                return raw[1:-1].replace('""', '"')
            if value == 'NUMBER':
                return normalize(float(raw))
            if value == 'LOGICAL':
                return raw == 'TRUE'
            if value == 'RANGE':
                return self.reference(sheet, raw)
            raise NotImplementedError(f'未対応オペランド: {node}')
        if kind == 'prefix':
            return ev(args[0]) * (-1 if value == '-' else 1)
        if kind == 'binary':
            a, b = map(ev, args)
            if value == '&':
                return as_text(a) + as_text(b)
            functions = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                         '/': operator.truediv, '=': operator.eq, '<>': operator.ne,
                         '<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge}
            return functions[value](a, b)
        nodes = args[0]
        if value == 'IF':
            return ev(nodes[1] if ev(nodes[0]) else nodes[2])
        if value == 'IFERROR':
            try:
                return ev(nodes[0])
            except (FormulaError, ZeroDivisionError):
                return ev(nodes[1])
        if value == 'VLOOKUP':
            # 表全体の評価は不要な列の逆参照まで辿るため、検索列と返却セルだけを読む。
            if len(nodes) != 4 or ev(nodes[3]) is not False:
                raise NotImplementedError('VLOOKUP は完全一致のみ対応')
            key, column = ev(nodes[0]), int(ev(nodes[2]))
            ref = nodes[1][2]
            target, address = ref.rsplit('!', 1) if '!' in ref else (sheet, ref)
            target = target.strip("'").replace("''", "'")
            c1, r1, c2, r2 = range_boundaries(address.replace('$', ''))
            if not 1 <= column <= c2 - c1 + 1:
                raise FormulaError('VLOOKUP: 範囲外')
            for row in range(r1, r2 + 1):
                if self.cell(target, self.source[target].cell(row, c1).coordinate) == key:
                    return self.cell(target, self.source[target].cell(row, c1 + column - 1).coordinate)
            raise FormulaError(f'VLOOKUP: {key} がありません')
        a = list(map(ev, nodes))
        if value == 'COUNTA':
            return sum(x is not None for x in flatten(a))
        if value in ('COUNTIF', 'COUNTIFS'):
            columns = [flatten(a[i]) for i in range(0, len(a), 2)]
            criteria = a[1::2]
            return sum(all(self.matches(x, c) for x, c in zip(row, criteria))
                       for row in zip(*columns))
        if value == 'SUM':
            return sum(x for x in flatten(a) if isinstance(x, (int, float)))
        if value == 'INDEX':
            row = int(a[1]) - 1
            col = int(a[2]) - 1 if len(a) > 2 else 0
            if row < 0 or row >= len(a[0]):
                raise FormulaError('INDEX: 範囲外')
            return a[0][row][col]
        if value == 'MATCH':
            choices = flatten(a[1])
            if len(a) > 2 and a[2] == 0:
                for i, x in enumerate(choices, 1):
                    if x == a[0]:
                        return i
            else:
                found = [i for i, x in enumerate(choices, 1) if x <= a[0]]
                if found:
                    return found[-1]
            raise FormulaError(f'MATCH: {a[0]} がありません')
        if value == 'TEXT':
            return f'{int(a[0]):0{len(a[1])}d}'
        if value == 'CHAR':
            return chr(int(a[0]))
        if value == 'LEN':
            return len(as_text(a[0]))
        if value == 'ISNUMBER':
            return isinstance(a[0], (int, float)) and not isinstance(a[0], bool)
        if value == 'TEXTJOIN':
            return a[0].join(as_text(x) for x in flatten(a[2:])
                             if not a[1] or x not in (None, ''))
        if value == 'SUBSTITUTE':
            return as_text(a[0]).replace(a[1], a[2])
        raise NotImplementedError(f'未対応関数: {value}')

    @staticmethod
    def matches(value, criterion):
        if not isinstance(criterion, str):
            return value == criterion
        match = re.match(r'^(<>|>=|<=|>|<|=)(.*)$', criterion)
        if match:
            op, other = match.groups()
            if op == '<>':
                return as_text(value) != other
            if op == '=':
                return as_text(value) == other
            return {'>': operator.gt, '<': operator.lt, '>=': operator.ge,
                    '<=': operator.le}[op](float(value or 0), float(other))
        pattern = re.escape(criterion).replace(r'\*', '.*').replace(r'\?', '.')
        return re.fullmatch(pattern, as_text(value), re.IGNORECASE) is not None


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def extract(input_path, output_dir, recalculate=False):
    source = load_workbook(input_path, data_only=False)
    cached = load_workbook(input_path, data_only=True)
    reader = FormulaReader(source, cached, recalculate)
    sheets, tables = {}, {}
    for s in source:
        cells = {}
        for row in s:
            for c in row:
                if c.value is None:
                    continue
                item = {'value': normalize(reader.cell(s.title, c.coordinate))}
                if c.data_type == 'f':
                    item['formula'] = reader.formula(c)
                if c.hyperlink:
                    item['hyperlink'] = c.hyperlink.target or c.hyperlink.location
                cells[c.coordinate] = item
        headers = [normalize(reader.cell(s.title, c.coordinate)) for c in s[5]]
        # 非表形式のダッシュボード／一話リーダーも cells に位置付きで全て保存。
        records = []
        if s.title not in ('00_全体設計', '14_一話リーダー'):
            for row in s.iter_rows(min_row=6):
                if not any(c.value is not None for c in row):
                    continue
                records.append({'_row': row[0].row, **{
                    header or f'列{c.column_letter}': normalize(reader.cell(s.title, c.coordinate))
                    for header, c in zip(headers, row)}})
        tables[s.title] = records
        sheets[s.title] = {'sheet': s.title, 'state': s.sheet_state,
                           'max_row': s.max_row, 'max_column': s.max_column,
                           'merged_ranges': [str(r) for r in s.merged_cells.ranges],
                           'headers': headers, 'records': records, 'cells': cells}

    per_episode = ['01_全話一覧', '02_単話と通読設計', '11_読書ルート', '12_原文対照',
                   '13_会話劇台本', '17_少年漫画版台本', '20_会話を読む']
    indices = {}
    for name in per_episode:
        records = tables[name]
        index = {r['話ID']: r for r in records}
        if len(index) != len(records):
            raise ValueError(f'話ID重複: {name}')
        indices[name] = index
    ids = set(indices['01_全話一覧'])
    if len(ids) != 458:
        raise ValueError(f'全話数が458ではありません: {len(ids)}')
    for name, index in indices.items():
        if set(index) != ids:
            raise ValueError(f'話ID集合が一致しません: {name}')
    arcs = tables['18_連載アーク']
    timeline = {r['部']: r for r in tables['05_物語の時系列']}
    kas = {r['原書章']: r['知識領域'] for r in tables['04_章別集計']}
    topic_index = {r['照合キー']: r for r in tables['03_原書トピック']}
    episodes = []
    for record in tables['01_全話一覧']:
        eid, order = record['話ID'], record['通読順']
        draft = indices['17_少年漫画版台本'][eid]
        old = indices['13_会話劇台本'][eid]
        quote = indices['12_原文対照'][eid]
        arc = next(a for a in arcs if a['開始順'] <= order <= a['終了順'])
        part = arc['部']
        if timeline[part]['見出し'] != record['物語の部'] or draft['通読順'] != order:
            raise ValueError(f'部・通読順が不一致: {eid}')
        mappings = [r for r in tables['10_話と項目の対応'] if r['話ID'] == eid]
        motifs = [r for r in tables['19_キャラと伏線']
                  if eid in re.findall(r'[A-Z]+-\d+', (r['仕込み回'] or '') + '/' + (r['回収・再登場回'] or ''))]
        episodes.append({
            '話ID': eid, '通読順': order, '部番号': part, '部': record['物語の部'],
            '連載アーク': arc['アーク名'], '時期': record['物語上の時期'],
            'ドラマタイトル': draft['採用タイトル'], 'サブタイトル': record['サブタイトル（旧タイトル）'],
            '形式': record['形式'], '出演': draft['登場人物（台本）'],
            'シチュエーション': draft['場所・状況／幕開け'],
            '台本': {k: draft[k] for k in ('場所・状況／幕開け', '前半｜欲しいもの・衝突',
                       '中盤｜試行・発見・切り返し', '結末｜行動・決着・余韻', '通し台本')},
            '1メッセージ': record['1ページのメッセージ'],
            '伏線・関係変化': {'最新設計の該当行': motifs, '旧稿の人物・関係に残る変化': old['人物・関係に残る変化']},
            'SWEBOK': {'KA番号': record['原書章（番号／付録）'], 'KA': kas[record['原書章（番号／付録）']],
                       'トピック': record['扱うトピック'], '原書の節': record['原書の節'],
                       '節開始頁': record['原書開始頁'], '引用位置': draft['引用位置'],
                       '原書引用頁': quote['原書引用頁'], 'PDF引用頁（1始まり）': quote['PDF引用頁（1始まり）'],
                       '原文対応の確認': draft['原文対応の確認'], '項目対応': mappings,
                       '原書トピック行': [topic_index[m['照合キー']] for m in mappings]},
            '時系列設計': timeline[part], 'アーク設計': arc,
            '元シート列': {name: indices[name][eid] for name in per_episode},
        })
    episodes.sort(key=lambda e: e['通読順'])
    if [e['通読順'] for e in episodes] != list(range(1, 459)):
        raise ValueError('通読順が1〜458の連番ではありません')
    for i, ep in enumerate(episodes):
        for key, expected in [('直前話ID', episodes[i-1]['話ID'] if i else ''),
                              ('次話ID', episodes[i+1]['話ID'] if i < 457 else '')]:
            if (ep['元シート列']['17_少年漫画版台本'][key] or '') != expected:
                raise ValueError(f'前後リンク不整合: {ep["話ID"]} {key}')
        if not all(ep['台本'].values()):
            raise ValueError(f'台本欠落: {ep["話ID"]}')
    if any(r['話ID'] not in ids for r in tables['10_話と項目の対応']):
        raise ValueError('原書対応に未知の話IDがあります')

    parts = []
    for arc in arcs:
        es = [e for e in episodes if e['部番号'] == arc['部']]
        if len(es) != arc['終了順'] - arc['開始順'] + 1:
            raise ValueError(f'アーク話数不整合: {arc["部"]}')
        parts.append({'部番号': arc['部'], '部': es[0]['部'], 'アーク': arc['アーク名'],
                      '開始順': es[0]['通読順'], '終了順': es[-1]['通読順'],
                      '先頭話ID': es[0]['話ID'], '末尾話ID': es[-1]['話ID'],
                      '話数': len(es), '形式別': dict(Counter(e['形式'] for e in es))})
    summary = {'schema_version': 1, 'input_name': input_path.name,
               'input_sha256': hashlib.sha256(input_path.read_bytes()).hexdigest(),
               'sheet_count': len(sheets),
               'sheets': [{'name': n, 'state': s['state'], 'record_count': len(s['records']),
                           'populated_cells': len(s['cells'])} for n, s in sheets.items()],
               'episode_count': len(episodes), 'format_counts': dict(Counter(e['形式'] for e in episodes)),
               'parts': parts, 'formula_count': sum(c.data_type == 'f' for s in source for row in s for c in row),
               'recomputed_cells': reader.recomputed,
               'topic_count': len(topic_index), 'leaf_topic_count': sum(r['集計区分'] == '最下位' for r in topic_index.values()),
               'mapping_count': len(tables['10_話と項目の対応']),
               'reader_selection': normalize(reader.cell('14_一話リーダー', 'D4')),
               'needs_additional_source': [e['話ID'] for e in episodes if '補足出典要' in e['SWEBOK']['原文対応の確認']]}
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / 'sheets').mkdir(exist_ok=True)
    for name, sheet in sheets.items():
        write_json(output_dir / 'sheets' / f'{name}.json', sheet)
    write_json(output_dir / 'episodes.json', episodes)
    write_json(output_dir / 'extraction-report.json', summary)
    write_json(output_dir / 'writing-manifest.json', [
        {**part, 'file': f'script/part-{part["部番号"]:02d}.md',
         'episode_ids': [e['話ID'] for e in episodes if e['部番号'] == part['部番号']]}
        for part in parts])
    columns = ['話ID', '通読順', '部番号', '部', '連載アーク', '時期', 'ドラマタイトル', 'サブタイトル', '形式', '出演']
    with (output_dir / 'episode-index.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows({k: e[k] for k in columns} for e in episodes)
    print(f'{len(sheets)}シート / {len(episodes)}話 / ' + '・'.join(f'{p["部番号"]}部:{p["話数"]}' for p in parts))
    print(f'数式再計算: {len(reader.recomputed)}セル。出力: {output_dir}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--output', type=Path, default=ROOT / 'data')
    parser.add_argument('--recalculate', action='store_true', help='キャッシュを使わず全数式を元セルから評価')
    options = parser.parse_args()
    extract(options.input, options.output, options.recalculate)
