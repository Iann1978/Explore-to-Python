
import requests
import bs4
import pandas as pd
import re

urlbase = r"http://www.ccgp-shandong.gov.cn"
url = r"http://www.ccgp-shandong.gov.cn/sdgp2017/site/listnoleft.jsp?cmd=search&subject=%E6%9C%8D%E8%A3%85"

resp = requests.get(url)


# print(resp.status_code)
#
# print(resp.text)

soup = bs4.BeautifulSoup(resp.text, features='html.parser')
title = [i.text for i in soup.findAll(name='span', attrs={'class': 'title'})]
href = [i.contents[0]['href'] for i in soup.findAll(name='span', attrs={'class': 'title'})]


print()

# print(title)

df = pd.DataFrame({'title': title, 'href': href})
# print(df)



aaa = soup.findAll(name='span', attrs={'class': 'title'})[0]



# print(aaa)
bbb = aaa.contents[0]['href']
# print(aaa)
# print(bbb)

newurl =urlbase + bbb

# print(newurl)


resp1 = requests.get(newurl)

print(resp1.text)