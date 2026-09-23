# 台本の統合と通し校閲（フェーズ2b）

確認日：2026-09-23。対象：並行執筆された22チャンク、全458話。正本は `script/part-01.md`〜`script/part-13.md`。Gitコミットは行っていない。

## 確認方法と範囲

基準は README、script-format、story-bible、writing-plan、writing-manifest と episode-index。全話の「今回決まること」「引き継ぐ事実」、時期・出演・形式・導線を通読順で確認し、チャンク境界21か所の冒頭・最終コマ・引きを対照した。同じ最終チャンク内の部境界449→450、455→456も別途確認した。
主要伏線は初出・変化・回収の該当コマと全編の登場箇所を照合した。本編は全275接続の次話IDを検証し、ノート回が挟まる58区間について、前の本編の最終コマと次の本編のコマ1を対照した。人物名・役割、時期、用語の定義導入、英語の長い文章は本文を抽出して検索し、候補の文脈を確認した。
これは物語の接続校閲であり、補足458話の技術的主張を全件再監修する作業ではない。既稿の原典照合記録を維持し、今回の修正では新しい技術的主張・出典を追加していない。修正は場面表示、小道具、参照、引き、制作メモの補強に限定した。

## 境界の確認

| 通読順 | 接続 | 確認した物・時期・関係・残務／対処 |
| --- | --- | --- |
| 008→009 | [ENG-08](../script/part-01.md#episode-eng-08) → [REQ-05](../script/part-02.md#episode-req-05) | 観察記録・関係者一覧・要求候補を同じクリップで予算会議へ。1→2か月目。修正不要。 |
| 029→030 | [ECO-08](../script/part-02.md#episode-eco-08) → [ECO-09](../script/part-02.md#episode-eco-09) | 第三案の列、置いた判、調査中の条件を保持。ECO-09の場所を前話と同じ灯台ソフトへ修正。 |
| 049→050 | [PRC-01](../script/part-02.md#episode-prc-01) → [PRC-02](../script/part-02.md#episode-prc-02) | 十五時の共同確認から翌日の昼休み前へ。「設計完了」は一昨日の試作方針とし、次の本編PRC-03にも日付を補った。 |
| 069→070 | [ECO-29](../script/part-02.md#episode-eco-29) → [REQ-10](../script/part-03.md#episode-req-10) | 二店舗試行の承認紙から外部通知の条件書へ。2→3か月目。予算・未確定事項を保持。修正不要。 |
| 093→094 | [MOD-03](../script/part-03.md#episode-mod-03) → [DES-05](../script/part-03.md#episode-des-05) | 取消で戻した一枠を二端末の同時確保試験へ。森の赤ペン、三人の役割を継続。修正不要。 |
| 116→117 | [QUA-03](../script/part-03.md#episode-qua-03) → [SEC-07](../script/part-03.md#episode-sec-07) | 品質表の「誰の店の注文を見られるか」の未確認札を受領。「安全性の確認欄」を前話と同じ権限の欄へ修正。 |
| 139→140 | [ENG-14](../script/part-03.md#episode-eng-14) → [CMP-02](../script/part-04.md#episode-cmp-02) | モデル・不採用理由・未確認一覧の資料袋と青葉店端末借用票を4か月目へ。番号の先行登場は注文札に直した。 |
| 165→166 | [MTH-14](../script/part-04.md#episode-mth-14) → [DES-23](../script/part-04.md#episode-des-23) | 十三個目の別箱と梱包相談記録から、注文・取消・変更の三操作の記録へ。箱は167の再試行にも残る。修正不要。 |
| 191→192 | [CON-21](../script/part-04.md#episode-con-21) → [CON-22](../script/part-04.md#episode-con-22) | 正しく読めた商品名と二入力を共有処理の試験へ。取消の業務確認は別の保留票として残る。修正不要。 |
| 217→218 | [PRO-24](../script/part-04.md#episode-pro-24) → [REQ-26](../script/part-05.md#episode-req-26) | 試験用101の一周記録、未確認の返金条件、赤札を5か月目へ。同じ番号の参照を明記。本編220にも試験の状況を補った。 |
| 241→242 | [OPS-07](../script/part-05.md#episode-ops-07) → [TST-05](../script/part-05.md#episode-tst-05) | 連絡票・模擬連絡の受領記録・未実施札を残り一時間の試験机へ。蓮は水野が調整した支援枠。修正不要。 |
| 265→266 | [TST-26](../script/part-05.md#episode-tst-26) → [TST-27](../script/part-05.md#episode-tst-27) | 状態別取消の確認から代理受取の一日へ。佐伯は営業時間外の模擬協力、袋には紙札。公開判断は未了。修正不要。 |
| 288→289 | [CFG-15](../script/part-05.md#episode-cfg-15) → [OPS-15](../script/part-06.md#episode-ops-15) | 候補03と二店別設定、証拠、戻し方を前日夕方から試行初日の朝へ。相原は青葉、水野は駅前。番号は別件の「青葉・実001」。物語の修正不要。 |
| 303→304 | [CMP-35](../script/part-06.md#episode-cmp-35) → [OPS-17](../script/part-07.md#episode-ops-17) | 他店の利用場所確認を経た7か月目へ。8店分の印を冒頭に表示。正午の障害をここで初めて起こす。修正不要。 |
| 323→324 | [ENG-24](../script/part-07.md#episode-eng-24) → [REQ-19](../script/part-08.md#episode-req-19) | 復旧後の図・変更票を9か月目の現行仕様確認へ。応急処置や原因候補は未解決のまま保持。修正不要。 |
| 341→342 | [TST-42](../script/part-08.md#episode-tst-42) → [MNT-07](../script/part-08.md#episode-mnt-07) | TST-42の新旧試験記録と未確定の終了札を、そのまま影響範囲の確認へ。342〜357の「9〜10か月目」を10か月目に限定。 |
| 358→359 | [ENG-25](../script/part-08.md#episode-eng-25) → [REQ-24](../script/part-09.md#episode-req-24) | 限定した営業確認と他店・別枠の残務を11か月目の評価へ。REQ-24の引きを「既存の改善対象」に直し、追加要求がないという台詞と合わせた。 |
| 379→380 | [PRC-13](../script/part-09.md#episode-prc-13) → [QUA-06](../script/part-09.md#episode-qua-06) | 森が改善票と戻る操作の修正札を青葉店へ運ぶ。営業後の模擬操作から翌日の昼へ。本編PRC-10からも同じ操作の課題を追える。修正不要。 |
| 400→401 | [ENG-21](../script/part-09.md#episode-eng-21) → [CMP-03](../script/part-10.md#episode-cmp-03) | 比較条件・実績と受取準備の改善札を13か月目の展示へ。本番採用は未決。本編407への合流には調査目的を補った。 |
| 421→422 | [PRO-07](../script/part-10.md#episode-pro-07) → [PRO-11](../script/part-10.md#episode-pro-11) | 名称と技術の相談票を国・相手先・提供物の確認へ。外部提供は構想のまま。修正不要。 |
| 441→442 | [ENG-26](../script/part-10.md#episode-eng-26) → [MNT-11](../script/part-11.md#episode-mnt-11) | 未接続の構想は調査資料に残し、現行の手順・残件を15か月目の窓口試行へ。442の画面にも月・未接続を補った。 |
| 449→450 | [ENG-22](../script/part-11.md#episode-eng-22) → [ECO-15](../script/part-12.md#episode-eco-15) | 受領した現行構成・理由・残件の資料を「終了判断・17か月目」の箱から取り出す。部境界として確認。 |
| 455→456 | [ENG-01](../script/part-12.md#episode-eng-01) → [APP-01](../script/part-13.md#episode-app-01) | 佐伯の弁当は受領済み、本筋は完結。付録は後日の新しい相談の準備。昼食を未解決に戻さない。部境界として確認。 |

## 主要伏線の確認

| 伏線 | 初出・仕込み → 変化 → 回収 | 確認結果 |
| --- | --- | --- |
| 十二時二十分・空の弁当袋 | [REQ-01](../script/part-01.md#episode-req-01) → [OPS-19](../script/part-06.md#episode-ops-19) → [TST-20](../script/part-06.md#episode-tst-20) → [ENG-01](../script/part-12.md#episode-eng-01) | 001で代替の焼き魚を渡し終える。292では通常窓口で受付、298は紙の模擬受け渡し。455は同じ時計と手元の構図で実物の弁当を渡す。十八か月の未配達にはしない。 |
| 赤いペン・赤札 | [REQ-12](../script/part-02.md#episode-req-12) → [TST-05](../script/part-05.md#episode-tst-05) → [TST-40](../script/part-05.md#episode-tst-40) → [MGT-15](../script/part-12.md#episode-mgt-15) | 015で赤ペンが登場、242で試験を分担、280で人名ではなく再現条件を指す。453は受領返答後に収納し、赤札自体は署名付き残件記録に残る。214→215の貸借・返却も確認。 |
| 青いテープ | [REQ-09](../script/part-02.md#episode-req-09) → [CMP-35](../script/part-06.md#episode-cmp-35) → [ENG-07](../script/part-09.md#episode-eng-07) | 013で閉店後に三人の動線を試す。303では通信の利用場所を確かめる背景として保持。391には初回の配置記録を補い、営業中の比較とは条件を分けた。 |
| 大きすぎる城・相原の担当札 | [ARC-05](../script/part-03.md#episode-arc-05) → [ARC-08](../script/part-03.md#episode-arc-08) → [MNT-13](../script/part-08.md#episode-mnt-13) → [ENG-02](../script/part-11.md#episode-eng-02) | 083の一人分の札と却下理由を085で保存。347と448に比較メモ・担当札を画面で再登場させた。昔の案の誤りを断定せず、人数・応答条件の変化から選び直す。 |
| 一つの注文番号 | [ENG-17](../script/part-04.md#episode-eng-17) → [CON-11](../script/part-04.md#episode-con-11) → [PRO-24](../script/part-04.md#episode-pro-24) → [OPS-15](../script/part-06.md#episode-ops-15) → [OPS-17](../script/part-07.md#episode-ops-17) | 169の101を181から217へ継続。217の札と全画面に101を指定した。前段の紙試作は注文札、132の集合照合はA〜Kの練習印に区別。289の青葉・実001、304の営業中の照合は別注文。商品番号・店舗番号・電話番号、014の番号受付の要望は注文リレーの初出とは区別。 |
| 鳴り続ける電話 | [OPS-01](../script/part-02.md#episode-ops-01) → [OPS-06](../script/part-02.md#episode-ops-06) → [OPS-20](../script/part-06.md#episode-ops-20) → [OPS-17](../script/part-07.md#episode-ops-17) → [ECO-35](../script/part-12.md#episode-eco-35) | 計画時の個人番号依存から、店舗の当番窓口・障害時の連絡分担へ。452で翌月相談の受領と当番交代を確認し、相原の祝いの席を残す。 |
| 古い台帳の文字 | [ECO-05](../script/part-01.md#episode-eco-05) → [MNT-18](../script/part-08.md#episode-mnt-18) → [ECO-24](../script/part-09.md#episode-eco-24) → [ECO-16](../script/part-12.md#episode-eco-16) | 006では勘を調べる材料として使用。350で端の「店長確認」を初めて見せ、387で相談手順の入口として参照。451で照合・復旧記録・閲覧先を確かめて保管箱へ。記録や知識は捨てない。 |
| 椅子・藤堂の不在 | [REQ-01](../script/part-01.md#episode-req-01) → [ARC-03](../script/part-03.md#episode-arc-03) → [MNT-06](../script/part-08.md#episode-mnt-06) → [MNT-11](../script/part-11.md#episode-mnt-11) → [MNT-20](../script/part-11.md#episode-mnt-20) → [ENG-02](../script/part-11.md#episode-eng-02) | 001は現場を聞く席、080・340は後の担当にも読める理由、442は別案件による午前の不在。443で図を直し、448で藤堂が提案を聞く。449の本編にもその関係を補った。死亡・失踪ではない。 |
| 温かいお茶・未使用機能 | [CON-29](../script/part-02.md#episode-con-29) → [TST-40](../script/part-05.md#episode-tst-40) → [ECO-33](../script/part-09.md#episode-eco-33) → [APP-03](../script/part-13.md#episode-app-03) | 024の速い試作、280の共同修正、390の未使用機能と温かいお茶を確認。458でも蓮は違う案を持つ相棒。常勤の六人目にはしない。 |
| 白い一ページ | [REQ-01](../script/part-01.md#episode-req-01) → [APP-01](../script/part-13.md#episode-app-01) → [APP-02](../script/part-13.md#episode-app-02) → [APP-03](../script/part-13.md#episode-app-03) | 完成画面を持ち込む001との対照。456で問いから調べ、457で目的・版を確かめ、458で新しいページに二人のペンが触れる。次話なし、明日の二つは新しい注文。 |

## 本編ルート・人物・本文の確認

- 本編の既存275接続に誤ったIDはなかった。REQ-01からENG-01まで276話、循環・欠落なし。ノート回の合流表示と終端の表記を含む124欄を、次の本編IDまたは「該当なし」に統一した。うち25欄は次の本編があるのにIDを示していなかった。
- ノートを挟む58区間を以下に記録する。129・220・280・407・438・442・449の導入を補強した。217のリレーは、本編だけでも同じ番号を追う意味が画面で分かる。
- 主要10人の話者表記は遥・藤堂・水野・森・相原・小野寺・坂本・佐伯・蓮・立花で一貫していた。電話・通話・画面越しは媒体表示であり別人物として扱わない。出演欄の役職は場面ごとの役割として照合し、職位変更と誤認する箇所は見つからなかった。449へ補った遥の動作は出演欄・人数にも反映した。
- 既存八店舗、青葉店と駅前店の試行、五人の兼務チーム、蓮の短期協力、小野寺の投資判断権を保持。時期は開始〜18か月、付録は通読後。342〜357は直前の10か月目にそろえ、050の時刻逆行に見える箇所には翌日を明記した。
- 漫画本文の「とは」「と呼ぶ」「定義」「の略」等の候補を確認。専門用語を定義する講義の混入は見つからず、仕事上の呼称・具体例は残した。補足の五見出しは全形式に存在する。
- 全台本の英語連続句を、句読点を含めて検査した。12語以上の連続した英語句は0件。確認した英語は短い節見出し・正式名称・書誌情報が中心で、長いSWEBOK英文の転載は見つからなかった。これは出典内容を全件再検証したことを意味しない。

| 前の本編 | 次の本編 | 間のノート数 |
| --- | --- | ---: |
| [ECO-01](../script/part-02.md#episode-eco-01)（023） | [ECO-07](../script/part-02.md#episode-eco-07)（028） | 4 |
| [MGT-03](../script/part-02.md#episode-mgt-03)（032） | [MGT-04](../script/part-02.md#episode-mgt-04)（034） | 1 |
| [ECO-10](../script/part-02.md#episode-eco-10)（040） | [OPS-01](../script/part-02.md#episode-ops-01)（042） | 1 |
| [PRC-01](../script/part-02.md#episode-prc-01)（049） | [PRC-03](../script/part-02.md#episode-prc-03)（051） | 1 |
| [PRC-03](../script/part-02.md#episode-prc-03)（051） | [PRC-07](../script/part-02.md#episode-prc-07)（053） | 1 |
| [PRO-21](../script/part-02.md#episode-pro-21)（065） | [ECO-28](../script/part-02.md#episode-eco-28)（068） | 2 |
| [REQ-10](../script/part-03.md#episode-req-10)（070） | [REQ-15](../script/part-03.md#episode-req-15)（073） | 2 |
| [ARC-05](../script/part-03.md#episode-arc-05)（083） | [ARC-08](../script/part-03.md#episode-arc-08)（085） | 1 |
| [DES-02](../script/part-03.md#episode-des-02)（090） | [DES-03](../script/part-03.md#episode-des-03)（092） | 1 |
| [DES-06](../script/part-03.md#episode-des-06)（096） | [DES-07](../script/part-03.md#episode-des-07)（098） | 1 |
| [DES-07](../script/part-03.md#episode-des-07)（098） | [DES-08](../script/part-03.md#episode-des-08)（100） | 1 |
| [DES-11](../script/part-03.md#episode-des-11)（106） | [DES-14](../script/part-03.md#episode-des-14)（109） | 2 |
| [DES-15](../script/part-03.md#episode-des-15)（111） | [DES-21](../script/part-03.md#episode-des-21)（113） | 1 |
| [TST-03](../script/part-03.md#episode-tst-03)（115） | [SEC-07](../script/part-03.md#episode-sec-07)（117） | 1 |
| [SEC-07](../script/part-03.md#episode-sec-07)（117） | [PRO-14](../script/part-03.md#episode-pro-14)（120） | 2 |
| [PRO-22](../script/part-03.md#episode-pro-22)（123） | [CMP-37](../script/part-03.md#episode-cmp-37)（129） | 5 |
| [CMP-37](../script/part-03.md#episode-cmp-37)（129） | [ENG-03](../script/part-03.md#episode-eng-03)（135） | 5 |
| [ENG-03](../script/part-03.md#episode-eng-03)（135） | [ENG-14](../script/part-03.md#episode-eng-14)（139） | 3 |
| [ENG-14](../script/part-03.md#episode-eng-14)（139） | [MGT-09](../script/part-04.md#episode-mgt-09)（149） | 9 |
| [CMP-20](../script/part-04.md#episode-cmp-20)（151） | [DES-04](../script/part-04.md#episode-des-04)（158） | 6 |
| [MGT-11](../script/part-04.md#episode-mgt-11)（159） | [MGT-12](../script/part-04.md#episode-mgt-12)（161） | 1 |
| [MGT-12](../script/part-04.md#episode-mgt-12)（161） | [MGT-19](../script/part-04.md#episode-mgt-19)（163） | 1 |
| [MGT-19](../script/part-04.md#episode-mgt-19)（163） | [CON-01](../script/part-04.md#episode-con-01)（170） | 6 |
| [CON-08](../script/part-04.md#episode-con-08)（178） | [CON-10](../script/part-04.md#episode-con-10)（180） | 1 |
| [CON-13](../script/part-04.md#episode-con-13)（182） | [MOD-18](../script/part-04.md#episode-mod-18)（187） | 4 |
| [MOD-18](../script/part-04.md#episode-mod-18)（187） | [CON-17](../script/part-04.md#episode-con-17)（189） | 1 |
| [CON-19](../script/part-04.md#episode-con-19)（190） | [CON-26](../script/part-04.md#episode-con-26)（194） | 3 |
| [QUA-11](../script/part-04.md#episode-qua-11)（197） | [TST-01](../script/part-04.md#episode-tst-01)（199） | 1 |
| [OPS-03](../script/part-04.md#episode-ops-03)（202） | [CFG-03](../script/part-04.md#episode-cfg-03)（204） | 1 |
| [PRO-24](../script/part-04.md#episode-pro-24)（217） | [MOD-11](../script/part-05.md#episode-mod-11)（220） | 2 |
| [ARC-13](../script/part-05.md#episode-arc-13)（221） | [DES-26](../script/part-05.md#episode-des-26)（229） | 7 |
| [CON-12](../script/part-05.md#episode-con-12)（233） | [QUA-12](../script/part-05.md#episode-qua-12)（236） | 2 |
| [QUA-12](../script/part-05.md#episode-qua-12)（236） | [QUA-16](../script/part-05.md#episode-qua-16)（239） | 2 |
| [TST-05](../script/part-05.md#episode-tst-05)（242） | [OPS-05](../script/part-05.md#episode-ops-05)（244） | 1 |
| [SEC-14](../script/part-05.md#episode-sec-14)（250） | [PRO-12](../script/part-05.md#episode-pro-12)（252） | 1 |
| [TST-13](../script/part-05.md#episode-tst-13)（253） | [TST-16](../script/part-05.md#episode-tst-16)（255） | 1 |
| [TST-19](../script/part-05.md#episode-tst-19)（259） | [TST-27](../script/part-05.md#episode-tst-27)（266） | 6 |
| [TST-27](../script/part-05.md#episode-tst-27)（266） | [OPS-11](../script/part-05.md#episode-ops-11)（269） | 2 |
| [OPS-11](../script/part-05.md#episode-ops-11)（269） | [OPS-12](../script/part-05.md#episode-ops-12)（271） | 1 |
| [OPS-12](../script/part-05.md#episode-ops-12)（271） | [OPS-13](../script/part-05.md#episode-ops-13)（273） | 1 |
| [OPS-13](../script/part-05.md#episode-ops-13)（273） | [TST-39](../script/part-05.md#episode-tst-39)（278） | 4 |
| [TST-39](../script/part-05.md#episode-tst-39)（278） | [TST-40](../script/part-05.md#episode-tst-40)（280） | 1 |
| [TST-43](../script/part-05.md#episode-tst-43)（282） | [OPS-14](../script/part-05.md#episode-ops-14)（284） | 1 |
| [MGT-08](../script/part-07.md#episode-mgt-08)（310） | [ENG-23](../script/part-07.md#episode-eng-23)（322） | 11 |
| [ENG-23](../script/part-07.md#episode-eng-23)（322） | [REQ-19](../script/part-08.md#episode-req-19)（324） | 1 |
| [PRO-25](../script/part-08.md#episode-pro-25)（328） | [DES-12](../script/part-08.md#episode-des-12)（330） | 1 |
| [MNT-02](../script/part-08.md#episode-mnt-02)（335） | [MNT-04](../script/part-08.md#episode-mnt-04)（337） | 1 |
| [ARC-14](../script/part-09.md#episode-arc-14)（360） | [MNT-14](../script/part-09.md#episode-mnt-14)（370） | 9 |
| [CON-25](../script/part-09.md#episode-con-25)（373） | [PRC-10](../script/part-09.md#episode-prc-10)（375） | 1 |
| [PRC-10](../script/part-09.md#episode-prc-10)（375） | [QUA-06](../script/part-09.md#episode-qua-06)（380） | 4 |
| [QUA-17](../script/part-09.md#episode-qua-17)（382） | [PRO-05](../script/part-09.md#episode-pro-05)（384） | 1 |
| [ECO-23](../script/part-09.md#episode-eco-23)（386） | [ECO-25](../script/part-09.md#episode-eco-25)（388） | 1 |
| [ENG-09](../script/part-09.md#episode-eng-09)（392） | [ENG-21](../script/part-09.md#episode-eng-21)（400） | 7 |
| [ENG-21](../script/part-09.md#episode-eng-21)（400） | [MNT-17](../script/part-10.md#episode-mnt-17)（407） | 6 |
| [MNT-17](../script/part-10.md#episode-mnt-17)（407） | [CMP-44](../script/part-10.md#episode-cmp-44)（438） | 30 |
| [CMP-44](../script/part-10.md#episode-cmp-44)（438） | [MNT-11](../script/part-11.md#episode-mnt-11)（442） | 3 |
| [MNT-20](../script/part-11.md#episode-mnt-20)（443） | [PRO-03](../script/part-11.md#episode-pro-03)（445） | 1 |
| [CMP-38](../script/part-11.md#episode-cmp-38)（447） | [ENG-22](../script/part-11.md#episode-eng-22)（449） | 1 |

## 修正一覧

話数・ID・通読順・形式・採用タイトル・サブタイトルは変更していない。導線表記以外の接続修正は41話（16話の時期限定、2話のチャンク参照の置換を含む）。導線表記を合わせると変更対象は158話。下表は同じ話の複数の変更をまとめたもの。

| 通読順・話 | 修正内容・理由 |
| --- | --- |
| 030 [ECO-09](../script/part-02.md#episode-eco-09) | 029→030：会議場所を前話にそろえる。 |
| 050 [PRC-02](../script/part-02.md#episode-prc-02) | 049→050：十五時の共同確認後に日をまたぐ。／049→050：前話の「昨日・試作の全体方針」と日付を合わせる。／049→050：制作メモにも経過日を残す。 |
| 051 [PRC-03](../script/part-02.md#episode-prc-03) | 本編049→051：ノート050を飛ばしても日付を追える。 |
| 117 [SEC-07](../script/part-03.md#episode-sec-07) | 116→117：引き継いだ権限の空欄を同じ表記で受ける。 |
| 129 [CMP-37](../script/part-03.md#episode-cmp-37) | 本編123→129：比較ノートの場所を知らなくても場面が分かる。 |
| 132 [MTH-07](../script/part-03.md#episode-mth-07) | 132→133：集合照合の印をA〜Kにし、169の注文番号の初出と区別（十件・九件・共通八件は維持）。／132：照合練習と後の注文リレーを制作メモでも区別。 |
| 133 [MTH-08](../script/part-03.md#episode-mth-08) | 132→133：前話から受け取る未照合札の印を合わせる。 |
| 135 [ENG-03](../script/part-03.md#episode-eng-03) | 注文番号の初出169を守り、紙画面の段階は注文札で示す。／135：注文番号の初出169より前の紙画面の表記を統一。 |
| 136 [ENG-04](../script/part-03.md#episode-eng-04) | 注文番号の初出169を守り、紙画面の段階は注文札で示す。 |
| 137 [ENG-05](../script/part-03.md#episode-eng-05) | 注文番号の初出169を守り、紙の試作の受け渡しにそろえる。 |
| 139 [ENG-14](../script/part-03.md#episode-eng-14) | 注文番号の初出169を守り、部末も紙の試作として受ける。 |
| 168 [MTH-20](../script/part-04.md#episode-mth-20) | 168→169：番号の表面を見せるのは次話に残す。 |
| 169 [ENG-17](../script/part-04.md#episode-eng-17) | 168→169：裏返した札を受け取り、101を初めて見せる。 |
| 217 [PRO-24](../script/part-04.md#episode-pro-24) | 181→217：同じ試験用番号のリレーを画面で回収。／217：試験用番号を指定し、実注文との区別を固定。／169→181→217→289：番号の状態を制作メモにも記録。 |
| 220 [MOD-11](../script/part-05.md#episode-mod-11) | 本編217→220：月と試す順序を再提示。／本編217→220：ノート回の前提を制作メモにも補う。 |
| 280 [TST-40](../script/part-05.md#episode-tst-40) | 本編278→280：ENG-13を飛ばしても失敗の内容が分かる。 |
| 289 [OPS-15](../script/part-06.md#episode-ops-15) | 統合後も参照できる話IDへ制作メモを置き換える。 |
| 305 [OPS-04](../script/part-07.md#episode-ops-04) | 統合後の正本の単位へ制作メモを置き換える。 |
| 342 [MNT-07](../script/part-08.md#episode-mnt-07) | 341以降：10か月目の継続場面として時期を明確化。／341→342：同じ変更作業の継続を明記。／341→342：本文にも時期の継続を表示。 |
| 343 [MNT-08](../script/part-08.md#episode-mnt-08) | 341以降：10か月目の継続場面として時期を明確化。 |
| 344 [MNT-09](../script/part-08.md#episode-mnt-09) | 341以降：10か月目の継続場面として時期を明確化。 |
| 345 [MNT-10](../script/part-08.md#episode-mnt-10) | 341以降：10か月目の継続場面として時期を明確化。 |
| 346 [MNT-12](../script/part-08.md#episode-mnt-12) | 341以降：10か月目の継続場面として時期を明確化。 |
| 347 [MNT-13](../script/part-08.md#episode-mnt-13) | 341以降：10か月目の継続場面として時期を明確化。／083→085→347：当時の制約と判断理由を見える形で参照。 |
| 348 [MNT-15](../script/part-08.md#episode-mnt-15) | 341以降：10か月目の継続場面として時期を明確化。 |
| 349 [MNT-16](../script/part-08.md#episode-mnt-16) | 341以降：10か月目の継続場面として時期を明確化。 |
| 350 [MNT-18](../script/part-08.md#episode-mnt-18) | 341以降：10か月目の継続場面として時期を明確化。 |
| 351 [MNT-19](../script/part-08.md#episode-mnt-19) | 341以降：10か月目の継続場面として時期を明確化。 |
| 352 [CFG-06](../script/part-08.md#episode-cfg-06) | 341以降：10か月目の継続場面として時期を明確化。 |
| 353 [CFG-11](../script/part-08.md#episode-cfg-11) | 341以降：10か月目の継続場面として時期を明確化。 |
| 354 [PRC-11](../script/part-08.md#episode-prc-11) | 341以降：10か月目の継続場面として時期を明確化。 |
| 355 [PRC-14](../script/part-08.md#episode-prc-14) | 341以降：10か月目の継続場面として時期を明確化。 |
| 356 [MOD-10](../script/part-08.md#episode-mod-10) | 341以降：10か月目の継続場面として時期を明確化。 |
| 357 [QUA-09](../script/part-08.md#episode-qua-09) | 341以降：10か月目の継続場面として時期を明確化。 |
| 359 [REQ-24](../script/part-09.md#episode-req-24) | 358→359→360：「新しいお願いは増えていない」と引きの整合。 |
| 391 [ENG-07](../script/part-09.md#episode-eng-07) | 013→391：初回の限定試行を具体的な記録として再参照。／013→391：初回と今回を同一条件の効果として扱わない。 |
| 407 [MNT-17](../script/part-10.md#episode-mnt-17) | 本編400→407：展示のノートを飛ばしても調査目的を受け取れる。 |
| 438 [CMP-44](../script/part-10.md#episode-cmp-44) | 本編407→438：調査の経過と本番未採用を場面内で再提示。 |
| 442 [MNT-11](../script/part-11.md#episode-mnt-11) | 本編438→442：外部調査から現行業務への復帰を表示。 |
| 448 [ENG-02](../script/part-11.md#episode-eng-02) | 083→085→448：制作メモにあった担当札を実際の画面へ置く。 |
| 449 [ENG-22](../script/part-11.md#episode-eng-22) | 本編447→449：ENG-02を飛ばしても提案を聞く関係への変化が見える。／本編447→449：関係の回収と現行版・試作の区別を保持。／449：補った遥の動作を出演欄へ反映。／449：出演人数を画面指示と整合。 |

導線表記を統一した全124欄（右列は修正後の値）。本編から本編への接続先自体は変更していない。

| 対象話 | 本編のみの次話 |
| --- | --- |
| [CON-29](../script/part-02.md#episode-con-29)、[ECO-02](../script/part-02.md#episode-eco-02)、[ECO-03](../script/part-02.md#episode-eco-03)、[ECO-04](../script/part-02.md#episode-eco-04) | [ECO-07](../script/part-02.md#episode-eco-07) |
| [TST-44](../script/part-02.md#episode-tst-44) | [MGT-04](../script/part-02.md#episode-mgt-04) |
| [ECO-13](../script/part-02.md#episode-eco-13) | [OPS-01](../script/part-02.md#episode-ops-01) |
| [SEC-08](../script/part-03.md#episode-sec-08)、[SEC-09](../script/part-03.md#episode-sec-09) | [PRO-14](../script/part-03.md#episode-pro-14) |
| [CMP-14](../script/part-03.md#episode-cmp-14)、[CMP-24](../script/part-03.md#episode-cmp-24)、[CMP-25](../script/part-03.md#episode-cmp-25)、[CMP-26](../script/part-03.md#episode-cmp-26)、[CMP-30](../script/part-03.md#episode-cmp-30) | [CMP-37](../script/part-03.md#episode-cmp-37) |
| [MTH-01](../script/part-03.md#episode-mth-01)、[MTH-02](../script/part-03.md#episode-mth-02)、[MTH-07](../script/part-03.md#episode-mth-07)、[MTH-08](../script/part-03.md#episode-mth-08)、[MTH-11](../script/part-03.md#episode-mth-11) | [ENG-03](../script/part-03.md#episode-eng-03) |
| [ENG-04](../script/part-03.md#episode-eng-04)、[ENG-05](../script/part-03.md#episode-eng-05)、[ENG-06](../script/part-03.md#episode-eng-06) | [ENG-14](../script/part-03.md#episode-eng-14) |
| [TST-06](../script/part-05.md#episode-tst-06) | [OPS-05](../script/part-05.md#episode-ops-05) |
| [TST-12](../script/part-05.md#episode-tst-12) | [PRO-12](../script/part-05.md#episode-pro-12) |
| [CMP-36](../script/part-05.md#episode-cmp-36) | [TST-16](../script/part-05.md#episode-tst-16) |
| [TST-21](../script/part-05.md#episode-tst-21)、[TST-22](../script/part-05.md#episode-tst-22)、[TST-23](../script/part-05.md#episode-tst-23)、[TST-24](../script/part-05.md#episode-tst-24)、[TST-25](../script/part-05.md#episode-tst-25)、[TST-26](../script/part-05.md#episode-tst-26) | [TST-27](../script/part-05.md#episode-tst-27) |
| [TST-28](../script/part-05.md#episode-tst-28)、[TST-30](../script/part-05.md#episode-tst-30) | [OPS-11](../script/part-05.md#episode-ops-11) |
| [TST-31](../script/part-05.md#episode-tst-31) | [OPS-12](../script/part-05.md#episode-ops-12) |
| [TST-32](../script/part-05.md#episode-tst-32) | [OPS-13](../script/part-05.md#episode-ops-13) |
| [TST-34](../script/part-05.md#episode-tst-34)、[CMP-29](../script/part-05.md#episode-cmp-29)、[TST-36](../script/part-05.md#episode-tst-36)、[ENG-12](../script/part-05.md#episode-eng-12) | [TST-39](../script/part-05.md#episode-tst-39) |
| [ENG-13](../script/part-05.md#episode-eng-13) | [TST-40](../script/part-05.md#episode-tst-40) |
| [TST-49](../script/part-05.md#episode-tst-49) | [OPS-14](../script/part-05.md#episode-ops-14) |
| [ECO-19](../script/part-07.md#episode-eco-19)、[ECO-20](../script/part-07.md#episode-eco-20)、[CMP-10](../script/part-07.md#episode-cmp-10)、[CMP-11](../script/part-07.md#episode-cmp-11)、[CMP-12](../script/part-07.md#episode-cmp-12)、[CMP-13](../script/part-07.md#episode-cmp-13)、[CMP-21](../script/part-07.md#episode-cmp-21)、[CMP-22](../script/part-07.md#episode-cmp-22)、[CMP-23](../script/part-07.md#episode-cmp-23)、[CMP-31](../script/part-07.md#episode-cmp-31)、[CMP-34](../script/part-07.md#episode-cmp-34) | [ENG-23](../script/part-07.md#episode-eng-23) |
| [ENG-24](../script/part-07.md#episode-eng-24) | [REQ-19](../script/part-08.md#episode-req-19) |
| [MTH-09](../script/part-08.md#episode-mth-09) | [DES-12](../script/part-08.md#episode-des-12) |
| [MNT-03](../script/part-08.md#episode-mnt-03) | [MNT-04](../script/part-08.md#episode-mnt-04) |
| [CMP-28](../script/part-09.md#episode-cmp-28)、[MTH-18](../script/part-09.md#episode-mth-18)、[MTH-19](../script/part-09.md#episode-mth-19)、[MTH-21](../script/part-09.md#episode-mth-21)、[MTH-22](../script/part-09.md#episode-mth-22)、[MTH-23](../script/part-09.md#episode-mth-23)、[MTH-24](../script/part-09.md#episode-mth-24)、[MTH-25](../script/part-09.md#episode-mth-25)、[DES-27](../script/part-09.md#episode-des-27) | [MNT-14](../script/part-09.md#episode-mnt-14) |
| [TST-29](../script/part-09.md#episode-tst-29) | [PRC-10](../script/part-09.md#episode-prc-10) |
| [TST-37](../script/part-09.md#episode-tst-37)、[PRC-12](../script/part-09.md#episode-prc-12)、[TST-38](../script/part-09.md#episode-tst-38)、[PRC-13](../script/part-09.md#episode-prc-13) | [QUA-06](../script/part-09.md#episode-qua-06) |
| [SEC-02](../script/part-09.md#episode-sec-02) | [PRO-05](../script/part-09.md#episode-pro-05) |
| [ECO-24](../script/part-09.md#episode-eco-24) | [ECO-25](../script/part-09.md#episode-eco-25) |
| [ENG-10](../script/part-09.md#episode-eng-10)、[ENG-11](../script/part-09.md#episode-eng-11)、[ENG-15](../script/part-09.md#episode-eng-15)、[ENG-16](../script/part-09.md#episode-eng-16)、[ENG-18](../script/part-09.md#episode-eng-18)、[ENG-19](../script/part-09.md#episode-eng-19)、[ENG-20](../script/part-09.md#episode-eng-20) | [ENG-21](../script/part-09.md#episode-eng-21) |
| [CMP-03](../script/part-10.md#episode-cmp-03)、[CMP-04](../script/part-10.md#episode-cmp-04)、[CMP-05](../script/part-10.md#episode-cmp-05)、[MTH-15](../script/part-10.md#episode-mth-15)、[MTH-26](../script/part-10.md#episode-mth-26)、[ARC-06](../script/part-10.md#episode-arc-06) | [MNT-17](../script/part-10.md#episode-mnt-17) |
| [MNT-17](../script/part-10.md#episode-mnt-17)、[DES-17](../script/part-10.md#episode-des-17)、[SEC-05](../script/part-10.md#episode-sec-05)、[DES-24](../script/part-10.md#episode-des-24)、[CON-18](../script/part-10.md#episode-con-18)、[SEC-17](../script/part-10.md#episode-sec-17)、[CON-24](../script/part-10.md#episode-con-24)、[TST-45](../script/part-10.md#episode-tst-45)、[SEC-18](../script/part-10.md#episode-sec-18)、[TST-46](../script/part-10.md#episode-tst-46)、[TST-47](../script/part-10.md#episode-tst-47)、[TST-48](../script/part-10.md#episode-tst-48)、[TST-50](../script/part-10.md#episode-tst-50)、[TST-51](../script/part-10.md#episode-tst-51)、[PRO-07](../script/part-10.md#episode-pro-07)、[PRO-11](../script/part-10.md#episode-pro-11)、[ECO-11](../script/part-10.md#episode-eco-11)、[ECO-14](../script/part-10.md#episode-eco-14)、[ECO-17](../script/part-10.md#episode-eco-17)、[ECO-18](../script/part-10.md#episode-eco-18)、[ECO-21](../script/part-10.md#episode-eco-21)、[ECO-22](../script/part-10.md#episode-eco-22)、[ECO-30](../script/part-10.md#episode-eco-30)、[ECO-32](../script/part-10.md#episode-eco-32)、[ECO-34](../script/part-10.md#episode-eco-34)、[ECO-36](../script/part-10.md#episode-eco-36)、[CMP-39](../script/part-10.md#episode-cmp-39)、[CMP-40](../script/part-10.md#episode-cmp-40)、[CMP-41](../script/part-10.md#episode-cmp-41)、[CMP-42](../script/part-10.md#episode-cmp-42)、[CMP-43](../script/part-10.md#episode-cmp-43) | [CMP-44](../script/part-10.md#episode-cmp-44) |
| [CMP-44](../script/part-10.md#episode-cmp-44)、[MTH-27](../script/part-10.md#episode-mth-27)、[MTH-28](../script/part-10.md#episode-mth-28)、[ENG-26](../script/part-10.md#episode-eng-26) | [MNT-11](../script/part-11.md#episode-mnt-11) |
| [PRO-01](../script/part-11.md#episode-pro-01) | [PRO-03](../script/part-11.md#episode-pro-03) |
| [ENG-02](../script/part-11.md#episode-eng-02) | [ENG-22](../script/part-11.md#episode-eng-22) |
| [ENG-01](../script/part-12.md#episode-eng-01)、[APP-01](../script/part-13.md#episode-app-01)、[APP-02](../script/part-13.md#episode-app-02)、[APP-03](../script/part-13.md#episode-app-03) | 該当なし |

## 統合と検証結果

`tools/assemble_script.py` を作成。初回は22チャンクを検証してmanifestの範囲へ統合し、部冒頭4行と話ID由来の明示アンカーを付ける。チャンクコメントは除去。書き出した正本を読み直して検証し、目次を生成してから入力チャンクを削除した。以後の追加修正は部ファイルへ直接適用した。
`--assemble` は既存正本の上書きを拒否する。通常は `--check`、目次の更新には `--index` を使う。chunks削除後も両コマンドが動く。全体あらすじは20行、部別目次は458行で、本編順1〜276も表示する。READMEと執筆計画の台本配置案内も現状に合わせた。

| 部 | 通読順 | 全話 | 本編 | 結果 |
| --- | --- | ---: | ---: | --- |
| 1 | 001〜008 | 8 | 8 | 一致 |
| 2 | 009〜069 | 61 | 51 | 一致 |
| 3 | 070〜139 | 70 | 45 | 一致 |
| 4 | 140〜217 | 78 | 44 | 一致 |
| 5 | 218〜288 | 71 | 39 | 一致 |
| 6 | 289〜303 | 15 | 15 | 一致 |
| 7 | 304〜323 | 20 | 8 | 一致 |
| 8 | 324〜358 | 35 | 33 | 一致 |
| 9 | 359〜400 | 42 | 19 | 一致 |
| 10 | 401〜441 | 41 | 2 | 一致 |
| 11 | 442〜449 | 8 | 6 | 一致 |
| 12 | 450〜455 | 6 | 6 | 一致 |
| 13 | 456〜458 | 3 | 0 | 一致 |
| 合計 | 001〜458 | 458 | 276 | 合格 |

- `python tools/assemble_script.py --check`：全13部の話数・所属ID・形式別件数、通読順001〜458、索引のタイトル・サブタイトル、必須8見出し、制作メモ・引きの欄、3〜6コマの連番と画面指示／セリフ／モノローグ／効果音を検証。
- 全形式457接続と終端、本編275接続と終端、ノートから本編への合流先を検証。458話のアンカーと目次を正本から照合。
- 負例8種類（話欠落、ID重複、順序交換、必須見出し欠落、本編次話の誤り、部所属違い、コマ欄欠落、アンカー違い）がすべて検証エラーになることを確認。
- 一時ディレクトリに正本から22チャンクを再構成し、統合を再実行。13部とREADMEが正本とバイト単位で一致し、検証後にチャンクが消えることを確認。不正入力では22チャンクが保持され、部ファイルが作られないことも確認。
- `--check`／`--index` の再実行と `--assemble` の上書き拒否を確認。正本のハッシュは変わらなかった。検証用の負例は一時領域だけに作成し、台本へ混入させていない。

## 残る課題と、物語上残す仕事

- MTH-19（363）の「補足出典要」は維持。今回、条件付き確率の公式や定義を追加していない。追加出典の調査は技術監修で扱う。
- 補足の全件再監修、法律・規格・製品の個別の現行性確認、作画、吹き出し・図表の実寸確認は本フェーズの完了に含めない。各話の制作状態にある未確認事項を引き続き管理する。PRO-24の6人・6コマ、ENG-01の7人・6コマ等は作画時に読み順と文字量を確認する。
- 小道具を補ったコマ1の情報量（347・391・448等）は絵コンテで確認する。物語の出来事を増やさず、資料や札の小さな参照で接続した。
- OPS-19の原因調査、OPS-16のデータ変更候補、全店障害の恒久対応、外部連携・新技術・専門家への照会には、作中で未解決・未採用として残るものがある。確認できた範囲から勝手に解決済みへ進めていない。既存の担当付き残件と採否理由を引き継ぎ資料として扱う。
- 最終回の別枠の待ちは意図して残す仕事。MGT-15で受領・担当・翌週の調査予定を確認済みであり、全客の待ちがなくなった結末ではない。古い台帳は保管、赤札は残件記録、製造連携は未接続の構想として、それぞれの状態を保持する。
- 今回の接続校閲で、未修正の重大な境界矛盾は見つかっていない。全文の表現を磨く二次推敲や技術監修まで完了したとは扱わない。
