# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:04:55 2020
創建1111爬蟲
@author: 軒亭
"""
import requests
from bs4 import BeautifulSoup
#from bs4 import Beautifulsoup
bb="python"
url=f"https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks={bb}&c0=100900&fs=1&col=da&sort=desc&page=1"
aa=requests.get(url)
#print(aa.text)
cc=BeautifulSoup(aa.text,"html.parser")
dd=cc.find_all("div","jbInfoin")
ff=cc.find_all("div","jbInfoTxt")
for ee,gg in zip(dd,ff):
    print(ee.h3.a["title"]) 
    print(ee.h3.a["href"])
    print(gg.text)
    print("-"*80)

     
