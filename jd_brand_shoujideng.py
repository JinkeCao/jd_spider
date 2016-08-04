#-*- coding=utf-8 -*-
import cookielib
import string
import re
import BaseHTTPServer
import urlparse
import threading
import json
import md5
import datetime
import time
import os
import subprocess
import traceback
import thread
import pymongo
import hashlib
import requests
import urllib
import urllib2
import lxml.etree
import codecs
import math
import random

from time import sleep, ctime
from pymongo import MongoClient
from scrapy.http import Request, HtmlResponse
from scrapy.selector import HtmlXPathSelector

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Cookie":'ali_beacon_id=60.166.58.226.1439518952541.043431.3; cna=MrHcDcyVMwICATymOuKgF+Hg; ad_prefer="2015/10/23 16:25:19"; h_keys="%u516c%u53f8#%u62d6%u978b#%u8fde%u8863%u88d9#%u6fee%u9662%u6bdb%u8863#%u53a8%u536b%u6e05%u6d01#%u6c34%u6e29%u8868#%u6539%u6027PP#%u9970%u54c1%u5305%u88c5#%u5316%u5986%u54c1%u5305%u88c5"; ali_ab=60.166.58.226.1443419385082.8; JSESSIONID=8L78OIqv1-KB3V0cqe4U0AuUkUPA-nPuE4bP-Mva4; _csrf_token=1453965463188; _tmp_ck_0="AhAPwLGenDsU2obBvfytDvRiqpy%2BXWtFsW%2BYE6YrWj7%2FLNbrXYNIv9QOYZ1ZEwQbqXy22POB9BOQ%2FhhLcDygQqRZEvxiBUSc7Rpn5VJYsqLXdi%2FtML88giCdejVQSxg7JT%2FrY9z%2F7fjE%2BI3Gx%2BHW7v5lKBobuZNmM0%2BBrjei4cCNapl6KS0GupffhfKI5SxY%2F%2BLjIZg46uY2Ybm33SpV6qlJJpHwm3gpf%2BLxdl0A0bkcIhE2vfJPK2CzoNPqeQNnGAL%2B4FMUABsAH1TzTvi2WNj1bwCHQvdKndmmVR0URvN3pHzUlWBzSlZ%2BrkzQPBKz5mGMrbAqBiw5ckgRmUu9aw%3D%3D"; alicnweb=touch_tb_at%3D1453965493517; _ITBU_IS_FIRST_VISITED_=n; l=AoCAfkiuGy0CK72IiKcqIhqc0ARSCWTT; isg=1E3BFCA0DD17E68312F81EED656890FE',
	"Host":"s.1688.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safar"
}

if __name__ == "__main__":
	
	print 'start'

	fsr=open("jdgrade3list_shoujideng.txt","r")
	fsw=open("jdgrade4list_shoujideng.txt","a+")
	lines=fsr.readlines()
	print len(lines)
	
	# 家用电器	大家电 电视影音	家电配件	http://list.jd.com/737-794-877-0-0-0-0-0-0-0-1-1-1-1-1-72-4137-33.html
	for line in lines:
		#try:
		linearr=line.split("\t")
		grade1=linearr[0].strip()
		grade2=linearr[1].strip()
		grade3=linearr[2].strip()
		url=linearr[3].strip('\n')
		print url
		body=requests.get(url,timeout=15).text
	
		#response = HtmlResponse(url=url, body=body, encoding='utf8')
		#hxs = HtmlXPathSelector(response)
		#body_next = ''.join(hxs.select('//div[@class="sl-v-logos"]|//div[@class="sl-v-list"]/ul/li//a/@href').extract())
		#print 'body_next:',body_next

		#response_next = HtmlResponse(url=url, body=body_next, encoding='utf8')
		#hxs_next = HtmlXPathSelector(response_next)
		#links = hxs_next.select('//ul//li//a//text()').extract()
		#links = hxs_next.select('//ul//li//a/@href').extract()
		#for link in links:
		#	print 'brand:',link
		#	url1 = 'http://list.jd.com'+link
		#	fsw.write(grade1+"\t"+grade2+"\t"+grade3+"\t"+grade4+"\t"+url1+"\n")

		# scrapy shell 'http://list.jd.com/737-794-877-0-0-0-0-0-0-0-1-1-1-1-1-72-4137-33.html'
		# hxs.select('//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div[@class="J_selectorLine s-brand"]/div/div[@class="sl-value"]/div[@class="sl-v-logos"]/ul[@class="J_valueList v-fixed"]/li/a|//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div[@class="J_selectorLine s-brand"]/div/div[@class="sl-value"]/div[@class="sl-v-list"]/ul[@class="J_valueList"]/li/a|//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div[@class="J_selectorLine s-brand"]/div/div[@class="sl-value"]/div[@class="sl-v-list"]/ul[@class="J_valueList v-fixed"]/li/a').extract()

		doc=lxml.etree.HTML(body)
		#info_list=doc.xpath('//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div/div/div[@class="sl-value"]/div[@class="sl-v-logos"]/ul[@class="J_valueList v-fixed"]/li/a')
		info_list=doc.xpath('//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div[@class="J_selectorLine s-brand"]/div/div[@class="sl-value"]/div[@class="sl-v-logos"]/ul[@class="J_valueList v-fixed"]/li/a|//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div[@class="J_selectorLine s-brand"]/div/div[@class="sl-value"]/div[@class="sl-v-list"]/ul[@class="J_valueList"]/li/a|//div[@id="J_searchWrap"]/div[@class="container"]/div[@class="selector"]/div[@class="J_selectorLine s-brand"]/div/div[@class="sl-value"]/div[@class="sl-v-list"]/ul[@class="J_valueList v-fixed"]/li/a')
		print len(info_list)
		if len(info_list)>0:
			for info in info_list:
				#link = info.xpath('.//@href')[0]
				link = info.xpath('.//@href')[0]
				txtbrand = info.xpath('.//@title')[0]

				url1 =''
				if len(re.findall("search",url))>0:
					url1 = 'http://search.jd.com/'+link
				else:
					url1 = 'http://list.jd.com'+link 
				print url1
				# print grade2

				fsw.write(grade1+"\t"+grade2+"\t"+grade3+"\t"+txtbrand+"\t"+url1+"\n")
		
		# 暂停下载
		time.sleep(random.randint(30, 150))
		#except:
		#	print 'error'

	print 'end'