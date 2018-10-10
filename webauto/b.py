from bs4 import BeautifulSoup
import requests
r = requests.get('https://www.vivense.com/oturma-odasi-mobilyalari.html')
source = BeautifulSoup(r.content,'lxml')
box= source.find('div' , {'class':'product-carousel'})
all_item=box.find_all('div' , {'class':'product-content'})
for i in all_item:
	i_name=i.find('div' , {'class':'product-item-name'}).text
	print(i_name)