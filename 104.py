# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:04:55 2020
創建104爬蟲
@author: 軒亭
"""

import requests
from bs4 import BeautifulSoup

xx="高薪" #搜尋工作類型       

for i in range(1,10):
    url=f"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={xx}&area=6001008000&order=11&asc=0&page={i}&mode=s"
    aa=requests.get(url)
    bs=BeautifulSoup(aa.text, 'html.parser')
    ww=bs.find_all(class_="b-block--top-bord job-list-item b-clearfix js-job-item")
    for dd in ww:
        cc=dd.find(class_="b-tit")
        ee=dd.find(class_="b-block__left")
        print(cc.a.text.strip())
        print(cc.a["href"])
        try:
            
            print(ee.p.text.strip())
            
        except BaseException as k:
            print(k)
        print("---------------------------------------------------")
        