
print("Remove Duplicates1")

import redis
import json
import numpy as np
import pandas as pd



r = redis.StrictRedis(host='192.168.100.80', port=6379, db=1)
r2 = redis.StrictRedis(host='192.168.100.80', port=6379, db=2)
r.keys()
print(r.llen('interphone_src'))

interphones = r.lrange('interphone_src', 0, 300000)
interphones1 = [x.decode('utf-8') for x in interphones]
interphones2 = [json.loads(x) for x in interphones1]
print(interphones2[0])

a = interphones2[0]['NO'] + "_" + str(interphones2[0]['Time'])
print(a)

total = len(interphones2)
counter1 = 0
counter2 = 0
errcounter = 0
counter = 0
print("total:", total)
dict = {}
for v in interphones2:

    if counter % 1000 == 0:
        keycount = len(dict)
        dict = {}
        print(counter, "/", total, "(", counter2, "）", "(", keycount, "）")
    counter = counter + 1

    key = v['NO'] + "_" + str(v['Time'])

    # if key in dict
    if key in dict:
        vv = dict[key]
        err = (vv['Lon'] != v['Lon']) \
              or (vv['Lat'] != v['Lat']) \
              or (vv['Speed'] != v['Speed'])\
              or (vv['Direction'] != v['Direction'])\
              or (vv['Height'] != v['Height']) \
              or (vv['Precision'] != v['Precision'])\
              or (vv['Department'] != v['Department'])\
              or (vv['Organization'] != v['Organization'])\
              or (vv['AllExtendsField'] != v['AllExtendsField'])
        if err:
            errcounter = errcounter + 1



    dict[key] = v



    if r2.exists(key):
        counter1 = counter1 + 1
    else:
        counter2 = counter2 + 1
    r2.set(key, 1, px=10)

print("counter1:", counter1)
print("counter2:", counter2)
print("counter:", counter)
print("errcounter:", errcounter)


# src = [1,1,2,3,4,3,5,6,3,6,3,1,1,1,2,3,4,3,5,6,3,6,3,1,1,1,2,3,4,3,5,6,3,6,3,1,1,1,2,3,4,3,5,6,3,6,3,1]
# print(src)
#
# counter = 0
# for v in src:
#     if r.exists(v):
#         counter = counter + 1
#     r.set(v,1,px=1)
#
# print(counter)
