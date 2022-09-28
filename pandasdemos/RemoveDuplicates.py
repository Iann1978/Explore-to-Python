
print("Remove Duplicates")

import redis
import json
import numpy as np
import pandas as pd



r = redis.StrictRedis(host='192.168.100.80', db=1)

interphones = r.lrange('interphone_src', 0, 200000)
# print('interphones')
# print(interphones)
# print(len(interphones))
# print(type(interphones))

interphones1 = [x.decode('utf-8') for x in interphones]
# print('interphones1')
# print(interphones1)
# print(len(interphones1))
# print(type(interphones1))
# print(type(interphones1[0]))

interphones2 = [json.loads(x) for x in interphones1]
# print('interphones2')
# print(interphones2)
# print(len(interphones2))
# print(type(interphones2))
# print(type(interphones2[0]))

df = pd.DataFrame(interphones2[0:1])
print(df)

total = len(interphones2)
counter = 0;
YESNO =True
judge = [{'YESNO':YESNO, 'x':interphones2[0]}]
# judge = [YESNO]
print(type(judge))
for x in interphones2:
    counter = counter + 1
    if counter%500 == 0:
        print(counter,"/", total)

    NO = x['NO']
    Time = x['Time']
    # print(NO)
    # print(type(NO))
    # print(Time)
    # print(type(Time))
    qdf = df.query('NO==@NO and Time==@Time')
    YESNO = qdf.shape[0] == 0
    # judge = judge.append(judge, {'YESNO':YESNO, 'x':x})
    # print('hehe',counter)
    # print(judge)
    # print(type(judge))
    # print(type(judge[0]))
    # print('hehe')
    judge.append({'YESNO':YESNO, 'x':x})
    # print(judge)
    # print(qdf)
    if YESNO:
        df = df.append(x,ignore_index=True)

print(df)
print(df.shape)