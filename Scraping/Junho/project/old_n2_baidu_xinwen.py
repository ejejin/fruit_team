from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import numpy
from time import sleep
#random.seed(datetime.datetime.now())

def naver(duration=3,time=3):

    DIC = dict()
    #html = "https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-04-04T18:20:00"
#    html = "http://news.baidu.com/"
#    HTML = urlopen(html)
#    bsObj = BeautifulSoup(HTML, "html.parser")
    #print(bsObj)

#    TEST = bsObj.find("ul",{"class":"ah_l"}).findAll("span",{"class":"ah_k"})

    i = 1
    while i:
        html = "http://news.baidu.com/"
        HTML = urlopen(html)
        bsObj = BeautifulSoup(HTML, "html.parser")
#        TEST = bsObj.find("div",{"class":"hotnews"}).findAll("a",href=re.compile("^(http).*$"))
#        TEST = bsObj.find("div",{"class":"hotnews"}).findAll("a",{"target":"_blank"})
        TEST = bsObj.find("div",{"class":"hotnews"}).findAll("a",target="_blank")
        print(str(i)+"th rotation!")
        TIME = (datetime.datetime.now())
        LIST = list()
        for test in TEST:
       # print(test.get_text())
            LIST.append(test.get_text())
        print(LIST)
        DIC[TIME]=LIST
#        print(DIC)
        if(i > time):
            break
        i =i + 1
        sleep(duration)

#    print(DIC)
    return DIC

def main():
    dic =naver(3,2)
    print(dic)

if __name__=="__main__":
    main()


