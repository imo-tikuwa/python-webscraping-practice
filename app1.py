from urllib import request
from bs4 import BeautifulSoup

# beautifulsoup4を使ったスクレイピングの練習

# Yahoo!天気・災害のページから今日の全国の天気を取得
response = request.urlopen('https://weather.yahoo.co.jp/weather/')
soup = BeautifulSoup(response, 'html.parser')
response.close()

# 地図内の地域を1つずつ取得
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


# 札幌 曇り 6 1 50%
# 釧路 曇り 8 0 50%
# 仙台 曇時々晴 11 4 0%
# 東京 曇り 15 8 20%
# 名古屋 曇時々晴 17 8 0%
# 新潟 雨 10 3 80%
# 金沢 曇り 13 5 40%
# 大阪 曇時々晴 17 9 0%
# 広島 晴れ 20 8 0%
# 高知 晴れ 20 10 0%
# 福岡 晴れ 17 11 0%
# 鹿児島 晴れ 23 12 0%
# 那覇 晴れ 24 19 0%