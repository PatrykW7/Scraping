# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:45:36 2023

@author: patry
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
driver.get("https://store.unionlosangeles.com/collections/headwear?sort_by=creation_date")

# scrollowanie na sam koniec strony, z mozliwoscia scrollowania do gory po wykonaniu sie petli 
last_height = driver.execute_script('return document.body.scrollHeight')

soup = BeautifulSoup(driver.page_source, "lxml")

iterator = 0
# Petla odpowiadajaca za przeskakiwanie stron
link = "https://store.unionlosangeles.com/"

df = None
df = pd.DataFrame({"Link":[], "Name": [], "Price": [], "Company": []})

#while iterator <= 2:
for i in range(1,3):
    # Petla odpowiadajaca za scrollowanie w dol
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height
    boxes = soup.find_all("li",class_ = "isp_grid_product")
    time.sleep(1)
    
    
    
    for box in boxes:
        try:
            name = box.find("div",class_ = "isp_product_title").text
            price = box.find("div", class_ = "isp_product_price_wrapper").text
            part_link = box.find("a", class_ = "isp_product_image_href").get("href")
            full_link = link + part_link
            company = box.find("div", class_ = "isp_product_vendor").text
            df = df.append({"Link":full_link, "Name": name, "Price": price, "Company": company}, ignore_index = True)
        except:
            pass
    
    
    df.to_csv(f"C:\\Scraping\\union.csv")
    #new_page = driver.find_element('xpath','//*[@id="isp_pagination_anchor"]/ul/li[4]/a').click()
    driver.get(f"https://store.unionlosangeles.com/collections/headwear?sort_by=creation_date&page_num={i+1}")
    soup = BeautifulSoup(driver.page_source, "lxml")
   
    #iterator +=1

df = df.drop_duplicates()

if "FREE WHEELIN' TRUCKER CAP" in df["Name"].values:
    print("Koniec")
else:
    print("Continuing")
