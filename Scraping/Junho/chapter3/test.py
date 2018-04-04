

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

includeUrl = "https://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(includeUrl)
bsObj = BeautifulSoup(html, "html.parser")

internalLinks = []
includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
    if link.attrs["href"] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])          ### ?!?!??!
print(bsObj.find("a",href=re.compile("^(/|.*"+includeUrl+")")))




