#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-28 23:00:58
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：
"""
__author__ = '袁平华'

import os

# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
	name1 = 'Student'# 类属性

	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name #实例属性
	def __str__(self):
			return 'name = %s'% self.name  # 这里使用的是实例属性
	def __repr__(self):
		return 'name = %s '% self.name1 # 这里使用的是类型属性
	def __del__(self):
		print('%s  delloc'% self.__class__.__name__)
stu = Student('yuanph.org')
print(stu)
print(repr(stu))


class People(object):
	"""docstring for People"""
	country = "china"
	def __init__(self, age,country):
		super(People, self).__init__()
		self.age = age
		self.country= country
	
people = People(12,'HK')
print(people.age)#实例属性
print(people.country)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的country属性
print(People.country)#类型属性 但是类属性并未消失，用People.country仍然可以访问
del people.country #如果删除实例的country属性
print(people.country)#再次调用people.country，由于实例的country属性没有找到，类的country属性就显示出来了

