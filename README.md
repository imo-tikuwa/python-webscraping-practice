# python-webscraping-practice

## app1.py
beautifulsoup4でヤフー天気の地図を1日分スクレイピングするサンプルプログラム  

## app2.py
beautifulsoup4、seleniumでヤフー天気の地図を8日分スクレイピングするサンプルプログラム  
日付ごとにページを読み込みにいっているためあまり良くない  

## app3.py
beautifulsoup4、seleniumでヤフー天気の地図を8日分スクレイピングするサンプルプログラム  
2～8日目は日付ボタンをクリックしてajaxで変化した画面から取得している  
app2.pyを少し改善したもの  
ボタンクリック後の待機処理はtime.sleepではなくWaitを使用  
