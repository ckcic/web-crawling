from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지
# chrome_options.add_argument('headless') # 브라우저가 뜨지 않고 실행됩니다. 
# headless 탐지를 피하기 위해 user-agent변경필요
# https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html
# 위 링크에서 user-agent 확인
chrome_options.add_argument('window-size=1920x1080') # 화면 조정
chrome_options.add_argument('disable-gpu') # 하드웨어 가속 안함
chrome_options.add_argument('lang=ja') # 사용언어
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# UserAgent값을 바꿔줍시다!
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = "https://www.google.com//imghp"
driver.get(url)

# driver.quit()