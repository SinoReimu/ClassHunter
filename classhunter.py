#!/usr/bin/python
#coding=utf-8

import cookielib
import re
import sys
import urllib
from util import read, getopener
from ocr import ocrCaptcha

# init my opener
cookiename = 'cookie.dat'
cookie = cookielib.MozillaCookieJar(cookiename)
cookie.load(cookiename, ignore_discard=True, ignore_expires=True)
opener = getopener(cookie)

response = opener.open('http://jxgl.hdu.edu.cn/CheckCode.aspx')

def initTable(threshold=140):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table
	
captcha = file('captcha.gif', 'w')
captcha.write(response.read())
captcha.close()

print(ocrCaptcha())

