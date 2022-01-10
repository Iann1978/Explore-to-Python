import requests

url = r'https://sh.lianjia.com/ershoufang/pudong/pg1/'
response = requests.get(url)
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36'
}
print(response)

import bs4
soup = bs4.BeautifulSoup(response.text, "html.parser")
names = [i.text for i in soup.findAll(name='a', attrs={'target': '_blank',  'data-el': 'region'})]
types = [i.text.split('|')[0].strip() for i in soup.findAll(name = 'div', attrs = {'class': 'houseInfo'})]
sizes = [i.text.split('|')[1].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
direction = [i.text.split('|')[2].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
decoration = [i.text.split('|')[3].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
floor = [i.text.split('|')[4].strip() for i in soup.findAll(name='div', attrs = {'class':'houseInfo'})]
total = [i.text for i in soup.findAll(name='div', attrs = {'class':'totalPrice'})]
price = [i.text for i in soup.findAll(name='div', attrs = {'class':'unitPrice'})]

print(price)

#
import pandas as pd
df = pd.DataFrame({'name': names, 'type': types, 'size': sizes, 'direction': direction, 'decoration': decoration,
                   'floor': floor, 'total': total, 'price': price})
print(df)