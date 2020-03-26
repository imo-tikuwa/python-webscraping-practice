from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 練習として使うことを許可しているサイトでログインを行った先のページの情報を取得する
# 練習サイト
# Webスクレイピング入門者のためのサイト
# https://scraping-for-beginner.herokuapp.com/
#
# ログインアカウントは以下のページより imanishi / kohei であることを確認
# https://scraping-for-beginner.readthedocs.io/ja/latest/src/1.html#%E8%87%AA%E5%8B%95%E3%81%A7%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3

LOGIN_URL = 'https://scraping-for-beginner.herokuapp.com/login_page'
USERNAME = 'imanishi'
PASSOWRD = 'kohei'

# ログイン画面を開く
driver = webdriver.Chrome(executable_path = 'C:\\python\\chromedriver_win32\\chromedriver.exe')
driver.get(LOGIN_URL)

# input要素取得
input_username = driver.find_element_by_css_selector('#username')
input_password = driver.find_element_by_css_selector('#password')

# input要素に入力
input_username.send_keys(USERNAME)
input_password.send_keys(PASSOWRD)

# ログインボタンクリック
driver.find_element_by_css_selector('#login-btn').click()


# ログイン後画面が表示されるまで待機（ログイン後画面の最後の取得する要素を指定）
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#hobby')))

# ログイン後画面のURLを出力
print('ログイン後画面のURL：{0}'.format(driver.current_url))

# ログイン後画面の情報を取得
table_element = driver.find_element_by_tag_name('table')
th_elements = table_element.find_elements_by_tag_name('th')
td_elements = table_element.find_elements_by_tag_name('td')

# 項目名と値を出力（改行がある場合は読点に置換して表示）
for index, th_element in enumerate(th_elements):
    td_element = td_elements[index]
    td_text = td_element.text
    if '\n' in td_text:
        td_text = td_text.replace('\n', '、')
    print('{0}：{1}'.format(th_element.text, td_text))

# ブラウザを閉じる
driver.close()


# ログイン後画面のURL：https://scraping-for-beginner.herokuapp.com/mypage
# 講師名：今西 航平
# 所属企業：株式会社キカガク
# 生年月日：1994年7月15日
# 出身：千葉県
# 趣味：バスケットボール、読書、ガジェット集め