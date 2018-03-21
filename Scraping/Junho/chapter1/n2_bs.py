from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#print(html.read())
#print(html.read())   # once read, then empty the html... !!!!
bsObj = BeautifulSoup(html.read(), "html.parser"); 
print(bsObj.html)
print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.html.h1)
print(bsObj.body.h1)

