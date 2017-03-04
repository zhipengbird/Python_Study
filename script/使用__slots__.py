#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-28 23:32:59
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""使用__slots__
"""
__author__ = '袁平华'

import os
from types import MethodType
"""
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

"""
class Student(object):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
# 定义一个函数作为实例方法
	def set_age(self,age):
		self.age = age
	# 为了给所有实例都绑定方法，可以给class绑定方法：
	def set_score(self,score):
		self.score = score

stu = Student()
stu.name = 'yuanph.org' # 动态给实例绑定一个属性
# stu.set_age = MethodType(set_age,stu)
stu.set_age(10)
print(stu.age)
print(stu.name)
# Student.set_score= set_score
stu.set_score(100)
print(stu.score)


"""
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
"""
class Student1(object):
	"""docstring for Student1"""
	__slots__ =('name','age')#用tuple定义允许绑定的属性名称
	def __init__(self):
		super(Student1, self).__init__()

stud = Student1()
stud.name = 'yuanph'
stud.age = 100
stud.score=100 #AttributeError: 'Student1' object has no attribute 'score'
"""
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

"""

		

