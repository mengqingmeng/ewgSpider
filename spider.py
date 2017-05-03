# -*- coding:utf-8 -*-
'''
爬取EWG网站数据
'''
from openpyxl import Workbook, load_workbook
from urllib import request,parse
from bs4 import BeautifulSoup
import os

# with open('/Users/mqm/Desktop/jtp/ewg/EWG待爬成分列表20170502.xlsx', 'r') as f:
#     print(f.read())
url ='http://www.ewg.org/skindeep/search.php'


#加载excel文件
wb = load_workbook("/Users/mqm/Desktop/jtp/ewg/EWG待爬成分列表20170502.xlsx")

#获取第一个Sheet
sheet1 = wb.get_sheet_by_name('Sheet1')

#遍历行
for row in sheet1.rows:
    #遍历单元格
    for cell in row:
        cellValue = cell.value
        #如果是第一行跳过
        if '待爬成分名称' in cellValue:
            continue
        #print("cell:",cell.value)
        queryParams = {
            'query':cellValue
        }
        params = parse.urlencode(queryParams)
        req = request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/58.0.3029.81 Safari/537.36')

        with request.urlopen(req,data = params.encode('utf-8')) as f:
            returnData = f.read().decode('utf-8')
            soup = BeautifulSoup(returnData)
            print("data:",soup.prettify())
