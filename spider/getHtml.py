# -*- coding:utf-8 -*- ＃
import urllib.request
import re
import sys
import chardet


def GetHtml(url):
    page = urllib.request.urlopen(url)
    contex = page.read()
    return contex


def GetLink(html):
    reg = r' <li  ><a href="(.+)">(.+)</a></li>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

#
# url = "http://www.taobao.com/"
# print((GetHtml(url)))
# print((GetHtml(url).decode('utf-8')))
# print((GetHtml(url).decode('utf-8').encode('utf-8')))
# get = GetLink(GetHtml(url).decode('utf-8').encode('utf-8'))