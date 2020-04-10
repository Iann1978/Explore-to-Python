# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:14:41 2020

@author: ALIENWARE
"""

import pymysql
import pandas as pd

con = pymysql.connect(host='106.120.93.169',user='test',password='test',database='test')
print(con)
table = pd.read_sql("select * from rect",con=con)
print(table)
con.close()