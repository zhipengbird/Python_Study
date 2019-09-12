#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-13 21:28:42
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""


import urllib2.request

import os
import time
import sys
import re


def getHtml(url):
	"""获取网页
		Arguments:
		url {[type]} -- [description]

	Returns:
		[type] -- [html]
	"""
	headers = {
	'Referer': 'http://www.qiushibaike.com/pic/',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'

	}
	page = urllib.request.build_opener()
	page.addheaders = [headers]
	html = page.open(url)
	return html


def getimg(html):
	""" 获取图片地址"""
	reg = r'<img src ="(.+?.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	print(imglist)
	return imglist


def download(num, block, total):

  per = 100.0 * num * block / total

  if per > 100:
  	per = 100.0
  if num * block > total:
  	a = total
  else:
  	a = num * block

  if total < 1024 * 1024:
        sys.stdout.write('%.2f/%.2f(KB)  %.2f%%\r' %
                         (a / 1024, total / 1024, per))
  else:
        sys.stdout.write('%.2f/%.2f(MB)  %.2f%%\r' %
                         (a / 1024 / 1024, total / 1024 / 1024, per))
  sys.stdout.flush()
  print('')  # 不能删掉，防止下载进度的百分比被遮盖


def get_file(url):
	html = getHtml(url)
	print(html)
	try:
		html = html.decode('utf-8')
	except Exception as e:
		html = html.decode('gbk')

	imglist = getimg(html)
	dirname = 'spider_img'
	path.os.path.join(os.getcwd(), dirname)
	if not os.path.exists(path):
		os.mkdir(dirname)
	os.chdir(path)
	n = 1
	for imagurl in imglist:
		t = time.strftime('%m-%d_%H-%M-%S')
		filename = '%s_%s' % (t, n)
		try:
			urllib.request.urlretrieve(imagurl, filename, download)
			n += 1
		except Exception as e:
			print(e)
	 # print('保存文件：%s 张' % len(imglist))
   #  print('保存目录：%s' % path)
   # 窗口关闭时间
  # window_close_time = 5
  # print('>>> 脚本 %s s后自动关闭' % window_close_time)
  # time.sleep(window_close_time)



if __name__ == '__main__':
	url ="http://www.qiushibaike.com/imgrank/"
	get_file(url)

  	
  		 






