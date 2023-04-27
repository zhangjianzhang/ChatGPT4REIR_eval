# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: wechatClustering
@file   : logUtils.py
@version: 1.0
@time   : 2018-01-14
@author : Jianzhang Zhang, <jianzhang.zhang@foxmail.com>
"""



def getLogger(loggerName,logFile=None):
	import logging
	import sys
	# 创建一个日志器logger并设置其日志级别为DEBUG
	logger = logging.getLogger(loggerName)
	logger.setLevel(logging.DEBUG)
	# 创建一个流处理器handler并设置其日志级别为DEBUG
	if logFile:
		handler = logging.FileHandler(logFile)
	else:
		handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	# 创建一个格式器formatter并将其添加到处理器handler
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	handler.setFormatter(formatter)
	# 为日志器logger添加上面创建的处理器handler
	logger.addHandler(handler)
	return logger