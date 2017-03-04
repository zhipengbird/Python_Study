#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 14:48:28
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""使用元类

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

"""
__author__ = '袁平华'

import os

class Hello(object):
	"""docstring for Hello"""
	def __init__(self):
		super(Hello, self).__init__()
	def hello(self,name = 'word '):
		print('Hello ,%s'%name )

Hello().hello()
print(type(Hello)) #<class 'type'>
print(type(Hello()))
#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

def fn(self,name ='word'):
	print('hi .%s'%name)

Hi =type('Hi',(object,),dict(hi=fn))
h = Hi()
h.hi()
print(type(h))
print(type(Hi))

"""使用type()函数创建class对象
要创建一个class对象，type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
"""


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	"""docstring for ListMetaclass"""
	def __new__(cls, name,bases,attrs):
		attrs['add']=lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)


"""__new__()方法接收到的参数依次是：

1. 当前准备创建的类的对象；

2. 类的名字；

3. 类继承的父类集合；

4. 类的方法集合。

[description]
"""


class Mylist(list,metaclass = ListMetaclass):
	"""docstring for Mylist"""
	def __init__(self):
		super(Mylist, self).__init__()
		
		
L  = Mylist()
L.add(1)
print(L)



