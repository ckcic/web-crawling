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
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

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


# 투니버스
tooniverse_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "https://tooniverse.cjenm.com/ko/schedule/"
tooniverse_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
tooniverse_driver.implicitly_wait(10)

element = tooniverse_driver.find_element(By.XPATH, '//*[@id="contents"]/section[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/ul[4]')
tooniverse = element.find_elements(By.CLASS_NAME, "inner")

program_timelist = []
program_titlelist = []
film_ratinglist = []

for program in tooniverse:
    program_time = program.find_element(By.CLASS_NAME, "p_time").text
    program_title = program.find_element(By.CLASS_NAME, "p_name").text
    film_rating = program.find_element(By.CLASS_NAME, "age").text
    
    program_timelist.append(program_time)
    program_titlelist.append(program_title)
    film_ratinglist.append(film_rating)

tooniverse_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist, "등급":film_ratinglist}
df = pd.DataFrame(data)
# print(df.head(len(tooniverse)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("tooniverse "+ file_date +".csv", encoding = "utf-8-sig")


# 카툰네트워크
cartoonnetwork_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "https://main.cartoonnetworkkorea.com/program/schedule.php"
cartoonnetwork_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
cartoonnetwork_driver.implicitly_wait(10)

element = cartoonnetwork_driver.find_element(By.CSS_SELECTOR, 'body > table:nth-child(8) > tbody > tr > td:nth-child(2) > table > tbody > tr > td:nth-child(2) > table:nth-child(2) > tbody > tr > td:nth-child(3) > table:nth-child(2) > tbody > tr > td > table > tbody > tr > td > table:nth-child(5) > tbody > tr > td')
cartoonnetwork = element.find_elements(By.TAG_NAME, "table")

program_timelist = []
program_titlelist = []

cartoonnetwork_count = 0

for program in cartoonnetwork:
    program_time = program.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1)").text.split('\n')[0]
    program_title = program.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td:nth-child(2)").text.split('\n')[0]
    if(cartoonnetwork_count == 0):
        program_timelist.append(program_time)
        program_titlelist.append(program_title)
        cartoonnetwork_count += 1
    elif(cartoonnetwork_count == 2):
        cartoonnetwork_count = 0
    else:
        cartoonnetwork_count += 1

cartoonnetwork_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist}
df = pd.DataFrame(data)
# print(df.head(len(cartoonnetwork)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("cartoonnetwork "+ file_date +".csv", encoding = "utf-8-sig")


# sbs kizmom , 니켈로디언
kizmom_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "https://sbsmedianet.sbs.co.kr/schedule.html?channel=Nick"
kizmom_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
kizmom_driver.implicitly_wait(10)

element = kizmom_driver.find_element(By.XPATH, '//*[@id="sbs-scheduler-schedulerList-self"]')
kizmom = element.find_elements(By.CLASS_NAME, "schedule_program_w")

program_timelist = []
program_titlelist = []

for program in kizmom:
    program_time = program.find_element(By.CLASS_NAME, "spt_hours").text
    program_title = program.find_element(By.CLASS_NAME, "spi_title").text
    
    program_timelist.append(program_time)
    program_titlelist.append(program_title)


kizmom_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist}
df = pd.DataFrame(data)
# print(df.head(len(kizmom)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("kizmom "+ file_date +".csv", encoding = "utf-8-sig")


# EBSKIDS
EBSU_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "https://www.ebs.co.kr/schedule?channelCd=EBSU&onor=EBSU"
EBSU_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
EBSU_driver.implicitly_wait(10)

element = EBSU_driver.find_element(By.CLASS_NAME, 'main_timeline')
EBSU = element.find_elements(By.TAG_NAME, "li")

program_timelist = []
program_titlelist = []

for program in EBSU:
    program_time = program.find_element(By.CSS_SELECTOR, "div.time > span").text
    program_title = program.find_element(By.CSS_SELECTOR, "div.tit > p > strong").text
    
    program_timelist.append(program_time)
    program_titlelist.append(program_title)


EBSU_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist}
df = pd.DataFrame(data)
# print(df.head(len(EBSU)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("EBSU "+ file_date +".csv", encoding = "utf-8-sig")


# 챔프TV
champtv_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = "https://www.champtv.com/schedule/daily/daily.asp"
champtv_driver.get(url)

# 페이지 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
champtv_driver.implicitly_wait(10)

element = champtv_driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/article/table/tbody')
champtv = element.find_elements(By.TAG_NAME, "tr")

program_timelist = []
program_titlelist = []

for program in champtv:
    program_time = program.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
    program_title = program.find_element(By.TAG_NAME, "a").text
    
    program_timelist.append(program_time)
    program_titlelist.append(program_title)


champtv_driver.quit()

# dataframe으로 변환
data = {"방송시간" : program_timelist,"프로그램 정보":program_titlelist}
df = pd.DataFrame(data)
# print(df.head(len(champtv)))

# dataframe을 csv파일로 내보내기
file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_csv("champtv "+ file_date +".csv", encoding = "utf-8-sig")
