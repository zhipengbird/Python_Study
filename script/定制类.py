#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 11:25:25
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""定制类

 [description]
"""
__author__ = '袁平华'

"""定制类

看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

"""

#__str__

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name


print(Student('mac')) # <__main__.Student object at 0x107551e10> 这种输出不美观 ，怎么才能让我们自己能看懂，又美观呢  只需要定义好__str__()方法

class Student1(object):
	"""docstring for Student1"""
	def __init__(self, name):
		super(Student1, self).__init__()
		self.name = name 

	def __str__(self):
		"""返回学生对象 可读性描述
		
		"""
		return '%s objct (name: %s)'%(self.__class__.__name__,self.name)


print(Student1('jack')) # Student1 objct (name: jack)
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：

""" 
 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串， 
 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
 
"""

class Student2(object):
	"""docstring for Student1"""
	def __init__(self, name):
		super(Student2, self).__init__()
		self.name = name 

	def __str__(self):
		"""返回学生对象 可读性描述
		
		"""
		return '%s objct (name: %s)'%(self.__class__.__name__,self.name)

	def __repr__(self):
		'返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的'
		return '%s objct (name: %s)'%(self.__class__.__name__,self.name)

	__repr__ =__str__ #这是一种简洁的写法，可以偷下懒哦


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#  
 
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		super(Fib, self).__init__()
		self.a,self.b = 0,1  #初始化两个计数器
	def __iter__(self):
		return self 

	def __next__(self):
		self.a,self.b = self.b ,self.a+self.b 
		if self.a >10000:
			raise StopIteration("超出预设值了")
		return self.a 
 
  #__getitem__  
  #__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
	def __getitem__(self,n):
		if isinstance(n ,int):
			for x in range(n):
				self.a,self.b =self.b,self.a+self.b
			return self.a 
		if isinstance(n ,slice):
			start = n.start 
			stop = n.stop 
			step = n.step 
			if  start is None:
				start = 0
			a, b = 0,1
			if step is None:
				step =1 
			L =[]

			for x in range(start,stop):
				if x>start:
					L.append(a)
				a,b = b,a+b 
			return L[start:stop:step] 

for x in Fib():
	print(x)

print(Fib()[10])
print(Fib()[:10])
print(Fib()[:10:2])

#__getattr__
# 常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Stu(object):
	"""docstring for Stu"""
	def __init__(self):
		super(Stu, self).__init__()
		self.name = 'jack'

	# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
	def __getattr__(self,attribute):
		return None 

		
print(Stu().name) #jack
print(Stu().age) #AttributeError: 'Stu' object has no attribute 'age'

		
# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path =''):
		super(Chain, self).__init__()
		self._path = path
		
	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path ,path ))

	def __str__(self):
		return self._path
	__repr__ =__str__ 

	def __del__(self):
		pass

print(Chain().status.user.timeline.list)


			
