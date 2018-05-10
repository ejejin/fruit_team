
from selenium import webdriver
import time
driver = webdriver.PhantomJS()

driver.get("https://weibo.com/u/5292292281?refer_flag=1001030103_&is_hot=1")
time.sleep(7)
#print(driver.find_element_by_id("item_text W_fl").text)
#HOME = driver.find_elements_by_css_selector('.item_text.W_fl')
HOME = driver.find_elements_by_tag_name('span')
for i in HOME:
    print(i.text)

for iii in range(len(HOME)):
    s1 = (HOME[iii].text).encode('unicode-escape')#.decode('string_escape')
#    if(s1.find('\\u5317\\u4eac') != -1):                        # "\\u5317\\u4eac"  is  北京
    print(HOME[iii].text)
#        jjj = jjj+1
#        break



driver.close()


