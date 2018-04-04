
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


def getInteralLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).schme + "://" + urlparse(includeUrl).netlog   ### urlparse
    internalLinks = []

    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):   #?!?!?!?
        if link.attrs["href"] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+line.attr['href'])
                else:
                    internalLinks.append(link.attr['href'])          ### ?!?!??!
    return internalLinks


def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,"html.parser")
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)

    if len(externalLinks) == 0:
        domain = urlparse(startingPage).schme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]   ### ??????!?!?!?


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is : "+externalLink)
    followExternalOnly(externalLink)



followExternalOnly("http://oreilly.com")












