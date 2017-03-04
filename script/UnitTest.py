#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 19:19:07
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""

import unittest

class Dict(dict):
	"""docstring for Dict"""
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except Exception as e:
			raise AttributeError(r"'Dict' object has not attribute '%s'"%key)

	def __setattr__(self,key,value):
		self[key]= value 


"""编写单元测试

编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的

"""

class TestDict(unittest.TestCase):
	"""docstring for TestDict"""
	def test_init(self):
			d = Dict(a=1,b='test')
			self.assertEqual(d.a,1)
			self.assertEqual(d.b ,'test')
			self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key']= 'value'
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d =Dict()
		with self.assertRaises(AttributeError):
			value= d.empty

	"""[setUp与tearDown]
			可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
	"""
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')
		
		
#运行单元测试
# 1. 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
# if __name__ == '__main__':
#     unittest.main()

# 2. 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
# $ python3 -m unittest mydict_test
# 
# 
if __name__ == '__main__':
	import doctest
	"""
	Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

  doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。	
	"""
	doctest.testmod()
	doctest.DocTestRunner()
	# unittest.main()

"""小结

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

"""
		
