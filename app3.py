from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
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
for element in driver.find_elements_by_css_selector('#navCal a'):
    # TODO 日付をクリックした先がよくわからない
    element.click()
#     print_weather(driver.page_source)

# ブラウザを閉じる
driver.close()
