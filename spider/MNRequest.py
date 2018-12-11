# coding:utf-8
import re
import time
from urllib import request

import requests
from bs4 import BeautifulSoup

#模拟用户的cookie
cookie = '''uuid=341c928448caf75c78f35f768ece788e; Hm_lvt_bc75b9260fe72ee13356c664daa5568c=1515467001,1515548182,1515563872,1515646433; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221569937%22%2C%22props%22%3A%7B%22uid%22%3A0%2C%22gamenewId%22%3A%22c6ad8cac9e930317%22%2C%22sessionSource%22%3A%22%22%7D%7D; ac_username=%E5%A4%A7%E5%A4%A7%E7%9A%84%E7%96%AF%E5%AD%90; auth_key=1569937; auth_key_ac_sha1=-1993871800; auth_key_ac_sha1_=zGIJqwaDcP/9oI8Z78kbbPLmObE=; checkReal=0; ac_userimg=http%3A%2F%2Fcdn.aixifan.com%2Fdotnet%2F20120923%2Fstyle%2Fimage%2Favatar.jpg; JSESSIONID=4a2e21da073d46ec8b1606543e0869eb; analytics=GA1.2.1889439718.1513912352; userGroupLevel=1; checkMobile=1; checkEmail=1; online_status=8905; userLevel=13; identifier=1569937; usersig=eJxNkF1PwjAUhv-LbjHSz0FJuBgogohGMYrcLLU9GwXdmq5bUMN-dzQz8Vw*T96c95yf6PlufSmtNTqVPqVOR6MIRRcBw9EaB6nMPLgWEy4ICtP5BlxlyuKsEOaY0P-SaCi8yUyIYh4LQQedqkzestX143QxX8uX*OOwka4-7A*O9PZt*-CtRBNP-ay3q5dPsnSL-Y3a4lViErhSr7vMAqVKwYTbZEPQ*4Tf73Vd4fnM9pa6KfKcE5uPx3-L9CEN951rsLYfQzgmnfTmE0I9woZYMMw6LpUq68Kn-stCeMjpF8Z1VyI_; supernova=1; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1525928769,1526003027,1526266288,1526285297; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1526285402; clientlanguage=zh_CN'''
#拼一个请求Header
header = {
    'User-Agent' :      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie': cookie}

url = 'http://www.acfun.cn/'

#利用各种工具获取网页，requests,urllib,scrapy
wbdata = requests.get(url, headers=header).content.decode('utf-8')

# print(sys.getfilesystemencoding())
# print(wg.GetHtml(url).decode('utf-8'))
# print('Html is encoding by : %',chardet.detect(wg.GetHtml(url)))


print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#print(wbdata)

listUrl = re.findall(r'http:.jpg',wbdata)

listJpg = re.findall('http:.jpg and http:.png and http:.jpeg',wbdata)

listPng = re.findall('http:.+\.png',wbdata)

listPng = re.findall('http:.+\.jpeg',wbdata)


for jpg in listUrl:
    print(jpg)

print ('JPG>>>>>>>>>>')



for jpg in listJpg:
    print(jpg)



print(property(wbdata))
# print ('============================================================')
#
#
# print (wbdata.decode('utf-8'))
#
# print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

soup = BeautifulSoup(wbdata, 'html.parser')
print(soup)


# Beautiful Soup和正则表达式结合，提取出所有图片的链接（img标签中，class=**，以.jpg结尾的链接）
links = soup.find_all('img',src=re.compile(r'.jpg$|.png$'))
# 设置保存的路径，否则会保存到程序当前路径
local_path = r'E:\Python\PyCharm\PyCharm Community Edition 2017.2.3\workspace\mySpider\pic'

for link in links:
    print(link.attrs['src'])
    # 保存链接并命名，time防止命名冲突
    request.urlretrieve(link.attrs['src'], local_path+r'\%s.jpg' % time.time())
