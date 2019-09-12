#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 12:12:49
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""


import os
import xlrd
import xdrlib,sys 
from biplist  import * 
# reload(sys)
# sys.setdefaultencoding("utf8")

def  open_excel(file):
	try:
		data = xlrd.open_workbook(file)
		return data 

	except Exception as e:
		print(e)

def  excel_table_byindex(file,columnindex,by_index =0):
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows
	ncols = table.ncols
	colname = table.row_values(columnindex)
	# print(colname)
	list  =[]
	for row_num in range(1,nrows):
		row = table.row_values(row_num)
		print(row)
		if row:
			app ={"code":'0x'+row[0],"type":0}
			list.append(app)
	packageDes ={"packageName":"emoji","packageImage":"chat_ic_emoji","type":0}
	return {"package":packageDes,"items":list} 


if __name__ == '__main__':
	list =  excel_table_byindex('/Users/yuanpinghua/Desktop/new project/emoj表情编码.xlsx',0)
	writePlist(list,"builtin_emoji.plist")
