import argparse
import os
import signal
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime # yyyymmddHHMMSS のタイムスタンプをファイルに付ける
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser(description='Log in to Rakuten.')
parser.add_argument('-u', '--user-id', type=str, required=True, dest='user_id', help='Specify your login ID')
parser.add_argument('-p', '--password', type=str, required=True, dest='password', help='Specify your password')

current_time = datetime.datetime.today()
current_time_str = current_time.strftime("%Y%m%d%H%M%S")
dir_name = f'screenshots/{current_time_str}'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage') # メモリ不足の回避

driver = webdriver.Chrome(options=options)
print('開始します')

try:
    args = parser.parse_args()

    # 楽天ログインページに移動
    url = "https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top"
    driver.get(url)
    driver.save_screenshot(f'{dir_name}_log_in.png')
    print("ログインページ表示")
    driver.implicitly_wait(2)

    # 楽天にログイン
    elem_search_word = driver.find_element_by_id("loginInner_u")
    elem_search_word.send_keys(args.user_id) # USER ID
    elem_search_word = driver.find_element_by_id("loginInner_p")
    elem_search_word.send_keys(args.password) # USER PASSWORD
    driver.save_screenshot(f'{dir_name}_logging_in.png')
    print("ログイン中")

    # ログインボタンをクリック
    driver.find_element_by_css_selector('input[type="submit"][class="loginButton"]').click()

    wait = WebDriverWait(driver, 10)
    # ログイン後の検索フォームが表示されているかチェック
    element = wait.until(EC.element_to_be_clickable((By.ID, 'sitem')))

    driver.save_screenshot(f'{dir_name}_logged_in.png')
    print("ログインしました")

except Exception as e:
    print(e)

finally:
    print('終了しました')

    driver.stop_client()
    driver.close()
    driver.quit()
