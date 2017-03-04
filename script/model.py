#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-28 20:14:56
# @Author  :  袁平华 (yuanpinghua@yeah.net)
# @Link    :  yuanph.org 
# @Version :  1.0 

import os


"""作用域

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
正常的函数和变量名是公开的（public），可以被直接引用.
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
""" 
def __private1(name):
	print(name)

def __private2(name):
	"""私有方法
	
	不能在外部使用
	
	Arguments:
		name {[type]} -- [description]
	"""
	print(name)

def greeting(name):
	"""公开方法	
	
	[description]
	
	Arguments:
		name {[type]} -- [description]
	"""
	__private1(name)

if __name__ == '__main__':
	greeting('yuanph.org')



	