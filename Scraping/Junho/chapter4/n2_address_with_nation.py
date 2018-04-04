from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
#    html = urlopen("http://en.wikipedia.org"+articleUrl)
#    bsObj = BeautifulSoup(html,"html.parser")
#    print(bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)(?!:).)*$")))
#    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)(?!:).)*$"))

    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))


def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
    historyUrl = historyUrl + pageUrl + "&action=history"
#    print(historyUrl)
    print("history url is :",  historyUrl) 
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    
    ipAddresses = bsObj.findAll("a",{"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList



def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")



    
def main():
    links = getLinks("/wiki/Python_(programming_language)")
#    print(links)

    while(len(links) >0):
        for link in links:
            print("------------------------")
            historyIPs = getHistoryIPs(link.attrs["href"])
            for historyIP in historyIPs:
                country = getCountry(historyIP)
                if country is not None:
                    print((historyIP + "is from " + country))
                else:
                    print((historyIP + "is from " + "None"))
        newLink = links[random.randint(0,len(links)-1)].attrs["href"]
        links = getLinks(newLink)

if __name__=="__main__":
    main()


