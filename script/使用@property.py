#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 09:58:46
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""使用@property

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
"""
__author__ = '袁平华'

import os

# property属性 使用方式一
class Student(object):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
	def getscore(self):
		return self._score

	def setscore(self,value):
		if not  isinstance(value,int):
			raise ValueError('score must be an integer')
		if value<0 or value>100:		
			raise ValueError('score must between 0~100')
		self._score = value
	def delScore(self):
		del self._score

	"""property
	property 可以将Python定义的函数“当做”属性访问，从而提供更加友好访问方式，但是有时候setter/getter也是需要的
	property是一个类，property(fget=None, fset=None, fdel=None, doc=None)用来定义一个property属性。
	1. fget是一个用于获取属性值时执行的方法，
	2. fset是用于设置属性值时执行的方法，
	3. fdel是用于删除属性值时执行的方法。
	4. doc是属性的描述

	"""
	score = property(getscore, setscore, delScore, '''__doc__''') #定义一个score属性

stu = Student()
try:
	stu.score= -100
except Exception as e:
	print(e)
else:
	pass
finally:
	pass





# property 属性使用方式2
class Son(object):
	"""docstring for Son"""
	def __init__(self):
		super(Son, self).__init__()
		self.__x = None
	@property 
	def x(self):
		return self.__x

	@x.setter
	def x(self,value):
		self.__x = value 

	@x.deleter 
	def x(self):
			del self.__x	

"""
在修饰器用法里，同一属性的三个函数名要相同
"""
son = Son()
son.x=100



"""
Python Descriptor是这样一个对象
它按照descriptor协议, 有这样的属性之一

def __get__(self, obj, type=None)  #  会返回一个value
def __set__(self, obj, value)   # 返回None
def __delete__(self, obj)  # 返回None
这样的对象就是一个descriptor

"""

"""
descriptor的特性

假若有一个对象t, 我们去引用它的一个属性a

t.a
但是发现a是一个descriptor

那么不会返回a, 而是会去调用a相应的__get__, __set__, __delete__

那么什么情况调用那个呢?如下
v = t.a   <---->   v = __get__(a, t)
t.a = v   <----->  __set__(a, t, v)
del t.a   <----->  __delete__(a, t)


Property对象是Descriptor
Property.setter 和 Property.deleter 都是装饰器,他们和property一样,都是返回Property()对象,
不同的是 @property设置 fget ,  setter和 deleter分别设置 fset, 和 fdel
"""

"""
参考文章： http://www.cnblogs.com/livingintruth/p/3601861.html
"""


class Property(object):
	"""docstring for Property"""
	def __init__(self, fget =None,fset =None,fdel =None,doc=None):
		super(Property, self).__init__()
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		if doc is None and fget is not  None:
			doc= fget.__doc__
		self.__doc__ = doc

	def __get__(self,obj,objtype =None):
		if obj is None:
			return self 
		if self.fget is None:
			raise AttributeError('unreadable attribute ')

		return self.fget(obj)

	def __set__(self,obj,value):
		if self.fset is None:
			raise AttributeError("can't set attribute")
		self.fset(obj,value)

	def __delete__(self,obj):
		if self.fdel is None:
			raise AttributeError("can't delete attribute")
		self.fdel(obj)

	def getter(self,fget):
		return type(self)(self.fget,self.fset,self.fdel,self.__doc__)

	def setter(self,fset ):
		return type(self)(self.fget,self.fset,self.fdel,self.__doc__)

	def deleter(self,fdel):
		return type(self)(self.fget,self.fset,self.fdel,self.__doc__)



class screen(object):
		"""docstring for screen"""
		def __init__(self):
			super(screen, self).__init__()
		
		def getwidth(self):
			return self.__width

		def setwidth(self,value):
			if not isinstance(value, int):
				raise ValueError("width must be integer")
			if value< 0 :
				raise ValueError("width must be greater than zero ")
			self.__width = value 

		def getheigth(self):
			return self.__height

		def setheigth(self,value):
			if not isinstance(value, int):
				raise ValueError("height must be integer")
			if value< 0 :
				raise ValueError("height must be greater than zero ")
			self.__height = value 

		
		def  getresolution(self):
				return self.__width*self.__height

		width = property(getwidth, setwidth )
		height = property(getheigth, setheigth)

		resolution = property(getresolution)

UI = screen()
UI.width = 1024
UI.height = 1980
print(UI.resolution)






			
		
			