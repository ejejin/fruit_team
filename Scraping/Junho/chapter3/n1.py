from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.findAll("a"):   # findAll("a") means find all of the link 
    if 'href' in link.attrs:      # if the tag "a"'s attribute is 'href', ...
        print(link.attrs['href'])

