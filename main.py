# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:55:01 2020

@author: 軒亭
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver




def w104(xx):
    yy=10       #頁數
    for i in range(1,yy):
        url=f"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={xx}&area=6001008000&order=11&asc=0&page={i}&mode=s"
        aa=requests.get(url)
        bs=BeautifulSoup(aa.text, 'html.parser')
        ww=bs.find_all(class_="b-block--top-bord job-list-item b-clearfix js-job-item")
        for xx in ww:
            cc=xx.find(class_="b-tit")
            yy=xx.find(class_="job-list-item__info b-clearfix b-content")
            print(cc.a.text.strip())
            print(cc.a["href"])
            print(yy.text.strip())
            print("---------------------------------------------------")
#    zz="本函式結束"
    print(f"{w104.__name__:=^40}")
    

def w1111(xx):
    url=f"https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks={xx}&c0=100900&fs=1&col=da&sort=desc&page=1"
    aa=requests.get(url)
    cc=BeautifulSoup(aa.text,"html.parser")
    dd=cc.find_all("div","jbInfoin")
    ff=cc.find_all("div","jbInfoTxt")
    for ee,gg in zip(dd,ff):
        print(ee.h3.a["title"]) 
        print(ee.h3.a["href"])
        print(gg.text)
        print("-"*80)
        
    print(f"{w1111.__name__:=^40}")


def w518(xx):
    url=f"https://www.518.com.tw/job-index-P-1.html?i=1&am=1&ad={xx}&ai=0&orderType=1&orderField=8"
    bb=requests.get(url)
    bb=BeautifulSoup(bb.text,"html.parser")
    cc=bb.find_all(class_="title")
    dd=bb.find_all(class_="sumbox")

    for ee,gg in zip(cc,dd):
        print(ee.text.strip())
        print(ee.a["href"])
        print(gg.text.strip())
        print("-"*85)
    print(f"{w518.__name__:=^40}")



def yes123(xx):
    url="https://www.yes123.com.tw/admin/job_refer_list.asp"
#    xx="python"
    dr=webdriver.Chrome()
    dr.get(url)
    dr.find_element_by_id("find_key1").send_keys(xx)
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
    print(f"{yes123.__name__:=^40}")
    





def main(xx):

    
    w104(xx)
    w1111(xx)
    w518(xx)
    yes123(xx)
    
if __name__ == '__main__':
    
    
    main("python")