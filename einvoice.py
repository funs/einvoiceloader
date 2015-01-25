# -*- coding:utf-8 -*-
__author__ = 'HCWei'
import csv
import xlwt

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

def saveExcel(filepath,data):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet 1')
    for i, l in enumerate(data):
        for j, col in enumerate(l):
            sheet.write(i, j, col)
    book.save(filepath)
if __name__ == '__main__':
    data = getInvoice('invoice.csv')
    print(data[0][1])
    saveExcel('invoice.xls',data)