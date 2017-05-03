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
baseUrl = "http://www.ewg.org"
url ='http://www.ewg.org/skindeep/search.php'

#如果是第一行跳过
cellValue = 'PLACENTAL ENZYMES'

queryParams = {
    'query':cellValue,
    'search_group':'ingredients'
}
params = parse.urlencode(queryParams)
req = request.Request(url + '?' + params)
req.add_header('User-Agent',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/58.0.3029.81 Safari/537.36')

with request.urlopen(req) as f:
    returnData = f.read().decode('utf-8')
    soup = BeautifulSoup(returnData,'lxml')
    table_browse = soup.find(id='table-browse')
    if table_browse != None:
        print("table_browse:" + str(table_browse))
        centerTd = table_browse.find_all('tr')[1].find(align="center")
        hrefs = centerTd.find_all('a')
        for href in hrefs:
            print(baseUrl + href.get('href'))

            # print(hrefs[0].get('href'))
    else:
        print("empty")

