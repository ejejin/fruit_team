from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html,"html.parser")
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
#                        href="/wiki/Footloose_(1984_film)"):
                       href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

#print("!!!!!!!",bsObj.find("div",{"id":"bodyContent"}).findAll("a",
#                      href=re.compile("^(/wiki/)((?!:).)*$")))
