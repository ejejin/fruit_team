from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    try:
        print("1",bsObj.h1.get_text())
        print("2",bsObj.find(id = "mw-content-text").findAll("p")[0])
        print("3",bsObj.find(id = "ca-edit").find("span").find("a").attr['href'])    # it is said that this is edit link
    except AttributeError:
        print("this page is missing somthing!")
#    except TypeError:
#        print("This is type error")
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("------------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
        



def main():
    try :
        getLinks("")
    except TypeError:
        print(pages)
#    print("2000")
#    print(pages)

if __name__=="__main__":
    main()





