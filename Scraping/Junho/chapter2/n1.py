from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span",{"class":"green"})   ##findAll(tag, attributes, recursive, text, limit, keywords)
#nameList = bsObj.findAll("span")
#nameList = bsObj.findAll({"h1","h2","h3","h4"})
#nameList = bsObj.findAll("span",{"class":{"green","red"}})

allText = bsObj.findAll(id="text")   # "text"
#print(allText)
#print(allText[0])
#print(allText[0].get_text())

#print(type(nameList))   # <class 'bs4.element.ResultSet'>  # for me it seems like a list of python
#print(nameList)

for name in nameList:
    print(name.get_text())




