# python-webscraping-practice
作ったプログラムについて

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

## login.py
ログインを行った先のコンテンツを取得するサンプルプログラム  
※スクレイピングの練習の使用が許可されている[Webスクレイピング入門者のためのサイト](https://scraping-for-beginner.herokuapp.com/)を利用させていただきました。  

## ranking.py
一覧画面（ページ遷移あり）のコンテンツを取得するサンプルプログラム  
※login.pyと同様のサイトを利用。

## image.py
Webページ内の画像ファイルをローカルに保存するサンプルプログラム  
※login.pyと同様のサイトを利用。
