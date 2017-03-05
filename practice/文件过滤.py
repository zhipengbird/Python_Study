#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-05 15:41:41
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""文件过滤

显示一个文件的所有行 ，忽略以#开头的行，这个字符被用做Python,perl,tcl等脚本的注释符
附： 处理不是第一个字符开头的注释
"""
import os


def filtrationFileContent(filepath):
		try:
			with open(filepath,'r') as fileobj:
				for eachline in fileobj:
					if '#' in eachline:
						 """
						 如果该行是注释，则全部不显示
						 如果只是部分注释，则除注释外部分显示出来(#后面的为注释)

						 """
						 # 去除空格
						 # eachline = eachline.strip()
						 index  = eachline.rfind('#')
						 if index !=0:
						 		print(eachline[:index])
						 
					else:
						pass
						print(eachline)
					

		except Exception as e:
			print(e)


def outputFileforwardLines(filepath,lines):
		"""读取文件的前几行
		
		
		
		Arguments:
			filepath {[string]} -- 文件路径
			lines {int} -- [description]
		
		Raises:
			e -- [description]
		"""
		try:
			with open(filepath,'r') as file:
				for eachline in file:
					if lines:
						lines-=1
						print(eachline)
					else:
						break
					
		except Exception as e:
			print(e)

def fileLines(filepath):
		"""读取文件的行数



		Arguments:
			filepath {[string]} -- 文件路径

		Raises:
			e -- [description]
		"""
		try:
			lines=0
			with open(filepath,'r') as file:
				for eachline in file:
					lines+=1 

			print("this file:'%s' has '%s' lines "%(filepath,lines))

		except Exception as e:
			raise e


def fileLines2(filepath):
	"""读取文件的行数
	
	
	
	Arguments:
		filepath {[string]} -- 文件路径
	
	Raises:
		e -- [description]
	"""
	try:
		with open(filepath,'r') as file:
			lines = file.readlines()
			print("this file:'%s' has '%s' lines "%(filepath,len(lines)))
	except Exception as e:
		raise e

if __name__ == '__main__':
	# filtrationFileContent('../script/findFile.py')
	# outputFileforwardLines('../script/findFile.py',4)
	fileLines2('../script/findFile.py')
