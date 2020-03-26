from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
import datetime

# 練習として使うことを許可しているサイトで画像を収集する
# 練習サイト
# Webスクレイピング入門者のためのサイト
# https://scraping-for-beginner.herokuapp.com/

def get_current_time():
    # 現在の時間を返す
    return datetime.datetime.now().strftime("%H:%M:%S.%f")


print("{0} start".format(get_current_time()))

# 画像保存ディレクトリ
IMAGE_SAVE_DIR = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'images' + os.sep

# 画像ギャラリーのURL
GARALLY_URL = 'https://scraping-for-beginner.herokuapp.com/image'

# 画像ギャラリーの画面を開く
driver = webdriver.Chrome(executable_path = 'C:\\python\\chromedriver_win32\\chromedriver.exe')
driver.get(GARALLY_URL)
print("{0} page loaded {1}".format(get_current_time(), GARALLY_URL))

# 画像を含むdiv要素のリストを取得
image_elements = driver.find_elements_by_css_selector('div.row.card > div.col')

# 項目名と値を出力（改行がある場合は読点に置換して表示）
for image_element in image_elements:

    # 画像のファイルパスとファイル名を取得
    image_path = image_element.find_element_by_tag_name('img').get_attribute('src')
    image_name = os.path.basename(image_path)

    # 画像を読み込み
    print("{0} image read before {1}".format(get_current_time(), image_name))
    image_data = urllib.request.urlopen(image_path).read()
    print("{0} image read after  {1}".format(get_current_time(), image_name))

    # ローカルのimagesディレクトリに保存
    with open(IMAGE_SAVE_DIR + image_name, mode = "wb") as f:
        f.write(image_data)
        print("{0} image saved       {1}".format(get_current_time(), image_name))

# ブラウザを閉じる
driver.close()


# 00:22:03.286852 start
# 00:22:13.036854 page loaded https://scraping-for-beginner.herokuapp.com/image
# 00:22:13.078854 image read before img1.JPG
# 00:22:15.138856 image read after  img1.JPG
# 00:22:15.139854 image saved       img1.JPG
# 00:22:15.160853 image read before img2.JPG
# 00:22:16.506855 image read after  img2.JPG
# 00:22:16.507855 image saved       img2.JPG
# 00:22:16.529854 image read before img3.JPG
# 00:22:18.031855 image read after  img3.JPG
# 00:22:18.032856 image saved       img3.JPG
# 00:22:18.047855 image read before img4.JPG
# 00:22:19.891855 image read after  img4.JPG
# 00:22:19.892852 image saved       img4.JPG
# 00:22:19.910855 image read before img5.JPG
# 00:22:21.455854 image read after  img5.JPG
# 00:22:21.455854 image saved       img5.JPG
# 00:22:21.474855 image read before img6.JPG
# 00:22:22.963854 image read after  img6.JPG
# 00:22:22.964856 image saved       img6.JPG
# 00:22:22.982854 image read before img7.JPG
# 00:22:24.973854 image read after  img7.JPG
# 00:22:24.974854 image saved       img7.JPG
# 00:22:24.992856 image read before img8.JPG
# 00:22:28.818854 image read after  img8.JPG
# 00:22:28.819856 image saved       img8.JPG
# 00:22:28.838854 image read before img9.JPG
# 00:22:30.189853 image read after  img9.JPG
# 00:22:30.189853 image saved       img9.JPG
# 00:22:30.205854 image read before img10.JPG
# 00:22:31.543852 image read after  img10.JPG
# 00:22:31.544852 image saved       img10.JPG
# 00:22:31.561854 image read before img11.JPG
# 00:22:32.930853 image read after  img11.JPG
# 00:22:32.931853 image saved       img11.JPG
# 00:22:32.955853 image read before img12.JPG
# 00:22:34.344855 image read after  img12.JPG
# 00:22:34.345854 image saved       img12.JPG
# 00:22:34.365855 image read before img13.JPG
# 00:22:36.271853 image read after  img13.JPG
# 00:22:36.272854 image saved       img13.JPG
# 00:22:36.289854 image read before img14.JPG
# 00:22:37.656855 image read after  img14.JPG
# 00:22:37.657854 image saved       img14.JPG
# 00:22:37.676854 image read before img15.JPG
# 00:22:39.015853 image read after  img15.JPG
# 00:22:39.016854 image saved       img15.JPG
# 00:22:39.032853 image read before img16.JPG
# 00:22:40.619854 image read after  img16.JPG
# 00:22:40.620855 image saved       img16.JPG
# 00:22:40.636856 image read before img17.JPG
# 00:22:42.805854 image read after  img17.JPG
# 00:22:42.806853 image saved       img17.JPG
# 00:22:42.826856 image read before img18.JPG
# 00:22:44.873853 image read after  img18.JPG
# 00:22:44.875856 image saved       img18.JPG
# 00:22:44.900854 image read before img19.JPG
# 00:22:46.256853 image read after  img19.JPG
# 00:22:46.257855 image saved       img19.JPG
# 00:22:46.273854 image read before img20.JPG
# 00:22:47.599855 image read after  img20.JPG
# 00:22:47.600856 image saved       img20.JPG
# 00:22:47.621854 image read before img21.JPG
# 00:22:48.988854 image read after  img21.JPG
# 00:22:48.989856 image saved       img21.JPG
# 00:22:49.008854 image read before img22.JPG
# 00:22:50.360853 image read after  img22.JPG
# 00:22:50.361853 image saved       img22.JPG
# 00:22:50.377854 image read before img23.JPG
# 00:22:51.697855 image read after  img23.JPG
# 00:22:51.698855 image saved       img23.JPG
# 00:22:51.715853 image read before img24.JPG
# 00:22:52.889455 image read after  img24.JPG
# 00:22:52.889455 image saved       img24.JPG