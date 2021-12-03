
rows = [
    {'address': '5412 N CLARK', 'data': '07/01/2012'},
    {'address': '5148 N CLARK', 'data': '07/04/2012'},
    {'address': '5800 E CLARK', 'data': '07/02/2012'},
    {'address': '2122 N CLARK', 'data': '07/03/2012'},
    {'address': '5645 N CLARK', 'data': '07/02/2012'},
    {'address': '1060 W CLARK', 'data': '07/02/2012'},
    {'address': '4801 N CLARK', 'data': '07/01/2012'},
    {'address': '1039 W CLARK', 'data': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('data'))

for r in rows:
    print(r)


for data, items in groupby(rows, key=itemgetter('data')):
    print(data)
    for i in items:
        print(' ', i)
