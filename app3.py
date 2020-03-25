from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# beautifulsoup4とseleniumを使ったスクレイピングの練習
# 事前にPCにインストールされているChromeに対応したバージョンのChromeDriverをインストールしておく必要あり

def print_weather(source):
    # HTMLソースから天気の情報を取得
    soup = BeautifulSoup(source, 'html.parser')

    # 日付取得
    day = soup.find('span', class_ = 'current').text
    print('{0}'.format(day))

    # 地図内の地域を1つずつ取得
    results = []
    for li in soup.find_all('li', class_ = 'point'):
        # 地域名
        area = li.find('dt', class_ = 'name').text
        # 天気
        weather = li.find('p', class_ = 'icon').find('img').get('alt')
        # 最高気温
        high_temp = li.find('em', class_ = 'high').text
        # 最低気温
        low_temp = li.find('em', class_ = 'low').text
        # 降水確率
        rainy_percent = li.find('p', class_ = 'precip').text

        # 結果を出力
        print(area, weather, high_temp, low_temp, rainy_percent)

    print("\n")
    return


# Yahoo!天気・災害のページから現在日～8日後の全国の天気を取得
driver = webdriver.Chrome(executable_path = 'C:\\python\\chromedriver_win32\\chromedriver.exe')
driver.get('https://weather.yahoo.co.jp/weather/')

# ページを開いたときに表示されている現在日の天気情報を取得&格納
print_weather(driver.page_source)

# 地図上部に表示されている日付をクリックして別日の天気予報を取得していく
# 2～8日目のデータ天気を取得
# for element in driver.find_elements_by_css_selector('#navCal a'): ←修正前
for day in range(2, 9):
    element = driver.find_element_by_css_selector('#navCal > li:nth-child({0})'.format(day))
    element.click()

    # クリックした日付が青くなる(aタグが消えて、spanにcurrentというクラスが付く)まで待機してから天気情報を出力する処理を呼び出す
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#navCal > li:nth-child({0}) > span.current'.format(day))))
    print_weather(driver.page_source)

# ブラウザを閉じる
driver.close()


# 25(水)
# 札幌 晴れ 9 1 0%
# 釧路 晴れ 6 -2 0%
# 仙台 晴れ 12 2 0%
# 東京 晴時々曇 15 4 0%
# 名古屋 晴れ 17 3 0%
# 新潟 晴れ 11 4 0%
# 金沢 晴れ 11 3 0%
# 大阪 晴れ 16 5 0%
# 広島 晴れ 17 4 0%
# 高知 晴時々曇 17 5 10%
# 福岡 曇時々晴 20 6 0%
# 鹿児島 曇時々晴 22 9 0%
# 那覇 晴時々曇 25 18 0%
#
#
# 26(木)
# 札幌 晴時々曇 10 2 0%
# 釧路 晴れ 9 -1 0%
# 仙台 晴時々曇 18 3 0%
# 東京 晴れ 18 7 0%
# 名古屋 晴れ 21 5 0%
# 新潟 晴時々曇 16 2 0%
# 金沢 晴れ 19 4 0%
# 大阪 晴時々曇 20 6 10%
# 広島 晴のち雨 18 7 60%
# 高知 曇のち雨 19 9 50%
# 福岡 曇のち雨 21 12 100%
# 鹿児島 曇り 22 14 40%
# 那覇 曇時々晴 25 20 10%
#
#
# 27(金)
# 札幌 曇時々雨 11 2 70%
# 釧路 曇のち雨 8 -4 60%
# 仙台 晴のち曇 17 3 40%
# 東京 曇時々晴 20 8 20%
# 名古屋 雨時々曇 18 10 90%
# 新潟 曇のち雨 19 6 100%
# 金沢 曇のち雨 20 9 100%
# 大阪 曇時々雨 21 13 80%
# 広島 大雨 18 14 100%
# 高知 雨 20 14 90%
# 福岡 雨 22 15 100%
# 鹿児島 雨時々曇 22 18 90%
# 那覇 曇り 26 21 10%
#
#
# 28(土)
# 札幌 曇時々晴 6 0 20%
# 釧路 曇時々晴 8 -1 10%
# 仙台 曇一時雨 14 3 50%
# 東京 雨時々曇 19 6 90%
# 名古屋 雨時々曇 19 9 100%
# 新潟 曇一時雨 11 4 100%
# 金沢 曇時々雨 13 5 100%
# 大阪 曇時々雨 17 6 90%
# 広島 曇一時雨 18 8 70%
# 高知 雨時々曇 20 9 90%
# 福岡 曇一時雨 16 8 80%
# 鹿児島 曇時々雨 19 13 90%
# 那覇 曇時々雨 25 19 70%
#
#
# 29(日)
# 札幌 晴れ 11 0 10%
# 釧路 晴れ 7 -1 0%
# 仙台 晴時々曇 12 1 20%
# 東京 曇一時雨 14 4 80%
# 名古屋 晴一時雨 18 7 50%
# 新潟 晴時々曇 12 3 20%
# 金沢 晴時々曇 13 5 40%
# 大阪 晴時々曇 18 6 30%
# 広島 晴時々曇 18 7 10%
# 高知 曇時々晴 19 8 20%
# 福岡 曇時々晴 18 7 20%
# 鹿児島 曇り 19 11 20%
# 那覇 曇り 24 19 20%
#
#
# 30(月)
# 札幌 晴れ 14 3 0%
# 釧路 晴時々曇 9 -1 0%
# 仙台 曇時々晴 13 2 30%
# 東京 曇一時雨 15 7 50%
# 名古屋 曇時々雨 17 10 80%
# 新潟 曇時々晴 17 4 20%
# 金沢 曇一時雨 15 6 70%
# 大阪 曇一時雨 17 9 80%
# 広島 曇時々雨 15 9 90%
# 高知 曇時々雨 18 10 90%
# 福岡 雨時々曇 15 10 90%
# 鹿児島 曇時々雨 20 14 90%
# 那覇 曇一時雨 26 20 60%
#
#
# 31(火)
# 札幌 晴時々曇 14 2 10%
# 釧路 曇り 10 1 10%
# 仙台 曇一時雨 13 6 70%
# 東京 曇時々雨 16 8 80%
# 名古屋 曇時々雨 19 11 80%
# 新潟 曇一時雨 16 8 60%
# 金沢 曇時々雨 15 10 80%
# 大阪 曇時々雨 19 12 70%
# 広島 曇一時雨 19 12 50%
# 高知 曇一時雨 21 14 60%
# 福岡 曇一時雨 18 12 60%
# 鹿児島 曇一時雨 21 15 60%
# 那覇 曇時々雨 25 20 60%
#
#
# 4/1(水)
# 札幌 曇時々晴 13 4 20%
# 釧路 曇り 10 1 30%
# 仙台 曇一時雨 15 7 50%
# 東京 曇一時雨 19 11 50%
# 名古屋 曇一時雨 20 12 60%
# 新潟 曇一時雨 16 9 60%
# 金沢 曇時々雨 16 10 70%
# 大阪 曇り 19 11 40%
# 広島 曇り 20 11 20%
# 高知 曇り 21 12 30%
# 福岡 曇り 18 11 40%
# 鹿児島 曇り 20 14 40%
# 那覇 曇一時雨 24 19 60%