from bs4 import BeautifulSoup
import requests
r = requests.get('file:///C:/Users/aycan/Desktop/Kartlar.html')
source = BeautifulSoup(r.content,'lxml')
word= source.find_all('a', class_='SetPageTerm-wordText')
# all_itemWord=word.find_all('span' , {'class':'TermText'})
defination= source.find('a' , {'class':'SetPageTerm-wordText'})
# all_itemDef=defination.find_all('span' , {'class':'TermText'})


# for i in all_itemWord:
# 	for x in all_itemDef:
# 		print all_itemDef,all_itemWord
print word, defination