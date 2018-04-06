#-*-coding: UTF-8-*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
#import numpy
from time import sleep
#random.seed(datetime.datetime.now())

def Baidu_News(duration=3,iteration=3):

    DIC = dict()
    html = "http://news.baidu.com/"
    ILIST = list()  
 
    j = 0
    i = 1
    ii = 0
    IJK = 0
    while i:
        try:
            HTML = urlopen(html)
        except:
            HTTPError
            if(i==1):
                j=1
            continue
        bsObj = BeautifulSoup(HTML, "html.parser")
        TEST = bsObj.find("div",{"class":"hotnews"}).findAll("a",target="_blank")
        print(str(i)+"th rotation!")
        TIME = (datetime.datetime.now())
        TIME = str(TIME);  TIME = TIME.replace(" ","_")
        TIME = str(TIME); TIME = TIME.replace(" ","_"); TIME = TIME.replace(":","-")
        loca = len(TIME)
        for ij in range(1,len(TIME)+1):
            if((TIME[-ij] == '.')):
                loca = ij-1
                break
        TIME = TIME.replace(TIME[len(TIME)-loca-1:len(TIME)],"")
        if((i==1) | (j==1)):
            for test in TEST:
                ILIST.append(test.get_text())
            RUNTIME = duration * iteration / 3600;  RUNTIME = round(RUNTIME,3)
            fn = "Baidu_News_hot_"+str(RUNTIME)+"H_"+TIME+".txt"
            wf = open(fn,"w+")
            j=0
        LIST = list()
        for test in TEST:
            LIST.append(test.get_text())
        print(LIST)
        if(i > iteration):
            break
        i =i + 1

        if(IJK == 0):
            IJK = 1
            for ik in range(len(LIST)):
                if(ik==0):
                    wf.write(str(TIME)+": ") 
                if(ik==len(LIST)-1):
                    wf.write(str(LIST[ik])+"\n")
                else:
                     wf.write(str(LIST[ik]) + ",  ")

        if(ILIST == LIST):
            sleep(duration)
            continue
        else:
            ILIST = LIST
            sleep(duration)
            IJK = 0

        DIC[TIME]=LIST
        sleep(duration)
    return DIC

def main():
    dic = Baidu_News(2,2)
#    print(dic)

if __name__=="__main__":
    main()


