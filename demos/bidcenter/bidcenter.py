# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests
import bs4

print('hello')

url = r'https://search.bidcenter.com.cn/search?keywords=服装'
headers = {
#':authority': 'search.bidcenter.com.cn'
# ,':method': 'GET'
# ,':path': '/search?keywords=hehe'
# ,':scheme': 'https'
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
,'accept-encoding': 'gzip, deflate, br'
,'accept-language': 'zh-CN,zh;q=0.9'
,'cache-control': 'max-age=0'
,'cookie': 'UM_distinctid=1714727c1e5501-0c3e7f555006c3-f313f6d-295d29-1714727c1e6799; Hm_lvt_9954aa2d605277c3e24cb76809e2f856=1586036720,1586224891; bidguid=71d2e71f-56c9-4b94-800a-d3580c3fa0e4; bidguid202039_26F54EAD8B31F5DA88F82FEB9DC04F14=a695ec8d-80f9-4efb-9d57-5bf5ef8bf49a; CNZZDATA888048=cnzz_eid%3D544982081-1586222315-https%253A%252F%252Fwww.bidcenter.com.cn%252F%26ntime%3D1586222315; keywords==hehe; Hm_lpvt_9954aa2d605277c3e24cb76809e2f856=1586227448'
,'sec-fetch-dest': 'document'
,'sec-fetch-mode': 'navigate'
,'sec-fetch-site': 'none'
,'sec-fetch-user': '?1'
,'upgrade-insecure-requests': '1'
,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' 
           }
response = requests.get(url,headers=headers)
print(response)
print(response.text)
print('\n\n')
soup = bs4.BeautifulSoup(response.text, features='html.parser')
names = [i for i in soup.findAll(name='td',attrs={'class':'zb_title'})]
print(names)
# types = [i.text.split('|')[0] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
# areas = [i.text.split('|')[1] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
# floors = [i.text.split('|')[4] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]
# ages = [i.text.split('|')[-2] for i in soup.findAll(name='div', attrs={'class':'houseInfo'})]

# dic = {'name':names,'type':types,'area':areas,'floor':floors,'age':ages}
# print(dic)

# import pandas as pd

# table = pd.DataFrame(dic)
# print(table)

