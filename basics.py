# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:20:28 2023

@author: patry
"""



# class(zolta czcionka), id ? to jest atrybut
# div to jest tag, czyli to co jest na poczatku linijki np. body, header, div

import requests
from bs4 import BeautifulSoup 

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

page = requests.get(url)

soup = BeautifulSoup(page.text,"lxml")

soup


# Funkcja find zwraca tylko pierwsze wystapienie danego elementu
# find 
soup.find("header")

soup.header.attrs

a = soup.find("div",{"class":"container test-site"})

# to samo znaczace polecenie

b = soup.find("div",class_ = "container test-site")

if a == b:
    print("Approve")
else:
    print("Not approve")
    

cipek = soup.find("h1",{"class":"page-header"}).text
cipek


########################### find_all function 


prices = soup.find_all("h4",{"class":"pull-right price"})
prices[6:]

oceny = soup.find_all("p",{"data-rating":3})
type(oceny)


soup.find_all(["p","h4"])

soup.find_all(id = True)

soup.find_all(string = "Iphone")


import re

# znajdowanie calego teksut wykorzystujac jego kawalek 
soup.find_all(string = re.compile("Nok"))


# Ciekawe polecenie re.compile 
dupa = soup.find_all("p",{"class": re.compile("pull")})[:3]
dupa[0].text


# Find_all part 3 

products_names = soup.find_all("a",{"class":"title"})
products_names

prices = soup.find_all("h4",{"class":"pull-right price"})
prices


reviews = soup.find_all("p",{"class":"pull-right"})
reviews

# To samo z wykorzystaniem funkcji re.compile 
reviews = soup.find_all("p",{"class": re.compile("pull")})
reviews


description = soup.find_all("p",{"class": re.compile("description")})
description


product_name_list = []
for i in products_names:
    a = i.text
    product_name_list.append(a)


product_prices_list = []
for i in prices:
    a = i.text
    product_prices_list.append(a)


prices_list = []
for i in prices:
    a = i.text
    prices_list.append(a)


review_list = []
for i in reviews:
    a = i.text
    review_list.append(a)


description_list = []
for i in description:
    a = i.text
    description_list.append(a)

import pandas as pd


table = pd.DataFrame({"Product Name":product_name_list,"Description":description_list, "Price":prices_list, "Reviews":review_list})
table


# Extracting data from nested HTML tags

# Wyciagniecie danych z jednego konkretnego "boxa"

boxes = soup.find_all("div",{"class": re.compile("col-sm-4 col-lg-4 col-md-4")})[0]
boxes
len(boxes)


box = soup.find_all("ul",{"class":"nav","id":"side-menu"})[0]

# len(box)
box.find_all("a",{"class":"category-link"})[0].text





########## CODING EXERCISE APPLE SCRAPE


url = "https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol"


page = requests.get(url)
page

soup = BeautifulSoup(page.text,"lxml")

div_main_price = soup.find_all("div",{"class":"intraday__data"})[0]
div_main_price

main_price = div_main_price.find_all("h2")[0].text
main_price


table_closing_price = soup.find_all("tbody",{"class": re.compile("remove-last-border")})[0]
table_closing_price

closing_price = table_closing_price.find_all("td",{"class": re.compile("table__cell u-semi")})[0]
closing_price.text


range_week = soup.find_all("div",{"class":re.compile("range__header")})[2]
min_price = range_week.find_all("span",{"class":re.compile("primary")})[0]
min_price.text


max_price = range_week.find_all("span",{"class":re.compile("primary")})[1]
max_price.text


analyst_rating = soup.find_all("div",{"class":re.compile("analyst__chart")})[0]
len(analyst_rating)

analyst_rating

avg = analyst_rating.find_all("li",{"class":re.compile("analyst__option active")})[0]
avg.text

















