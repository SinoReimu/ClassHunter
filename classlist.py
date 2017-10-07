#!/usr/bin/python
#coding=utf-8

import cookielib
import re
import sys
import urllib
from util import read, getopener, align

# get argument 

if len(sys.argv) < 3:
	print('usage:python classlist.py [name] [student code]')
	sys.exit(0)
else:
	name = sys.argv[1]
	code = sys.argv[2]


baseurl = 'http://jxgl.hdu.edu.cn/xf_xsqxxxk.aspx?'

# init my opener
paramters = urllib.urlencode({
						'xh': code, 
						'xm': name.decode('utf-8').encode('gbk'),
						'gnmkdm': 'N121113'})
cookiename = 'cookie.dat'
cookie = cookielib.MozillaCookieJar(cookiename)
cookie.load(cookiename, ignore_discard=True, ignore_expires=True)
opener = getopener(cookie)

para_dct = {}
response = opener.open(baseurl+paramters)

temp_content = read(response)

viewstate = re.compile('id="__VIEWSTATE" value="(.*)"').search(temp_content).groups()[0]
eventvali = re.compile('id="__EVENTVALIDATION" value="(.*)"').search(temp_content).groups()[0]

para_dct['ddl_kcxz'] = ''
para_dct['ddl_ywyl'] = ''
para_dct['ddl_kcgs'] = ''
para_dct['ddl_xqbs'] = '1'
para_dct['ddl_sksj'] = ''
para_dct['TextBox1'] = ''
para_dct['Button2'] = '确定'.decode('utf-8').encode('gbk') #confirm
para_dct['txtYz'] = ''
para_dct['hidXNXQ'] = '2017-20181'
para_dct['__EVENTTARGET'] = 'ddl_ywyl'
para_dct['__EVENTARGUMENT'] = ''
para_dct['__LASTFOCUS'] = ''
para_dct['__VIEWSTATE'] = viewstate
para_dct['__EVENTVALIDATION'] = eventvali
para_data = urllib.urlencode(para_dct)

response = opener.open(baseurl+paramters, para_data)
content = read(response).decode('gbk').encode('utf-8')

classes = re.compile('(<tr[\s\S]*?<\/tr>)').findall(content)
regnum = re.compile('kcmcGrid_ctl(\d+)')
regname = re.compile('target=\'_blank\'>(.*?)<\/a>')
reginfo = re.compile('<td>(.*?)<\/td>')

for i in range(1, len(classes)-1):
	sclass = classes[i]
	codeg=regnum.findall(sclass)
	if codeg:
		code=codeg[0]
	else:
		break
	group1=regname.findall(sclass)
	name=group1[0]
	teacher=group1[1]
	group2=reginfo.findall(sclass)
	print(align(code, 4) + align(name, 35) + align(teacher, 18) +
			align(group2[4], 20) + align(group2[5], 5) + align(group2[6], 10) +
			align(group2[7], 7) + group2[9] + '/' + group2[8] )

