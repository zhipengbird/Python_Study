#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-05 16:44:25
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""模块研究. 
提取模块的属性资料. 提示用户输入一个模块名(或者从命令行接受输入). 然后使用 dir() 和其它内建函数提取模块的属性, 显示它们的名字, 类型, 值.

"""


import importlib


def get_module_attr(module_name):
		module = importlib.import_module(module_name) 
		attrs = dir(module)
		res =[]
		for  attr in attrs:
			value = getattr(module,attr)
			res.append({'name':attr,'type':type(value),'value':value})
		return res 


if __name__ == '__main__':
	for attr in get_module_attr('sqlite3'):
		print('name:%s\t type:%s \t value: %s '%(attr['name'],attr['type'],attr['value']))
		pass




