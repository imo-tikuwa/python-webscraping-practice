from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# 練習として使うことを許可しているサイトで一覧表示されてるページの情報を取得する
# 練習サイト
# Webスクレイピング入門者のためのサイト
# https://scraping-for-beginner.herokuapp.com/


# ランキング画面を開く
driver = webdriver.Chrome(executable_path = 'C:\\python\\chromedriver_win32\\chromedriver.exe')
driver.get('https://scraping-for-beginner.herokuapp.com/ranking/')

# 一つ前のページのURLを格納しとく変数
prev_url = None

# 結果を保存する配列
results = []

while (True):

    # ページ末尾のページャー要素が見つかるまで待機
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pagination')))

    # 1つ前の画面とURLが一緒のとき終了
    if (prev_url is not None and prev_url == driver.current_url):
        print("一つ前のURLと現在のURLが一致してしまってるのでループを抜けます")
        break

    # 現在のページのランキングを出力する。うまく取得できなかったときは処理を抜ける
    ranking_elements = driver.find_elements_by_css_selector('.u_areaListRankingBox')
    if (len(ranking_elements) == 0):
        break

    for index, ranking_element in enumerate(ranking_elements):
        rank_and_title = ranking_element.find_element_by_class_name('u_title').text
        rank_and_title = rank_and_title.split('\n')

        # 順位
        rank = rank_and_title[0]
#         print("順位：{0}".format(str(rank).rjust(2, ' ')))

        # タイトル
        title = rank_and_title[1]
#         print("タイトル：{0}".format(title))

        # レート(平均)
        rate_average = ranking_element.find_element_by_css_selector('.u_rankBox > .evaluateNumber').text
#         print("レート(平均)：{0}".format(rate_average))

        # レート(楽しさ～アクセス)
        rate_elements = ranking_element.find_elements_by_css_selector('.u_categoryTipsItem > dl')
        rate_amusement = rate_crowded = rate_view = rate_access = 0
        for index, rate_element in enumerate(rate_elements):
            rate = rate_element.find_element_by_class_name('is_rank').text
            if (index == 0):
                rate_amusement = rate
#                 print("レート(楽しさ)：{0}".format(rate_amusement))
            elif(index == 1):
                rate_crowded = rate
#                 print("レート(人混みの多さ)：{0}".format(rate_crowded))
            elif(index == 2):
                rate_view = rate
#                 print("レート(景色)：{0}".format(rate_view))
            elif(index == 3):
                rate_access = rate
#                 print("レート(アクセス)：{0}".format(rate_access))

        # 配列に保存
        results.append([rank, title, rate_average, rate_amusement, rate_crowded, rate_view, rate_access])


    # 次のページが存在するかチェックする。存在しないときループを抜けて処理を終了する
    # 次のページを表示する > ボタンを包むli要素を取得
    pager_next_btn_element = driver.find_element_by_xpath("//ul[@class='pagination']/li[last()]")

    # 現在のページのボタンを番号を取得
    active_page_num = driver.find_element_by_xpath("//ul[@class='pagination']/li[@class='active']").text

    # 次ページが存在しないときに付与されているクラス disabled がli要素についてたら処理を終了
    if 'disabled' in pager_next_btn_element.get_attribute('class'):
#         print("次のページは存在しないのでループを抜けます。現在のページ番号：{0}".format(active_page_num))
        break

    # 次のページ番号を元にXPathでクリックしたいaタグを取得
    next_page_num = int(active_page_num) + 1
    next_page_btn = driver.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '{0}')]".format(next_page_num))
    if (next_page_btn is not None):
        prev_url = driver.current_url
        next_page_btn.click()


# ブラウザを閉じる
driver.close()

# 結果をCSV出力
if (len(results) > 0):
    # CSVヘッダ
    results.insert(0, ["順位", "タイトル", "レート(平均)", "レート(楽しさ)", "レート(人混みの多さ)", "レート(景色)", "レート(アクセス)"])

    # CSV出力
    with open("ranking.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(results)


# 順位,タイトル,レート(平均),レート(楽しさ),レート(人混みの多さ),レート(景色),レート(アクセス)
# 1,観光地 1,4.7,4.6,4.5,4.9,4.2
# 2,観光地 2,4.7,4.6,4.5,4.9,4.2
# 3,観光地 3,4.6,4.5,4.4,4.8,4.1
# 4,観光地 4,4.5,4.4,4.4,4.8,4.0
# 5,観光地 5,4.5,4.4,4.3,4.7,4.0
# 6,観光地 6,4.4,4.3,4.3,4.7,3.9
# 7,観光地 7,4.3,4.2,4.2,4.6,3.8
# 8,観光地 8,4.3,4.2,4.2,4.6,3.8
# 9,観光地 9,4.2,4.1,4.1,4.5,3.7
# 10,観光地 10,4.1,4.0,4.1,4.4,3.6
# 11,観光地 11,4.1,4.0,4.0,4.4,3.6
# 12,観光地 12,4.0,3.9,4.0,4.3,3.5
# 13,観光地 13,3.9,3.8,3.9,4.3,3.4
# 14,観光地 14,3.9,3.8,3.9,4.2,3.4
# 15,観光地 15,3.8,3.7,3.8,4.2,3.3
# 16,観光地 16,3.7,3.6,3.8,4.1,3.2
# 17,観光地 17,3.7,3.6,3.7,4.1,3.2
# 18,観光地 18,3.6,3.5,3.7,4.0,3.1
# 19,観光地 19,3.5,3.4,3.6,3.9,3.0
# 20,観光地 20,3.5,3.4,3.6,3.9,3.0
# 21,観光地 21,3.4,3.3,3.5,3.8,2.9
# 22,観光地 22,3.3,3.2,3.5,3.8,2.8
# 23,観光地 23,3.3,3.2,3.4,3.7,2.8
# 24,観光地 24,3.2,3.1,3.4,3.7,2.7
# 25,観光地 25,3.1,3.0,3.3,3.6,2.6
# 26,観光地 26,3.1,3.0,3.3,3.6,2.6
# 27,観光地 27,3.0,2.9,3.2,3.5,2.5
# 28,観光地 28,2.9,2.8,3.2,3.4,2.4
# 29,観光地 29,2.9,2.8,3.1,3.4,2.4
# 30,観光地 30,2.8,2.7,3.1,3.3,2.3