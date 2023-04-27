# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: softwareReviewSpider
@file   : spiderUtils.py
@version: 1.0
@time   : 2018-03-15
@author : Jianzhang Zhang, <jianzhang.zhang@foxmail.com>
"""

import json
import time
import random
import urllib
import requests
from fileUtils import jiema
from bs4 import BeautifulSoup


def revertShortLink(longUrl):
	'''
	将长网址恢复短网址, 其实requests可以直接请求短网址
	:param longUrl:
	:return:
	'''
	res = requests.head(longUrl)
	return res.headers.get('location')


def getShortUrl(longUrl):
	'''
	调用短网址服务
	:param longUrl: 长URL
	:return: 短URL
	'''
	params = urllib.urlencode({'url': longUrl})
	response = requests.post("http://suo.im/front/index/urlCreate/", data=params,
	                         headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
	resultDict = response.json()
	if resultDict.get("status") == 1:
		return resultDict.get("list")
	else:
		return ""
	
def getElementText(element):
	if element:
		return element.text.strip()
	else:
		return ""

def getJson(url):
	jsonStr = requests.get(url).content
	rankDict = json.loads(jsonStr)
	return rankDict


def getSoup(url, parser="html.parser"):
	while True:
		try:
			html = requests.get(url).content
			soup = BeautifulSoup(html, parser)
			break
		except requests.exceptions.SSLError:
			time.sleep(random.randint(0,2)+random.random())
			continue
		except requests.exceptions.ConnectionError:
			time.sleep(random.randint(0,2)+random.random())
			continue
	return soup


# 将"亿"和"万"转换为阿拉伯数字
def strNumToIntNum(strNum):
	if u"\u4ebf" in strNum:
		return float(strNum.replace(u"\u4ebf", "")) * 100000000
	elif u'\u4e07' in strNum:
		return float(strNum.replace(u'\u4e07', "")) * 10000
	else:
		return strNum


def getWeekday(dateStr):
	weekdayDict = {
		0: jiema('星期一'),
		1: jiema('星期二'),
		2: jiema('星期三'),
		3: jiema('星期四'),
		4: jiema('星期五'),
		5: jiema('星期六'),
		6: jiema('星期日'),
	}
	timeStringFormat = "%Y-%m-%d"
	timeArray = time.strptime(dateStr, timeStringFormat)
	return weekdayDict[timeArray.tm_wday]

