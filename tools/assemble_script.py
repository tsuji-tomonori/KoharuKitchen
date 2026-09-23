#!/usr/bin/env python3
"""一度だけチャンクを統合し、以後は部ファイルを検証・索引化する。

初回: python tools/assemble_script.py --assemble --remove-chunks
校閲後: python tools/assemble_script.py --index
検証のみ: python tools/assemble_script.py --check
既存の部ファイルは上書きしない。外部ライブラリは不要。
"""

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EPISODE = re.compile(r"^## ([A-Z]+-\d{2}) / 通読順(\d{3}) / (.+)$", re.M)
HEADINGS = (
    "制作メモ（読者には表示しない）", "漫画本文（1ページ）",
    "次の話へのつなぎ（引き）", "この話で起きていたこと",
    "ソフトウェアエンジニアリングでは何と呼ぶか", "なぜ有効なのか",
    "どんな場合には使えないか", "SWEBOKではどこで扱われているか",
)
FIELDS = (
    "サブタイトル", "部・アーク", "形式", "時期・場所", "出演", "制作状態",
    "この話の1メッセージ", "主役が欲しいもの", "今回決まること",
    "伏線・関係変化", "引き継ぐ事実", "原案参照", "次話", "渡すもの",
    "画面への反映", "本編のみの次話",
)

# 時期／あらすじ／関係／次へ渡すもの。話ごとの原稿はこのコードに保持しない。
INTRO = [
    ("開始〜1か月", "十二時二十分、予約の一食を渡せなかった店で、遥は画面を閉じて仕事を見始める。", "坂本が遥へ椅子を出し、立花と森の視点も加わって、現場に教わる関係が始まる。", "観察記録、関係者一覧、未決の要求候補を予算の相談へ渡す。"),
    ("2か月目", "三千万円と開始から六か月目の二店舗試行を前に、自作・既製品・組合せの案を比べる。", "蓮が遥の競争相手となり、水野は曖昧な約束を条件へ変え、森と相原の仕事を計画に入れる。", "対象外と未確定事項を残した承認資料を、通知や受付の設計へ渡す。"),
    ("3か月目", "紙の受付と模擬注文で、同じ言葉に隠れていた違いを確かめる。藤堂の大きな案も見直す。", "遥と森は互いの見落としを認め、藤堂も人数と現場の条件に合わせて案を選び直す。", "状態・責務・権限・接点のモデル、不採用理由と未確認一覧を実装へ渡す。"),
    ("4か月目", "古い端末と小さな部品を確かめ、つないだ途端に止まる注文を、一件ずつ店まで通していく。", "遥と蓮は接点の修正を頼み合い、全員が一つの試験用番号を受け渡す仲間になる。", "一周した試験注文、コードと試験記録、未確認の赤札を公開前試験へ渡す。"),
    ("5か月目", "公開前に失敗を再現し、全部は試せない時間の中で、試す順と残す危険を選ぶ。", "森は赤札を仲間へ渡し、遥と蓮は失敗を隠さず、水野も未確認を一緒に伝える。", "確認済みの試行候補03、店舗別設定、証拠・残件・戻し方を二店舗へ運ぶ。"),
    ("6か月目", "青葉店と駅前店のベルが鳴る。注文の迷い、店の違い、通信の途切れを実際の利用から知る。", "立花と坂本が互いの条件を確かめ、相原と水野は店長も休める問い合わせ窓口を整える。", "試行結果と残件、各店の確認条件を、既存八店舗への展開へ渡す。"),
    ("7〜8か月目", "全店展開後の正午に電話が重なる。復旧と注文照合を進め、同じ障害の記録を調べ直す。", "水野が連絡を受け持ち、相原と店員たちが復旧・照合を分担する。", "復旧後の影響と構成の記録、原因候補、応急処置の残務を保守へ渡す。"),
    ("9〜10か月目", "積み重なった変更票と古いマクロを読み直し、直した箇所の外へも確認を広げる。", "藤堂は昔の判断の負担を開き、遥は責めるより改善を引き受け、店長の知識も記録に残す。", "変更票・影響図・回帰試験・保守計画と、営業で確かめた範囲を評価へ渡す。"),
    ("11〜12か月目", "増えた件数や美しいグラフを見直し、未使用の機能と残る待ちを確かめる。青いテープで再試合する。", "遥と蓮は利用結果まで競い、小野寺は不都合な数字も開き、森と遥は根拠のある喜びを分け合う。", "比較条件と実績、受取準備の負担を減らす問いを外部調査へ渡す。"),
    ("13〜14か月目", "展示・見学・試作・読書会で、製造連携や新技術の条件を調べる。採用を急がず問いを持ち帰る。", "遥は知らないことを尋ね、蓮とは違う案を残す。藤堂は現行業務の引き継ぎを遥に頼む。", "採否理由と未回答の問い、現行の手順・残件を引き継ぎ試行へ渡す。"),
    ("15〜16か月目", "藤堂が別案件で不在の午前、遥は手順と相原の力で相談を受ける。古い図と判断理由を皆で読み直す。", "遥が条件に合う案を提案し、藤堂は隣で教わる側になる。主担当と相談先を確かめる。", "現行構成、未解決事項、担当と判断理由を、案件を終える相談へ渡す。"),
    ("17〜18か月目", "愛着のある部品を手放す計画を選び、必要な記録を残して二重入力の台帳を閉じる。十二時二十分に袋を渡す。", "小野寺が終了を受け取り、水野と森が残件の受領を確認する。遥は次の担当へ判断を託す。", "本筋はENG-01で完結。別枠の待ちは担当と調査日を残し、付録へは任意の後日談を渡す。"),
    ("通読後の後日談／随時参照（本筋の十八か月を延長しない）", "新しい相談に備え、知識の地図、標準の目的と版、参考文献から必要な一つを探す。", "遥と蓮は違う案を持つ相棒のまま、白い一ページに問いを書き、先に現場を聞きに行く。", "APP-03で全458話を閉じる。次の話はない。"),
]

SYNOPSIS = """十二時二十分、青葉店で予約されていた最後の一食が、別の客に売られていた。
若手開発者の青井遥は画面を開くが、それだけでは佐伯真帆の昼食を用意できない。
坂本店長が代替の弁当を渡し、遥は空の袋を広げた手で、二枚の伝票を並べる。
店長が出してくれた椅子に座り、遥は電話、厨房、受取口の仕事を聞き始める。
二か月目、三千万円の枠と六か月目の二店舗試行に向け、作る範囲を相談する。
速い試作を持つ真柴蓮が現れ、森の赤ペンや相原の運用の問いが、遥の案を揺らす。
水野は曖昧な約束を紙へ開き、小野寺は作らないものと未確定の条件も引き受ける。
三か月目、紙の店で一食を動かすと、同じ言葉の裏に違う約束が見つかる。
藤堂も大きな構成案を脇へ置き、今の人数で扱える案と、退けた理由を残す。
四か月目、ばらばらに完成した部品は止まり、遥と蓮は互いの接点を直し始める。
一つの試験用注文番号が全員の画面を一周し、喜びの横に次の赤札が置かれる。
五か月目、森は試す順と担当を選び、遥たちは失敗と未確認を一緒に報告する。
六か月目、青葉店と駅前店でベルが鳴り、試験だけでは見えなかった迷いと店舗差に出会う。
七〜八か月目、八店舗の正午に障害が起き、水野の連絡と相原の復旧、店員の照合がつながる。
九〜十か月目、古い札と台帳の文字を読み直し、遥は藤堂が残した負担の改善も引き受ける。
十一〜十二か月目、使われない機能や条件の違う数字を認め、青いテープの前で効果を確かめ直す。
十三〜十四か月目、仲間は店の外へ調べに行き、採らない理由と専門家への問いを持ち帰る。
十五〜十六か月目、藤堂のいない席で遥が相談を受け、戻った藤堂は遥の提案を聞く側になる。
十七〜十八か月目、自作への愛着を認めながら置換を選び、控えを残して二重入力の台帳を閉じる。
同じ十二時二十分、佐伯は弁当入りの袋を普通に受け取る。残る仕事を次の担当へ託し、仲間は昼食を取る。"""


@dataclass
class Episode:
    id: str
    order: int
    title: str
    text: str
    source: Path

    def field(self, name):
        values = re.findall(r"^- " + re.escape(name) + r"：(.+)$", self.text, re.M)
        require(len(values) == 1, f"{self.id}: {name} は1件必要（{len(values)}件）")
        return values[0]

    @property
    def anchor(self):
        return "episode-" + self.id.lower()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^\s*<!--\s*chunk\b[^\n]*-->\s*$", "", text, flags=re.M)
    matches = list(EPISODE.finditer(text))
    require(bool(matches), f"話見出しがありません: {path}")
    require(len(re.findall(r"^## ", text, re.M)) == len(matches), f"不正な話見出し: {path}")
    return [Episode(m[1], int(m[2]), m[3],
                    text[m.start():matches[i + 1].start() if i + 1 < len(matches) else len(text)].strip(), path)
            for i, m in enumerate(matches)]


def catalog():
    manifest = json.loads((ROOT / "data/writing-manifest.json").read_text(encoding="utf-8"))
    with (ROOT / "data/episode-index.csv").open(encoding="utf-8-sig", newline="") as f:
        index = list(csv.DictReader(f))
    require(len(index) == 458, "索引は458話必要")
    require([p["部番号"] for p in manifest] == list(range(1, 14)), "部番号は1〜13が必要")
    return manifest, index


def validate(episodes, manifest, index, canonical=False):
    require(len(episodes) == 458, f"全458話必要（{len(episodes)}話）")
    require(len({e.id for e in episodes}) == 458, "話IDの重複")
    require([e.order for e in episodes] == list(range(1, 459)), "通読順は001〜458の連続順が必要")
    for i, (e, row) in enumerate(zip(episodes, index)):
        require((e.id, e.order, e.title) == (row["話ID"], int(row["通読順"]), row["ドラマタイトル"]), f"索引不一致: {e.id}")
        for field in FIELDS:
            e.field(field)
        require(e.field("形式") == row["形式"], f"形式不一致: {e.id}")
        require(e.field("サブタイトル") == row["サブタイトル"], f"サブタイトル不一致: {e.id}")
        headings = re.findall(r"^### (.+)$", e.text, re.M)
        for heading in HEADINGS:
            require(headings.count(heading) == 1, f"{e.id}: 必須見出し {heading}")
        positions = [e.text.index("### " + h) for h in HEADINGS]
        require(positions == sorted(positions), f"見出し順不一致: {e.id}")
        body = e.text[positions[1]:positions[2]]
        panels = re.findall(r"^#### コマ(\d+)\n(.*?)(?=^#### |\Z)", body, re.M | re.S)
        require(3 <= len(panels) <= 6, f"コマ数が範囲外: {e.id}")
        require([int(n) for n, _ in panels] == list(range(1, len(panels) + 1)), f"コマ順不一致: {e.id}")
        for n, panel in panels:
            for field in ("画面指示", "セリフ", "モノローグ", "効果音"):
                require(bool(re.search(r"^- " + field + "：.+$", panel, re.M)), f"{e.id} コマ{n}: {field} 欠落")
        next_all = episodes[i + 1] if i + 1 < len(episodes) else None
        expected = f"{next_all.id} / 通読順{next_all.order:03} / {next_all.title}" if next_all else "なし"
        require(e.field("次話") == expected, f"全話ルート不一致: {e.id}: {e.field('次話')}")
        next_main = next((x.id for x in episodes[i + 1:] if x.field("形式") == "本編"), "該当なし")
        require(e.field("本編のみの次話") == next_main, f"本編ルート不一致: {e.id}")
        require("<!-- chunk" not in e.text, f"チャンクコメント残存: {e.id}")
        if canonical:
            require(e.text.count(f'<a id="{e.anchor}"></a>') == 1, f"話リンクのアンカー不一致: {e.id}")
    for part in manifest:
        group = episodes[part["開始順"] - 1:part["終了順"]]
        require(len(group) == part["話数"], f"話数不一致: {part['file']}")
        require([e.id for e in group] == part["episode_ids"], f"話ID所属・順序不一致: {part['file']}")
        require((group[0].id, group[-1].id) == (part["先頭話ID"], part["末尾話ID"]), f"端点不一致: {part['file']}")
        require(Counter(e.field("形式") for e in group) == part["形式別"], f"形式別話数不一致: {part['file']}")
        if canonical:
            require(all(e.source == ROOT / part["file"] for e in group), f"ファイル所属不一致: {part['file']}")
            require((ROOT / part["file"]).read_text(encoding="utf-8").startswith(part_title(part) + "\n"), f"部見出し不一致: {part['file']}")
    main = [e for e in episodes if e.field("形式") == "本編"]
    require(len(main) == 276 and main[0].id == "REQ-01" and main[-1].id == "ENG-01", "本編ルートの件数・端点不一致")


def part_title(part):
    prefix = "付録" if part["部番号"] == 13 else f"第{part['部番号']}部"
    return f"# {prefix}：{part['アーク']}"


def render_part(part, episodes):
    period, synopsis, relation, handoff = INTRO[part["部番号"] - 1]
    intro = f"{part_title(part)}\n\n- 時期：{period}\n- あらすじ：{synopsis}\n- この部で変わる関係：{relation}\n- 次へ渡すもの：{handoff}\n\n"
    blocks = []
    for e in episodes[part["開始順"] - 1:part["終了順"]]:
        heading, rest = e.text.split("\n", 1)
        blocks.append(f'{heading}\n\n<a id="{e.anchor}"></a>\n{rest}')
    return intro + "\n\n".join(blocks) + "\n"


def render_readme(episodes, manifest):
    lines = ["# こはるキッチンの開発日誌：台本", "", "## 十八か月の物語", "",
             "  \n".join(SYNOPSIS.splitlines()), "", "## 読み方", "",
             "全458話ルートは、下の目次を通読順001〜458に読みます。本編276話、技術ノート140話、比較ノート39話、付録ガイド3話を含みます。",
             "本編276話ルートは、表の「形式」が本編の行だけを「本編順」1〜276で読みます。各話末の「本編のみの次話」も同じ順序です。ノート回の同欄は、その地点から次の本編へ戻る入口です。",
             "本筋は[ENG-01（通読455）](part-12.md#episode-eng-01)で完結します。[付録APP-01〜03](part-13.md#episode-app-01)は任意の後日談です。各話の補足は漫画本文の後に置き、制作メモと引きの欄は読者への表示対象に含めません。",
             "", "台本の正本は `part-01.md`〜`part-13.md` です。以後は部ファイルを直接修正し、`python tools/assemble_script.py --index` で検証と目次更新、`--check` で書込みなしの検証を行います（リポジトリのルートから実行）。",
             "校閲の範囲・変更履歴・残る課題は[通し校閲記録](../docs/continuity-review.md)にあります。", ""]
    main_order = {e.id: n for n, e in enumerate((e for e in episodes if e.field("形式") == "本編"), 1)}
    for part in manifest:
        name = Path(part["file"]).name
        lines += ["## " + part_title(part)[2:], "", f"{INTRO[part['部番号'] - 1][0]}。{part['話数']}話（本編{part['形式別'].get('本編', 0)}話）。", "",
                  "| 話ID | 通読順 | タイトル | 形式 | 本編順 |", "| --- | ---: | --- | --- | ---: |"]
        for e in episodes[part["開始順"] - 1:part["終了順"]]:
            title = e.title.replace("|", "\\|")
            lines.append(f"| [{e.id}]({name}#{e.anchor}) | {e.order:03} | {title} | {e.field('形式')} | {main_order.get(e.id, '—')} |")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--assemble", action="store_true", help="chunksから初回統合（既存の部ファイルがあれば拒否）")
    mode.add_argument("--index", action="store_true", help="部ファイルを検証しREADMEを更新")
    mode.add_argument("--check", action="store_true", help="部ファイルとREADMEを検証する（既定動作）")
    parser.add_argument("--remove-chunks", action="store_true", help="初回統合・再読込検証成功後に入力チャンクを削除")
    args = parser.parse_args()
    require(not args.remove_chunks or args.assemble, "--remove-chunks は --assemble と併用してください")
    manifest, index = catalog()
    chunks = []
    if args.assemble:
        require(not list((ROOT / "script").glob("part-*.md")), "正本の部ファイルが存在します。直接修正し --index または --check を使ってください")
        chunks = sorted((ROOT / "script/chunks").glob("*.md"))
        require(len(chunks) == 22, f"入力チャンクは22ファイル必要（{len(chunks)}件）")
        require(set((ROOT / "script/chunks").iterdir()) == set(chunks), "chunks内に台本以外のファイルがあります")
        require(all(not p.is_symlink() for p in chunks), "チャンクのシンボリックリンクは扱いません")
        episodes = [e for p in chunks for e in parse(p)]
        validate(episodes, manifest, index)
        # 全入力の検証を通してから書く。部分生成時も再実行で正本を上書きしない。
        for part in manifest:
            (ROOT / part["file"]).write_text(render_part(part, episodes), encoding="utf-8")
    paths = [ROOT / part["file"] for part in manifest]
    require(set((ROOT / "script").glob("part-*.md")) == set(paths), "部ファイルはmanifestの13件が必要")
    episodes = [e for p in paths for e in parse(p)]
    validate(episodes, manifest, index, canonical=True)
    readme = render_readme(episodes, manifest)
    target = ROOT / "script/README.md"
    if args.assemble or args.index:
        target.write_text(readme, encoding="utf-8")
    require(target.read_text(encoding="utf-8") == readme, "READMEが最新の台本と一致しません。--index で更新してください")
    if args.remove_chunks:
        # 書込み後の正本を全話読み直し検証した後に、確認済みの入力だけを削除。
        for path in chunks:
            path.unlink()
        (ROOT / "script/chunks").rmdir()
    for part in manifest:
        print(f"OK {part['file']}: {part['話数']}話 / {part['開始順']:03}〜{part['終了順']:03}")
    print("OK 全458話・本編276話／ID・通読順・形式・タイトル・必須見出し・コマ欄・全話/本編の次話・目次458リンク")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f"検証失敗: {exc}") from exc
