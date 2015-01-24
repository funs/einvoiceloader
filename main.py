# -*- coding:utf-8 -*-
__author__ = 'ITRI'
import csv

f=open('invoice.csv','rb')
csvreader = csv.reader(f)
data=[]
for raw in csvreader:
    try:
        k = raw[0].decode('big5').encode('utf-8')
        l = k.split('|')
        #print(l)
        data.append(l)
    except(Exception) as err:
        print(err)
print(data).