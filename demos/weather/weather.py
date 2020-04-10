# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests
import re
import pandas as pd

print('hello')

url = r'http://tianqi.2345.com/t/wea_history/js/202002/58362_202002.js'
response = requests.get(url)
print(response)
print(response.text)

ymd = re.findall("ymd:'(2020-02-[012]\d)'",response.text)
bWendu = re.findall(",bWendu:'([\d-]+.)'",response.text)
yWendu = re.findall("yWendu:'([\d-]+.)'",response.text)
print(len(ymd))
print(len(bWendu))
print(len(yWendu))
# types = [i.text.split('|')[0] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
# areas = [i.text.split('|')[1] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
# floors = [i.text.split('|')[4] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
# ages = [i.text.split('|')[-2] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]

dic = {'ymd':ymd,'bWendu':bWendu,'yWendu':yWendu}
# print(dic)

# 

table = pd.DataFrame(dic)
print(table)

