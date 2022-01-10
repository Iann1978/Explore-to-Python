import requests
import re

url = r'http://www.redbull.com.cn/about/branch'

response = requests.get(url)

print(response.text)

company = re.findall('<h2>(.*?)</h2>', response.text)

print()
print(company)


add = re.findall("<p class=\'mapIco\'>(.*?)</p>", response.text)
print()
print(add)


import bs4
soup = bs4.BeautifulSoup(response.text,"html.parser")
mail = [i.text for i in soup.findAll(name='p', attrs={'class': 'mailIco'})]
tel = [i.text for i in soup.findAll(name='p', attrs={'class': 'telIco'})]
print(mail)


import pandas as pd
df = pd.DataFrame({'company':company,'add':add, 'mail': mail, 'tel': tel})
print(df)

