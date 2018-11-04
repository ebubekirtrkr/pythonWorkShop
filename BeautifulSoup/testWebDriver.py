from bs4 import BeautifulSoup
import requests
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.vivense.com/oturma-odasi-mobilyalari.html')
res = driver.execute_script("return document.documentElement.outerHTML")

soup= BeautifulSoup(res,'lxml')
box= soup.find('div' , {'class':'product-carousel'})
all_aaa=box.find_all('div' , {'class':'product-content'})
for a in all_aaa:
	a_name=a.find('div' , {'class':'product-item-name'}).text

	print(a_name)