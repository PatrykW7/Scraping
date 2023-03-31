# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:31:50 2023

@author: patry
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
driver.get("https://www.google.com/")
driver.find_element('xpath','//*[@id="L2AGLb"]/div').click()
box = driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys("top 100 movies of all time")
box.send_keys(Keys.ENTER)


driver.find_element('xpath','//*[@id="rso"]/div[2]/div/div/div[1]/div/a/h3').click()

# Waiting time
element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[4]/div[3]/div[50]/div[2]/h3/a')))



#for i in range(1,51):
    #box = driver.find_element('xpath',f'//*[@id="main"]/div/div[4]/div[3]/div[{i}]')
    #tekst = box.find_element('xpath',f'//*[@id="main"]/div/div[4]/div[3]/div[{i}]/div[2]/h3/a').text
    #print(tekst)
    
jaws = driver.find_element('xpath','//*[@id="main"]/div/div[4]/div[3]/div[50]')

# Scrolluje do elemenetu w ktorym wystapi element jaws
driver.execute_script("arguments[0].scrollIntoView();",jaws)
driver.find_element('xpath','//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot(r'C:\\Scraping\\jaws.png')
driver.find_element('xpath','//*[@id="wrapper"]').screenshot(r'C:\\Scraping\\jaws_website.png')

