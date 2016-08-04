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

from scrapy.http import Request, HtmlResponse
from scrapy.selector import HtmlXPathSelector
from time import sleep, ctime
from pymongo import MongoClient

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
	#try: 
	fsr=open("jdgrade4list_shoujideng.txt","r")
	fsw=open("jdgrade5list_shoujideng.txt","a+")
	lines=fsr.readlines() 
	print len(lines)

	# 电脑	电脑整机	笔记本	联想（Lenovo）	http://list.jd.com/list.html?cat=670,671,672&ev=%40exbrand%5F11516&go=0&JL=3_品牌_联想（Lenovo） 
	for line in lines:
		linearr=line.split("\t")
		grade1=linearr[0].strip()
		grade2=linearr[1].strip()
		grade3=linearr[2].strip()
		txtbrand=linearr[3].strip()
		url =linearr[4].strip('\n')
		body=requests.get(url,timeout=15).text
		doc=lxml.etree.HTML(body)

		info_list=doc.xpath('//div[@class="gl-i-wrap j-sku-item"]/div[@class="p-name"]|//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]')
		print len(info_list)
		if len(info_list)>0:
			for info in info_list:
				link = info.xpath('.//@href')[0]
				#print link
			
				txtname = ""
				txtname = txtname.join(info.xpath('.//em/text()'))
				print txtname

				#http://item.jd.com/958912.html
				#http://p.3.cn/prices/mgets?type=1&skuIds=J_958912

				#link1 = re.findall("\d+",link)[0]
				#url1 = 'http://p.3.cn/prices/mgets?type=1&skuIds=J_'+link1
				#time.sleep(random.randint(120, 180)) 
				#print url1

				#strbody1=requests.get(url1,timeout=15).text
				#str = strbody1.replace('[','') # 将字符串里的[全部替换为''
				#str = str.replace(']','') # 将字符串里的]全部替换为''

				#json string:
				#s = json.loads(str)
				#print s
				#print s.keys()
				#print s["p"]

				fsw.write(grade1+"\t"+grade2+"\t"+grade3+"\t"+txtbrand+"\t"+txtname+"\n")
		time.sleep(random.randint(30, 100))
	#except:
	#	print 'error'

	print 'end'

