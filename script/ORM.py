#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 15:13:06
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""一个简单ORM的实现

 [description]
"""
__author__ = '袁平华'

import os



class Field(object):

	"""docstring for Field"""

	def __init__(self, name, column_type):
		super(Field, self).__init__()
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

	"""docstring for StringField"""

	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')
		self.name = name


class IntegerField(Field):

	"""docstring for IntegerField"""

	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')
		self.name = name


class ModelMetaclass(type):

	"""docstring for ModelMetaclass"""
	def __new__(cls, name, bases, attrs):
		if name == 'model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model:%s' % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping :%s===>%s' % (k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
		attrs['__table__'] = name  # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

	"""docstring for Model"""

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
				try:
					return self[key]
				except Exception as e:
					raise AttributeError(r" 'model'  object has no attribute %s "%key)

	def __setattr__(self,key,value):
		self[key] = value 
		print('%s:%s'%(self,value))

	def save(self):
		fileds = []
		params = []
		args =[]
		for k,v in self.__mappings__.items():
			fileds.append(v.name)
			params.append('?')
			args.append((getattr(self,k,None)))
		sql = 'insert into %s (%s) values (%s)'%(self.__table__,','.join(fileds),','.join(params))
		print('SQL:%s'%sql)
		print('ARGS: %s'%str(args))

class  User(Model):
	"""docstring for  User"""
	# 定义类的属性到列的映射：
	id  = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')
user = User(id = 1234,name='jack',email='yuanpinghua@yeah.net',password='my-pwd')
user.save()
		

		
		
