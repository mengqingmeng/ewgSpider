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

cellValue = 'PLACENTAL PROTEIN'

queryParams = {
    'query':cellValue,
    'search_group':'ingredients'
}

'''
请求数据方法
'''
def requestData(url,params):
    if params == None:
        req = request.Request(url)
    else:
        params = parse.urlencode(params)
        req = request.Request(url + '?' + params)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/58.0.3029.81 Safari/537.36')
    with request.urlopen(req) as f:
        returnData = f.read().decode('utf-8')
        return returnData

'''
2.获取详情信息
'''
def getDetail(url):
    returnData = requestData(url)
    print(BeautifulSoup(returnData,'lxml'))

'''
1.根据成分名称，请求成分详情链接
'''
returnData = requestData(firstUrl,queryParams)
soup = BeautifulSoup(returnData,'lxml')
#print("soup:",soup)
table_browse = soup.find(id='table-browse')
#print("table_browse:" + str(table_browse))
if table_browse != None:
    #print("table_browse:" + str(table_browse))
    centerTd = table_browse.find_all('tr')[1].find(align="center")
    hrefs = centerTd.find_all('a')
    detailUrl = baseUrl + hrefs[0]  #获得，获取详细页链接
    print('detailURL:'+detailUrl)
    # 获取详细页
    getDetail(detailUrl)
    #for href in hrefs:
    #    print(baseUrl + href.get('href'))
        # print(hrefs[0].get('href'))
else:
    print("empty")

