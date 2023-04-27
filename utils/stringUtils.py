#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
from .zhuanma import strdecode


def jiema(string):
	
	return strdecode(string)


def filterReturnChar(string):
	
	return string.replace("\r", "")


def encodeUTF8(string):
	
	return jiema(string).encode("utf-8")


def filterCChar(string):
	
	hanzi = re.compile(u"[\u4e00-\u9fa5]+", re.U)
	return "".join(re.findall(hanzi, string))
