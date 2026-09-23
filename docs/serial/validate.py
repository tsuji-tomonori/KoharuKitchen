#!/usr/bin/env python3
"""連載設計と原作IDを照合する。書込みは --report 指定時の当ディレクトリ内のみ。"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def check():
    failures = []
    def require(ok, message):
        if not ok:
            failures.append(message)

    originals = {}
    for path in sorted((ROOT / 'script').glob('part-*.md')):
        for block in re.split(r'(?=^## [A-Z]+-\d+ /)', path.read_text(), flags=re.M)[1:]:
            m = re.match(r'## (\S+) / 通読順(\d+) / (.*)', block)
            require(m is not None, f'原作見出し不正: {path}')
            if not m:
                continue
            form = re.search(r'^- 形式：(.*)$', block, re.M)
            require(m[1] not in originals, f'原作ID重複: {m[1]}')
            originals[m[1]] = (int(m[2]), form[1])
    require(len(originals) == 458, '正本のID数が458ではない')
    require({v[0] for v in originals.values()} == set(range(1, 459)), '原作通読順の欠落')

    plan = json.loads((HERE / 'series-plan.json').read_text())
    require([c['n'] for c in plan] == list(range(1, 97)), '連載話番号が1〜96ではない')
    prior = [n for c in plan for n in c['source_serial_r0']]
    require(sorted(prior) == list(range(1, 109)), '旧108話の統合に欠落・重複がある')
    md = (HERE / 'series-structure.md').read_text()
    rows = []
    for line in md.splitlines():
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) == 7 and cells[0].isdigit():
            rows.append(cells)
    require(len(rows) == len(plan), 'Markdown全話表の行数が不一致')
    assigned = Counter()
    expected_csv = Counter()
    for c, cells in zip(plan, rows):
        n = c['n']
        require(c['pages'] == (46 if n == 1 else 25 if n == 2 else 19), f'{n}:ページ数')
        require(0 <= c['heat'] <= 10, f'{n}:熱量の範囲')
        require(all(c[k] for k in ['title', 'event', 'emotion', 'stakes', 'hook', 'joke']), f'{n}:必須の物語欄が空')
        require(cells[:6] == [str(n), c['title'], str(c['pages']), c['event'], str(c['heat']), c['emotion']], f'{n}:全話表とJSONの不一致')
        ids = c['main'] + c['bonus']
        require(len(ids) == len(set(ids)), f'{n}:同一回内のID重複')
        require(Counter(re.findall(r'\b[A-Z]+-\d+\b', cells[6])) == Counter(ids), f'{n}:表の原作ID不一致')
        assigned.update(ids)
        orders = []
        for source_id in ids:
            require(source_id in originals, f'{n}:未知ID {source_id}')
            if source_id not in originals:
                continue
            order, form = originals[source_id]
            orders.append(order)
            place = '本編素材' if source_id in c['main'] else 'おまけ'
            require(form != '本編' or place == '本編素材', f'{n}:原作本編が補足のみ {source_id}')
            expected_csv[(str(n), f'{order:03}', source_id, form, place)] += 1
        require(Counter(orders) == Counter(c['nums']), f'{n}:原作通読順とIDの不一致')
    missing = sorted(set(originals) - set(assigned))
    unknown = sorted(set(assigned) - set(originals))
    require(not missing, f'未割り当て: {missing}')
    require(not unknown, f'未知ID: {unknown}')
    with (HERE / 'source-map.csv').open(newline='') as f:
        csv_rows = list(csv.DictReader(f))
    actual_csv = Counter(tuple(r[k] for k in ['serial_chapter', 'source_order', 'source_id', 'source_form', 'placement']) for r in csv_rows)
    require(actual_csv == expected_csv, 'CSVとJSONの不一致')
    narrative_rows = []
    narrative_section = md.split('<!-- GENERATED FROM series-plan.json -->', 1)[-1].split('## 熱量の推移と自己点検')[0]
    for line in narrative_section.splitlines():
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) == 4 and cells[0].isdigit():
            narrative_rows.append(cells)
    require(narrative_rows == [[str(c['n']), c['stakes'], c['joke'], c['hook']] for c in plan],
            '賭け金・緩和・ヒキ表とJSONの不一致')

    low = run = max_low = 0
    flat_runs = []
    start = 0
    for i, c in enumerate(plan):
        low = low + 1 if c['heat'] <= 3 else 0
        max_low = max(max_low, low)
        if i and c['heat'] == plan[i-1]['heat']:
            run += 1
        else:
            if run >= 2:
                flat_runs.append((start + 1, i, plan[i-1]['heat']))
            start, run = i, 0
    if run >= 2:
        flat_runs.append((start + 1, len(plan), plan[-1]['heat']))
    require(max_low < 3, '熱量3以下が3話以上連続')
    graph = {int(n): (len(bars), int(value)) for n, bars, value in re.findall(r'^(\d{3}) (■+)\s+(\d+) ', md, re.M)}
    require(graph == {c['n']: (c['heat'], c['heat']) for c in plan}, '熱量グラフ不一致')
    require(sum(c['pages'] for c in plan) == 1857, '本文総ページ数不一致')

    # 巻ごとの到達と次の問いを、話数の所属・全巻の被覆まで確認する。
    volume_ranges = [(1, 9), (10, 18), (19, 27), (28, 36), (37, 45),
                     (46, 54), (55, 63), (64, 72), (73, 78), (79, 87), (88, 96)]
    # 巻表は4列なので、話別の4列表とは見出しの範囲で分ける。
    volume_section = md.split('| 巻 | 巻のクライマックス話 |', 1)[-1].split('## 割り当て・形式検証')[0]
    volume_rows = [[c.strip() for c in line.strip('|').split('|')]
                   for line in volume_section.splitlines() if re.match(r'^\| \d+ \|', line)]
    require([r[0] for r in volume_rows] == [str(n) for n in range(1, 12)], '巻の山場・ヒキが全11巻分ない')
    for row, (first, last) in zip(volume_rows, volume_ranges):
        require(len(row) == 4 and all(row), f'第{row[0]}巻:山場・ヒキ欄不足')
        if len(row) == 4:
            climax = re.match(r'第(\d+)話', row[1])
            ending = re.match(r'第(\d+)話', row[3])
            require(climax is not None and first <= int(climax[1]) <= last, f'第{row[0]}巻:山場の所属')
            require(ending is not None and int(ending[1]) == last, f'第{row[0]}巻:ヒキが巻末話でない')

    with (HERE / 'dialogue-counts.csv').open(newline='') as f:
        dialogue_rows = list(csv.DictReader(f))
    dialogue_counts = {(int(r['chapter']), int(r['page'])): (int(r['r1_chars']), int(r['r2_chars']), int(r['r3_chars']),
                                                         int(r['r4_chars']) if r['r4_chars'] != '' else None)
                       for r in dialogue_rows}
    historical_pages = {(n, p) for n, count in [(1, 48), (2, 25), (3, 19)] for p in range(1, count + 1)}
    require(len(dialogue_rows) == len(dialogue_counts) == 92 and set(dialogue_counts) == historical_pages,
            '旧稿を含む頁別台詞集計の件数・重複・頁番号')
    actual_dialogue = {}

    scenario_report = []
    for n, count in [(c['n'], c['pages']) for c in plan[:3]]:
        text = (HERE / f'ch{n:02}.md').read_text()
        body = text.split('## おまけページ')[0]
        headers = list(re.finditer(r'^## P(\d+)｜(.+?)｜(右|左)｜(\d+)コマ$', body, re.M))
        require([int(m[1]) for m in headers] == list(range(1, count+1)), f'ch{n}:ページ連番')
        require(f'第{n}話「{plan[n-1]["title"]}」' in text, f'ch{n}:タイトル不一致')
        require(f'本文{count}ページ' in text, f'ch{n}:冒頭の頁数不一致')
        if n == 1:
            layout_rows = re.findall(r'^\| P(\d+)（(右|左)） \| (\d+) \| ([^|]+) \| ([^|]+) \|$', body, re.M)
            require([(int(p), side, int(panels)) for p, side, panels, _, _ in layout_rows]
                    == [(int(h[1]), h[3], int(h[4])) for h in headers], 'ch1:冒頭構成表の頁・左右・コマ数')
            for p, _, _, spread, style in layout_rows:
                page = int(p)
                first = page if page % 2 else page - 1
                require(spread.startswith(f'P{first:02}〜{first+1:02}：'), f'ch1 P{page}:構成表の対向頁')
                require(('一枚絵' in spread) == (page in [23, 24, 35, 36]), f'ch1 P{page}:構成表の見開き')
                require(style.startswith(('E標準', 'F強調')), f'ch1 P{page}:E・F案なし')
                if style.startswith('F強調'):
                    require('対象：' in style and '理由：' in style, f'ch1 P{page}:F案の対象・理由なし')
        panel_count = 0
        max_bubble = 0
        page_chars = []
        spreads = []
        panel_sizes = Counter()
        for i, h in enumerate(headers):
            p = int(h[1]); panels = int(h[4])
            block = body[h.end():headers[i+1].start() if i+1 < len(headers) else len(body)]
            nums = [int(v) for v in re.findall(r'^(\d+)\. ', block, re.M)]
            require(nums == list(range(1, panels+1)), f'ch{n} P{p}:コマ数・連番')
            require(h[3] == ('右' if p % 2 else '左'), f'ch{n} P{p}:左右')
            require('目的（感情）：' in block and '同時に見えるページ：' in block, f'ch{n} P{p}:目的・見開き相手がない')
            partner = re.search(r'同時に見えるページ：P(\d+)', block)
            require(partner is not None and int(partner[1]) == (p + 1 if p % 2 else p - 1),
                    f'ch{n} P{p}:対向頁の番号不一致')
            require(('めくりのヒキ：' if p % 2 == 0 else 'ページ末の誘導') in block, f'ch{n} P{p}:めくり記載なし')
            # 制作注記・補足を除くコマ記載内の台詞・内語。句読点も1字。
            panel_lines = '\n'.join(re.findall(r'^\d+\. .*$', block, re.M))
            chars = sum(len(q) for q in re.findall(r'「([^」]*)」', panel_lines))
            actual_dialogue[(n, p)] = chars
            page_chars.append(chars)
            for panel in re.split(r'^\d+\. ', block, flags=re.M)[1:]:
                require('擬音：' in panel and '台詞' in panel, f'ch{n} P{p}:台詞・擬音欄なし')
                for q in re.findall(r'「([^」]+)」', panel):
                    max_bubble = max(max_bubble, len(q))
                    require(len(q) <= 20, f'ch{n} P{p}:20字超 {q}')
            panel_count += panels
            panel_sizes[panels] += 1
            if '見開き（' in h[2]:
                spreads.append(p)
        require(spreads == ([23, 24, 35, 36] if n == 1 else []), f'ch{n}:見開き指定不一致')
        require(any(k <= 2 for k in panel_sizes) and any(5 <= k <= 7 for k in panel_sizes),
                f'ch{n}:大ゴマと小ゴマの緩急がない')
        require('話末のヒキ：' in body and 'おまけページ' in text, f'ch{n}:話末ヒキ・補足なし')
        # 同じ見開き一コマを左右で記載しているため、見開き組数を引く。
        distinct = panel_count - len(spreads) // 2
        before = sum(v[0] for k, v in dialogue_counts.items() if k[0] == n)
        previous = sum(v[1] for k, v in dialogue_counts.items() if k[0] == n)
        third = sum(v[2] for k, v in dialogue_counts.items() if k[0] == n)
        # 各回はその稿の頁位置で集計。総量の一律削減を合格条件にはしない。
        scenario_report.append(f'ch{n:02}: {count}頁、ページ別コマ記載{panel_count}（実コマ{distinct}）、引用符内最大{max_bubble}字、コマ数別頁数{dict(sorted(panel_sizes.items()))}')
        scenario_report.append(f'  台詞・内語: 第1回{before}→第2回{previous}→第3回{third}→第4回{sum(page_chars)}字、頁平均{sum(page_chars)/count:.1f}字、頁最大{max(page_chars)}字')
    require(actual_dialogue == {k: v[3] for k, v in dialogue_counts.items() if v[3] is not None}, '頁別台詞集計と本文の不一致')
    report = [
        '週刊連載版 設計検証',
        f'原作正本ID: {len(originals)} / 458',
        f'割り当て済みユニークID: {len(set(assigned) & set(originals))} / 458',
        f'未割り当て: {missing}', f'未知ID: {unknown}',
        f'割り当て総数（再利用込み）: {sum(assigned.values())}',
        f'複数回使用したID: {sum(v > 1 for v in assigned.values())}',
        f'連載: {len(plan)}話 / 11巻（旧108話の統合対応を照合）',
        f'本文: {sum(c["pages"] for c in plan)}頁 / おまけ{len(plan)*2}頁 / 合計{sum(c["pages"] for c in plan)+len(plan)*2}頁',
        f'原作形式: {dict(Counter(v[1] for v in originals.values()))}',
        f'熱量3以下の最長連続: {max_low}話（3話未満）',
        f'同じ熱量が3話以上連続: {flat_runs}',
        f'全話の賭け金・緩和・話末ヒキ: {len(plan)} / {len(plan)}',
        'JSON・CSV・全話表・熱量グラフ: 照合済み',
        f'巻のクライマックス話・巻末ヒキ: {len(volume_rows)} / 11（所属話・巻末話を照合）',
        f'頁別台詞・内語集計: {len(actual_dialogue)} / {sum(c["pages"] for c in plan[:3])}（第4回列を照合、旧3回は92頁分を保存。紙・画面上の文字は対象外）',
        '第1話の冒頭ページ構成表: 46頁のコマ数・左右・対向頁・二見開き・E/F案を照合',
        *scenario_report,
        '注意: 文字による設計検証。絵の可読性、試読反応、素材の描き切りは機械検証の対象外。',
        *[f'FAIL: {e}' for e in failures],
        'RESULT: FAIL' if failures else 'RESULT: PASS',
    ]
    return '\n'.join(report) + '\n', bool(failures)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', action='store_true', help='検証結果をdocs/serial/validation-report.txtへ保存')
    args = parser.parse_args()
    report, failed = check()
    if args.report:
        (HERE / 'validation-report.txt').write_text(report)
    print(report, end='')
    raise SystemExit(1 if failed else 0)
