# Image-to-MFM
- Q.なにこれ？ A.画像をMFMに変換するPythonプログラムです

# 使い方
1. file_set.txtの1行目に 0 または 1 を入力
   - 0 = 6桁RGBで出力
   - 1 = 4桁RGBAで出力
2. file_set.txtの2行目にファイルへのパスを入力
3. あとは ImageToMFM.py を実行するだけ。MFMが書かれた.txtが出力されてるはず。

# スケールや使用する文字のおすすめ
- ノートの場合のおすすめ
  - ノートだとそもそもでそんな大きいMFMにできず、頑張っても14x14pxくらい。
  - scale = "$[scale.y=0.7 "
  - space_char = "　" # 全角スペース
  - 画像サイズ……14x14、13x13、14x10（全てのドットに別々の色がついてる場合）

- ページの場合
  - ページなら文字数の制限が無いのでいくらでも大きいMFMで可能……とは言っても横幅に制限あるので注意
  - scale = "$[scale.y=0.185 "
  - space_char = " " # 半角スペース
  - 画像サイズ……横幅最大128px（機種ごとに横幅の表示が変わる可能性あるので、それを考慮すると100pxくらい……？）
