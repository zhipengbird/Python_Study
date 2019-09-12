#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-11 17:30:00
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""


import os
import json
import smtplib

def  findAssetsCar(baseroot):
	'''查找.xcarchive包里的.car文件
	
	[baseroot] 为包的路径
	
	Returns:
		[type] -- .car 文件路径
	'''
	for root,dirs,files in os.walk(baseroot):
			for file in files:
				if os.path.splitext(file)[1] =='.car':
					print( os.path.join(root,file))
					return os.path.join(root,file)
	return None

def assetProperty(carpath):
	'''使用xcrun工具生成图片资源的属性表	
	Arguments:
		carpath {[string]} -- [.car文件路径]
	'''
	jsonpath = os.path.join(os.getcwd(),'car.json')
	xrun_cmd = "xcrun --sdk iphoneos assetutil --info %s > %s "%(carpath,jsonpath)
	os.system(xrun_cmd)
	parseJson(jsonpath)
	


def parseJson(jsonpath):
		'''在图片资源属性表中检索出 'DisplayGamut': 'P3'的资水大白
		
		[description]
		
		Arguments:
			jsonpath {[type]} -- [description]
		'''
		with open(jsonpath,'r')as file:
			data = json.load(file)
		# print(data)
		result =[]
		for dic  in data:
				if  'DisplayGamut' in dic: 
							if dic['DisplayGamut'] =='P3':
								item ={"Name":dic['Name'],'DisplayGamut':dic['DisplayGamut'],'Encoding':dic['Encoding']}
								result.append(item)
		if len(result):
				print("count: %s"%(len(result)))
				print(result)
		jsonobj=  json.dumps(result)
		with open(jsonpath,'w') as file:
					file.write(jsonobj)

if __name__ == '__main__':
	carpath =  findAssetsCar(u'/Users/yuanpinghua/Downloads/Mask 2017-5-15 下午6.24.xcarchive')
	assetProperty(carpath)






	