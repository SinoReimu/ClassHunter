#!/usr/bin/python
#coding=utf-8

import cookielib
import re
import sys
import urllib
from util import read, getopener

# get argument 

if len(sys.argv) < 5:
	print('usage:python gradequery.py [name] [student code] [year] [term(1,2,3)]')
	sys.exit(0)
else:
	name = sys.argv[1]
	code = sys.argv[2]
	year = sys.argv[3]
	term = sys.argv[4]

baseurl = 'http://jxgl.hdu.edu.cn/xscjcx_dq.aspx?'

# init my opener
paramters = urllib.urlencode({
						'xh': code, 
						'xm': name.decode('utf-8').encode('gbk'),
						'gnmkdm': 'N121605'})
cookiename = 'cookie.dat'
cookie = cookielib.MozillaCookieJar(cookiename)
cookie.load(cookiename, ignore_discard=True, ignore_expires=True)
opener = getopener(cookie)


para_dct = {}
response = opener.open(baseurl+paramters)

temp_content = read(response)

viewstate = re.compile('id="__VIEWSTATE" value="(.*)"').search(temp_content).groups()[0]
eventvali = re.compile('id="__EVENTVALIDATION" value="(.*)"').search(temp_content).groups()[0]

para_dct['ddlxn'] = year+'-'+str(int(year)+1)
para_dct['ddlxq'] = term
para_dct['btn_cx'] = ' 查  询 '.decode('utf-8').encode('gbk')
para_dct['__EVENTTARGET'] = ''
para_dct['__EVENTARGUMENT'] = ''
para_dct['__LASTFOCUS'] = ''
para_dct['__VIEWSTATE'] = viewstate
para_dct['__EVENTVALIDATION'] = eventvali
para_data = urllib.urlencode(para_dct)

response = opener.open(baseurl+paramters, para_data)
content = read(response).decode('gbk').encode('utf-8')

print(content)
