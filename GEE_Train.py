import streamlit as st
#st.title("Google Earth Engine による崩壊地自動抽出")
# Draw a title and some text to the app:
'''
# 途上国におけるGoogle Earth Engineを用いた斜面崩壊地の自動抽出

2022/12/6 講師　**大丸裕武（石川県立大学）**

- 衛星ビッグデータの世界
    - GEEの特徴
        - 単純作業を自動化
        - 膨大なデータへのアクセス
        - Googleは正義の味方か？
        - GEEで利用できるデータ
        - 豊富なドキュメント
        - 圧倒的なコスト
        - 残念なところ
- GEEを使ってみよう!
    - JavaScriptの基本: [01_IntroJS](https://code.earthengine.google.com/fcada23cb52c819892d7819a50033c02)
    - GEEで使われる基本的な記述パターン: [02_Data_GEE](https://code.earthengine.google.com/b8b332f7e15407756e26ffe8eaf41833)
    - 関数: [03_function_basic](https://code.earthengine.google.com/173cdb20ae1ee5013ba172dfe8375c0e)
    - バンドの合成と画面への表示: [04_Landsat Composite](https://code.earthengine.google.com/169fd8bfe52258d90e92b72d3e766531)
    - バンドの生成: [05-NDVI](https://code.earthengine.google.com/68e9d535ebcf0af03f01112cb962bad2)
    - 計算結果の追加と名称の変更: [06_add_nd_def](https://code.earthengine.google.com/d6eac15a66f996443b5bbaa5c0f359bd)
    - 時系列データを用いて崩壊地の自動抽出に挑戦: [07_RF_2018Hiroshima](https://code.earthengine.google.com/80609dd5e2185c547aeef95aa4096d57)
    - データのエクスポートと再利用: [07_RF_2018Hiroshima](https://code.earthengine.google.com/80609dd5e2185c547aeef95aa4096d57)
    - 出力したデータをQGISで見てみよう
    - ベトナム山岳地域での利用例: [08_Cart_west_YenBai](https://code.earthengine.google.com/fa970d0cab97d2502217034bf28f2038)
    - さらに学びを深めるために
    - JavaScript or Python?

- 動画によるポイント解説
    - [教師付き分類](https://www.youtube.com/watch?v=VMab-HAXOpw)
    - 教師データの作成
'''

st.subheader('動画によるポイント解説')
st.video('make_feature_collection.mp4', format="video/mp4")


