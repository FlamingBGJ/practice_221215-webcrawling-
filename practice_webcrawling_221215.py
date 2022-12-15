# 크롬 드라이버 활용
from selenium import webdriver
import time

# webdriver 객체  생성
driver = webdriver.Chrome("./chromedriver.exe")
naver_url = "https://www.naver.com"

driver.get(naver_url)

time.sleep(10)
driver.close()

# 웹드라이버를 사용한 크롤링
from bs4 import BeautifulSoup as BS
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver.exe")
naver_url = "https://www.naver.com"

driver.get(naver_url)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"input#query").send_keys("부산국밥집")
driver.find_element(By.CSS_SELECTOR,"button#search_btn").click()
time.sleep(1)
html= driver.page_source
soup = BS(html,"html.parser")
driver.close() 

#네이버에서 부산국밥집을 검색한 결과를 가게 이름과 링크를 함께 df에 저장하세요
find_eats = soup.find_all("div",{"class":"CHC5F"})
post_list = []
for i in find_eats:
    name = i.find("span").text
    link = i.find("a")["href"]
    post_list.append({"상호":name,"위치":link})
df = pd.DataFrame(post_list)
print(df)

# 파파고
driver = webdriver.Chrome("./chromedriver.exe")
papago_url = "https://papago.naver.com/"
driver.get(papago_url)
time.sleep(3)

user_input = input("번역할 단어를 입력해주세요 : ")

driver.find_element(By.CSS_SELECTOR,"textarea#txtSource").send_keys(f"{user_input}")
driver.find_element(By.CSS_SELECTOR,"button#btnTranslate").click()
time.sleep(1)
html= driver.page_source
soup = BS(html,"html.parser")

ts = soup.find("div",id="txtTarget").text
#ts = soup.find_element(BY.CSS_SELECTER,"div#txtTarget").text
print(ts)

driver.close()
