# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:23:35 2020

@author: 軒亭

yes123

"""
#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
url="https://www.yes123.com.tw/admin/job_refer_list.asp"
dr=webdriver.Chrome()
dr.get(url)
dr.find_element_by_id("find_key1").send_keys("python")
dr.find_element_by_class_name("bt_search").click()
dr.find_element_by_xpath("//div[@class='illustrate']//li[2]//a[1]").click()
dr.find_element_by_xpath("//li[@class='date2']//a").click()
aa=dr.find_elements_by_class_name("t0")
cc=dr.find_elements_by_xpath("//span[@class='t0']//a")
ee=dr.find_elements_by_class_name("t3")
for bb,dd,ff in zip(aa,cc,ee):
    print(bb.text)
    print(dd.get_attribute("href"))
    print(ff.text.strip())
    print("-"*85)
    
dr.quit()

    

#bb=requests.get(url)
#bb=BeautifulSoup(bb.text,"html.parser")
#bb=bb.find_all(class_="box_detail_list")