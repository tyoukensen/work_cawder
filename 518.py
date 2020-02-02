# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:18:53 2020
518人力銀行
@author: 軒亭
"""
import requests
#from bs4 import Beautifulsoup
from bs4 import BeautifulSoup
xx="python"
url=f"https://www.518.com.tw/job-index-P-1.html?i=1&am=1&ad={xx}&ai=0&orderType=1&orderField=8"
bb=requests.get(url)
bb=BeautifulSoup(bb.text,"html.parser")
cc=bb.find_all(class_="title")
dd=bb.find_all(class_="sumbox")
#for ff in dd:
#    gg=ff.find_all("p")[1]
#for ee in cc:
#    print(ee.text.strip())
#    print(ee.a["href"])
#    print(gg.text.strip())
#    print("-"*85)
for ee,gg in zip(cc,dd):
    print(ee.text.strip())
    print(ee.a["href"])
    print(gg.text.strip())
    print("-"*85)
    
    
    
    
