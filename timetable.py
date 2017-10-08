#!/usr/bin/python

import cookielib
import re
import sys
import urllib
from util import read, getopener

# get argument 

if len(sys.argv) < 4:
	print('usage:python timetable.py [current/history] [name] [student code] ([year] [term(1,2,3)] if history)')
	sys.exit(0)
else:
	name = sys.argv[2]
	code = sys.argv[3]
	if sys.argv[1] == 'history':
		if len(sys.argv) < 6:
			print('usage:python timetable.py [now/history] [name] [student code] ([year] [term(1,2,3)] if history)')
			sys.exit(0)
		else:	
			year = sys.argv[4]
			term = sys.argv[5]

baseurl = 'http://jxgl.hdu.edu.cn/xskbcx.aspx?'

# init my opener
paramters = urllib.urlencode({
						'xh': code, 
						'xm': name.decode('utf-8').encode('gbk'),
						'gnmkdm': 'N121603'})
cookiename = 'cookie.dat'
cookie = cookielib.MozillaCookieJar(cookiename)
cookie.load(cookiename, ignore_discard=True, ignore_expires=True)
opener = getopener(cookie)


para_dct = {}
response = opener.open(baseurl+paramters)

temp_content = read(response)

if sys.argv[1] == 'history':
	viewstate = re.compile('id="__VIEWSTATE" value="(.*)"').search(temp_content).groups()[0]
	eventvali = re.compile('id="__EVENTVALIDATION" value="(.*)"').search(temp_content).groups()[0]

	para_dct['xnd'] = year+'-'+str(int(year)+1)
	para_dct['xqd'] = term
	para_dct['__EVENTTARGET'] = 'xnd'
	para_dct['__EVENTARGUMENT'] = ''
	para_dct['__LASTFOCUS'] = ''
	para_dct['__VIEWSTATE'] = viewstate
	para_dct['__EVENTVALIDATION'] = eventvali
	para_data = urllib.urlencode(para_dct)

	response = opener.open(baseurl+paramters, para_data)
	content = read(response).decode('gbk').encode('utf-8')
else:
	content = temp_content.decode('gbk').encode('utf-8')
	
classes = re.compile('<td align="center".*?>(.*?)<\/td>').findall(content)

for i in range(len(classes)-1, -1, -1):
    if not '<br>' in classes[i]:
	classes.pop(i)

for item in classes:
    print(item.replace('<br>', ' '))

