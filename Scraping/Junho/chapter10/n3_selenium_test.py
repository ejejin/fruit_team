
from selenium import webdriver
import time
driver = webdriver.PhantomJS()

driver.get("https://s.weibo.com/weibo/%25E9%259B%25BE%25E9%259C%25BE&region=custom:11:1000&typeall=1&suball=1&timescope=custom:2018-05-01:2018-05-02&Refer=g")
time.sleep(20)
#print(driver.find_element_by_id("item_text W_fl").text)
#HOME = driver.find_elements_by_css_selector('.item_text.W_fl')
KEYWORD = driver.find_elements_by_id("em")
for i in KEYWORD:
    print(i.text)


KEYWORD = driver.find_elements_by_css_selector("red")
for i in KEYWORD:
    print(i.text)


KEYWORD = driver.find_elements_by_css_selector("#red")
for i in KEYWORD:
    print(i.text)

for iii in range(len(KEYWORD)):
    s1 = (KEYWORD[iii].text).encode('unicode-escape')#.decode('string_escape')
#    if(s1.find('\\u5317\\u4eac') != -1):                        # "\\u5317\\u4eac"  is  北京
    print(KEYWORD[iii].text)
#        jjj = jjj+1
#        break



driver.close()


