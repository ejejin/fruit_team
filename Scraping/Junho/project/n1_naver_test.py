#-*-coding: UTF-8-*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
#import numpy
from time import sleep
#random.seed(datetime.datetime.now())

def naver(duration=3,iteration=3):

    DIC = dict()
    #html = "https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-04-04T18:20:00"
    html = "https://www.naver.com/"
#    HTML = urlopen(html)
#    bsObj = BeautifulSoup(HTML, "html.parser")
    #print(bsObj)

#    TEST = bsObj.find("ul",{"class":"ah_l"}).findAll("span",{"class":"ah_k"})
#    wf = open("naver_test1.txt", "w+")
   
    j = 0
    i = 1
    ii = 0
    while i:
        try:
            HTML = urlopen(html)
        except:
            HTTPError
            if(i==1):
                j=1
            continue
        bsObj = BeautifulSoup(HTML, "html.parser")
        TEST = bsObj.find("ul",{"class":"ah_l"}).findAll("span",{"class":"ah_k"})
        print(str(i)+"th rotation!")
        TIME = (datetime.datetime.now())
        TIME = str(TIME);  TIME = TIME.replace(" ","_")
        if((i==1) | (j==1)):
            TIME = str(TIME); TIME = TIME.replace(" ","_"); TIME = TIME.replace(":","-")
            loca = len(TIME)
            for ij in range(1,len(TIME)+1):
                if((TIME[-ij] == '.')):
                    loca = ij-1
                    break
            TIME = TIME.replace(TIME[len(TIME)-loca:len(TIME)],"")
            RUNTIME = duration * iteration / 3600;  RUNTIME = round(RUNTIME,3)
            fn = "naver_hot_"+str(RUNTIME)+"H_"+TIME+"txt"
            wf = open(fn,"w+")
            j=0
        LIST = list()
        for test in TEST:
       # print(test.get_text())
            LIST.append(test.get_text())
        print(LIST)


        for ik in range(len(LIST)):
            if(ik==len(LIST)-1):
                wf.write(str(LIST[ik])+"\n")
            else:
                wf.write(str(LIST[ik]) + " ")

        DIC[TIME]=LIST

        if(i > iteration):
            break
        i =i + 1
        sleep(duration)

#    print(DIC)
    return DIC

def main():
    dic = naver(10,5)
#    print(dic)

if __name__=="__main__":
    main()


