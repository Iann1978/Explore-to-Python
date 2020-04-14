# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:14:41 2020

@author: ALIENWARE
"""

import pymysql
import pandas as pd
import cv2
import numpy as np





con = pymysql.connect(host='106.120.93.169',user='test',password='test',database='test')
print(con)
table = pd.read_sql("select rdata from tile where level=17 and xidx=201149 and yidx = 77696",con=con)
print(table)
print(type(table))

print(type(table.values))
con.close()

print(type(table.values[0][0]))
# print(table.values[0][0])

img = np.frombuffer(table.values[0][0], dtype='int8')
print(type(img))
print(img.shape)
img1 = img.reshape((256,256))
print(img1.shape)
# img = cv2.imread('1.jpeg')
# print(type(img))
cv2.namedWindow("demo")
cv2.imshow("demo", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print('hehe')