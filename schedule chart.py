from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지
chrome_options.add_argument('headless') # 브라우저가 뜨지 않고 실행됩니다. 
# headless 탐지를 피하기 위해 user-agent변경필요
# https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html
# 위 링크에서 user-agent 확인
chrome_options.add_argument('window-size=1920x1080') # 화면 조정
chrome_options.add_argument('disable-gpu') # 하드웨어 가속 안함
# chrome_options.add_argument('lang=ko_KR') # 사용언어 한국어

# UserAgent값을 바꿔줍시다!
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# 방송국이름_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# 드라이버는 방송국 마다 생성해야함

# 재능TV
jeitv_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "https://www.jeitv.com/bbs/board.php?bo_table=every"
jeitv_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
jeitv_driver.implicitly_wait(10)

element = jeitv_driver.find_element(By.TAG_NAME, "tbody")
jeitv = element.find_elements(By.TAG_NAME, "tr")

program_timelist = []
program_titlelist = []
film_ratinglist = []

for i in jeitv:
    program = i.find_elements(By.TAG_NAME, "td")
    program_time = program[0].text
    program_title = program[1].text
    film_rating = program[2].text

    program_timelist.append(program_time)
    program_titlelist.append(program_title)
    film_ratinglist.append(film_rating)

jeitv_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist, "등급":film_ratinglist}
df = pd.DataFrame(data)
# print(df.head(len(jeitv)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("jeitv "+ file_date +".csv", encoding = "utf-8-sig")


# KBS 키즈
kbsn_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "http://www.kbsn.co.kr/schedule/index?dt=&ch=KIDS"
kbsn_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
kbsn_driver.implicitly_wait(10)

element = kbsn_driver.find_element(By.CLASS_NAME, "schedule_list")
kbsn = element.find_elements(By.TAG_NAME, "li")

program_timelist = []
program_titlelist = []

for program in kbsn:
    program_time = program.find_element(By.CLASS_NAME, "time").text
    program_title = program.find_element(By.CLASS_NAME, "title").text.replace("\n", " ")

    program_timelist.append(program_time)
    program_titlelist.append(program_title)

kbsn_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist}
df = pd.DataFrame(data)
# print(df.head(len(kbsn)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("kbsn "+ file_date +".csv", encoding = "utf-8-sig")