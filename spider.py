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
firstUrl ='http://www.ewg.org/skindeep/search.php'


#加载excel文件
wb = load_workbook("/Users/mqm/Desktop/jtp/ewg/EWG待爬成分列表20170502.xlsx")

#获取第一个Sheet
sheet1 = wb.get_sheet_by_name('Sheet1')

'''
请求数据方法
'''
def requestData(url,params):
    if params !=None:
        req = request.Request(url)
    else:
        req = request.Request(url + '?' + params)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/58.0.3029.81 Safari/537.36')
    with request.urlopen(req) as f:
        returnData = f.read().decode('utf-8')
        return returnData

'''
获取详情信息
'''
def getDetail(url):
    pass


#遍历行
for row in sheet1.rows:
    #遍历单元格
    for cell in row:
        cellValue = cell.value
        #如果是第一行跳过
        if 'name' in cellValue:
            continue
        #print("cell:",cell.value)
        queryParams = {
            'query': cellValue,
            'search_group': 'ingredients'
        }

        params = parse.urlencode(queryParams)
        req = request.Request(firstUrl + '?' + params)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/58.0.3029.81 Safari/537.36')

        '''
        1.取成分详细页面的链接
        '''
        returnData = requestData(firstUrl, queryParams)
        soup = BeautifulSoup(returnData, 'lxml')
        table_browse = soup.find(id='table-browse')
        if table_browse != None:
            # print("table_browse:" + str(table_browse))
            centerTd = table_browse.find_all('tr')[1].find(align="center")
            hrefs = centerTd.find_all('a')
            detailUrl = baseUrl + hrefs[0]  # 获得，获取详细页链接

            '''
            获取详细页
            '''
            getDetail(detailUrl)
