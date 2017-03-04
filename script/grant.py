#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-28 20:44:19
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""访问限制

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
"""
__author__ = '袁平华'

import os

class Student:
	"""docstring for ClassName"""
	def __init__(self, name,age)	:
		self.name = name
		self.age = age
	def print_score(self):
		print('%s:%s'%(self.name,self.age))

stu = Student('yuanph',23)
stu.age = 100
stu.name='nfadsm'
stu.print_score()
"""
从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
"""
class Student2:
	"""docstring for Student"""
	def __init__(self, name,age):
		self.__name = name
		self.__age = age
	def print_score(self):
			print('%s:%s'%(self.__name,self.__age))

stu = Student2('yuanph',23)
stu.__age = 100
stu.__name='nfadsm'
#修改变量 没有效果
stu.print_score()


"""注意

需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
"""
BASE_PATH = os.path.abspath(os.path.dirname(__file__))

print(BASE_PATH)
print(__file__)
print(os.path.dirname(__file__))


