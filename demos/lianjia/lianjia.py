# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests
import bs4

print('hello')

url = r'https://sh.lianjia.com/ershoufang/pudong/pgl/'
response = requests.get(url)
print(response)

soup = bs4.BeautifulSoup(response.text, features='html.parser')
names = [i.text.strip('|') for i in soup.findAll(name='a',attrs={'data-el':'region'})]
types = [i.text.split('|')[0] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
areas = [i.text.split('|')[1] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
floors = [i.text.split('|')[4] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
ages = [i.text.split('|')[-2] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]

dic = {'name':names,'type':types,'area':areas,'floor':floors,'age':ages}
print(dic)

import pandas as pd

table = pd.DataFrame(dic)
print(table)

