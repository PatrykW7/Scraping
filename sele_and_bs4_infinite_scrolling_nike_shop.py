# Combination of BeautifulSoup and Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
driver.get('https://www.nike.com/pl/w/mezczyzni-buty-nik1zy7ok')

driver.find_element('xpath','//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[2]/div[2]/button').click()

last_height = driver.execute_script('return document.body.scrollHeight')
# nieskonczone scrollowanie
# po skonczeniu mozna samemu scrollowac do gory ! 

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break 
    last_height = new_height


# Wykorzystanie BeautifulSoup z Selenium

df = None
df = pd.DataFrame({"Link": [], "Name":[], "Description":[] ,"Price":[]})

soup = BeautifulSoup(driver.page_source,"lxml")

boxes = soup.find_all("div", class_= "product-card__body")

for box in boxes:
    try:
        link = box.find("a",class_ = "product-card__link-overlay").get("href")
        name = box.find("div",class_ = "product-card__title").text
        price = box.find("div",class_ = "product-card__price").text
        #full_price = box.find_all("div",{"class":"product-price css-1h0t5hy"})
        Description = box.find("div",class_ = "product-card__subtitle").text
        df = df.append({"Link":link,"Name":name, "Description":Description ,"Price":price},ignore_index = True)
    except:
        pass
df.to_csv(f"C:\\Scraping\\nike.csv")



