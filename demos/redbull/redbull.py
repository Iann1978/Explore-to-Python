# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import re
import bs4

print('hello')

url = r'http://www.redbull.com.cn/about/branch'
response = requests.get(url)
comnpanies = re.findall('<h2>(.*?)</h2>',response.text)
addresses = re.findall("<p class='mapIco'>(.*?)</p>",response.text)
soup = bs4.BeautifulSoup(response.text)
mails = [i.text for i in soup.findAll('p',{'class':'mailIco'})]
phones = [i.text for i in soup.findAll('p',{'class':'telIco'})]

table = {'company':comnpanies, 'address':addresses, 'mail':mails, 'phone':phones}
#print(table)

import pandas as pd

table1 = pd.DataFrame(table)
print(table1)