# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib
import re
import HTMLParser
from bs4 import *
from PIL import Image
import csv
import sys  
import codecs


mainUrl = 'http://sztz.gdufe.edu.cn/sztz/publicity/'
L = []
mySet = set(L)
page = 1

class crowInformation(object):
	def __init__(self):
		cj = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		urllib2.install_opener(self.opener)

	def usernamePass(self):
		self.username = raw_input("please enter usernmae: ")
		self.password = raw_input('please enter password: ')

	def login(self):
		imgUrl = "http://my.gdufe.edu.cn/captchaGenerate.portal?s=0.3961200918366401"
		img = self.opener.open(imgUrl).read()
		localImg = open('e:/image.jpg', 'wb')
		localImg.write(img)
		localImg.close()
		im = Image.open('e:/image.jpg')
		im.show()
		imgCheck = raw_input("please input CheckCode:")
		self.data = urllib.urlencode({
		    "Login.Token1":self.username,
		    "Login.Token2":self.password,
		    "captchaField":imgCheck,
		    "goto":"http://my.gdufe.edu.cn/loginSuccess.portal",
		    "gotoOnFail":"http://my.gdufe.edu.cn/loginFailure.portal"
		})
		self.header = {
		    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36",
		    "Referer":"http://my.gdufe.edu.cn/index.portal"
		}
		postUrl  = "http://my.gdufe.edu.cn/userPasswordValidate.portal"
		request = urllib2.Request(postUrl, self.data, self.header)
		response = self.opener.open(request)
		if response.getcode() == 200:
			print '\n' + 'login sucessful' + '\n'
		else:
			print '\n' + 'login unsucessful' + '\n'

	def start(self):
		global page
		print 'Begin to crow, please wait' + '\n'
		while(page < 2):
			print 'The ' + str(page) + ' page'
			data = urllib.urlencode({
			    'conditionSelector':'departmentSpan',
			    'departmentId':'',
			    'specialtyId':'',
			    'grade':'2016',
			    'naturalClassId':'0',
			    'hasComplaint':'-1',
			    'search':'%e6%9f%a5%e8%af%a2', #&#x67E5;&#x8BE2;
			    'listTableClass':'HiddenList',
			    'itemPerPage':'30',
			    'currentPage':page,
			    'sort.sortColumn':'participant.studentId',
			    'sort.ascending':'true'
			})
			header = {
			    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36",
			    "Referer":'http://sztz.gdufe.edu.cn/sztz/publicity/studentList.jsp'
			}
			postUrl  = "http://sztz.gdufe.edu.cn/sztz/publicity/studentList.jsp"
			request = urllib2.Request(postUrl, data, header)
			response = self.opener.open(request)
			html_doc = response.read()
			page = page+1
			soup = BeautifulSoup(
			    html_doc,
			    "html.parser",
			    from_encoding = 'utf-8'
			)

			links = soup.find_all(name = 'a', attrs = {'href':re.compile(r'itemParticipantId=')})
			for link in links:
				newUrl = mainUrl + link['href']
				response1 = urllib2.urlopen(newUrl)
				html_doc = response1.read()
				soup = BeautifulSoup(
					    html_doc,
					    "html.parser",
					    from_encoding = 'utf-8'
					)
				linkss = soup.find_all(name = 'td', attrs = {'colspan':"3", 'class':"tittle3"})

				for linkk in linkss:
					if not linkk.a:
						if len(linkk) == 1:
							s = linkk.get_text().encode('gbk', 'ignore')
							s = str(s)
							s = s.split()
							s = str(s)
							s = s.replace("', '", ' ')
							s = s[2:-2]
							s = s.encode('gbk').decode('string_escape')
							mySet.add(s)		





if __name__ == '__main__':
	crow = crowInformation()
 	crow.usernamePass()
 	crow.login()
 	crow.start()
	with open('2016xinxi.txt', 'w') as w:
		for i in mySet:
			i = str(i)
			if(i.find('2016') >= 0 ):
				if(len(i) < 150):
					w.write(i+'\n')
	 







