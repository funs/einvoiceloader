# -*- coding:utf-8 -*-
__author__ = 'HCWei'
import csv
#import xlwt

def getInvoice(filepath=''):
    try:
        f=open(filepath,'rb')
        csvreader = csv.reader(f)
        data=[]
        for raw in csvreader:
            k = raw[0].decode('big5').encode('utf-8')
            l = k.split('|')
            data.append(l)
        return data
    except(Exception) as err:
        print(err)
    #print(data[0][1])

'''
def saveExcel(filepath,data):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet 1')
    for i, l in enumerate(data):
        for j, col in enumerate(l):
            sheet.write(i, j, col)
    book.save(filepath)
'''
def setlist(data):
    try:
        listdata = []
        for i in data:
            if i[0] == 'M':
                listdata.append(i[2]+' / '+i[3]+' / '+i[5])
            else:
                pass
        return listdata
    except Exception as err:
        print(err)

def compare_content(data,text):
    contentlist = []
    content = ''
    try:
        for i in data:
            if (i[0] == 'D') & (i[1].find(text[0:10])==0):
                contentlist.append(i[3]+' $'+i[2]+'\n')
            else:
                pass
        #print(contentlist)
        for i in contentlist:
            content = content+i
        #print(content)
        return content
    except Exception as err:
        print(err)


if __name__ == '__main__':
    data = getInvoice('invoice.csv')
    for i in data[0]:
        print(i)
        print(type(i))

    #saveExcel('invoice.xls',data)
    k = setlist(data)
    print(k[18])
    j = compare_content(data,k[3])
    print('aaa')
    print(j)