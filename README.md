# line_follow
2019 Taiwan TDK Robocon
主要的code在follow_kine.py內

A 方案 作法為:
    從圖片的底部使用一個 windows 滑過去將黑色面積最大的部分框起來，以此類推座兩層，因為超過3層之後對飛行器其實沒有相對性的重要。觀看斜率來調整飛行

B 方案 作法為:
    因本次比賽飛行器皆為轉左邊。所以在圖片的最左邊設置一個 windows ，
    一樣是框住黑色最多的部分，再來就是判斷遠近，到達某個特定的閥值後。就使其轉向。

test_data資料夾中有一部測試影片，可拿 2jpg 轉成一張張 jpg 每秒 8 帪，放到 main 去跑完後可再拿 2video 轉成影片

2019.07.17
  新增 在 windows 中畫出中心點並且與該層中心點連線。
2019.08.27
  結論，處理時間過於長，已經嘗試多種降速方案，演算法整體設計不良，廢案。(´ﾟдﾟ`)
