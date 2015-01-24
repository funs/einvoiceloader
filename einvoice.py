# -*- coding:utf-8 -*-
__author__ = 'ITRI'
import csv

def getInvoice(filepath=''):
    try:
        f=open(filepath,'rb')
        csvreader = csv.reader(f)
        data=[]
        for raw in csvreader:
            k = raw[0].decode('big5').encode('utf-8')
            l = k.split('|')
            data.append(l)
    except(Exception) as err:
        print(err)
    #print(data[0][1])
    return data

if __name__ == '__main__':
    data = getInvoice('invoice.csv')
    print(data[0][1])