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
	for root,dirs,files in os.walk(baseroot):
			for file in files:
				if os.path.splitext(file)[1] =='.car':
					print( os.path.join(root,file))
					return os.path.join(root,file)
	return None

def assetProperty(carpath):
	jsonpath = os.path.join(os.getcwd(),'car.json')
	xrun_cmd = "xcrun --sdk iphoneos assetutil --info %s > %s "%(carpath,jsonpath)
	os.system(xrun_cmd)
	parseJson(jsonpath)
	


def parseJson(jsonpath):
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

def function():
		pass

if __name__ == '__main__':
	carpath =  findAssetsCar(u'/Users/yuanpinghua/Desktop/2017-05-20-04-37/archive/Mask.xcarchive')
	assetProperty(carpath)