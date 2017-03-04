
# -*- coding:utf-8 -*-


import  os

"""
Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，
						如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""


class Employee:
	"""所有员工的其类"""
	empcount =0

	"""初始化方法
	__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
	"""
	def __init__(self,name ,salary):
		self.name = name
		self.salary = salary
		self.empcount+=1

	
	def displayCount(self):
		"""显示员工个数
		
		self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
		类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

		"""
		print('Total Employee count %d'% Employee.empcount)


	def displayEmployee(self):
		"""显示员工信息

		员工基本信息的显示
		"""
		print('name:'+self.name + '\t salary:'+self.salary)


	def __del__(self):
		"""析构方法

		析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
		"""
		classname = self.__class__.__name__
		print('%s 销毁了'% classname)


emp = Employee('yuanp','12k')
emp.displayCount()
emp.displayEmployee()
print(emp.__doc__)
# print(emp.__name__)
print(emp.__module__)
# print(emp.__bases__)
print(emp.__dict__)

"""访问属性

你也可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。

"""

print(getattr(emp,'name'))
print(hasattr(emp,'age'))
print(setattr(emp,'age',20))
print(hasattr(emp,'age'))
print(delattr(emp,'age'))
print(hasattr(emp,'age'))
emp.displayEmployee()

class Manager(Employee):
	"""
	
	Extends:
		Employee

	"""
	members =[]
	def __init__(self, name,salary):
		Employee.__init__(self,name,salary)
		# super(Manager,self).__init__(self,name,salary)
		

	def managerEmploy(self):
		"""管理员工
		
		[对员工进行管理]
		"""
		print('手下有%d员工'%(len(self.members)))

	def addEmploy(self,emp):
		"""增加手下员工
		"""
		self.members.append(emp)


emp1 = Employee('jack','13k')
emp2 = Employee('tom','20k')

manager = Manager('jackson','45')

manager.addEmploy(emp1)
manager.addEmploy(emp2)
manager.addEmploy(emp)
manager.managerEmploy()


"""基础重载方法

序号			方法, 描述 & 简单的调用
1				__init__ ( self [,args...] )
				构造函数
				简单的调用方法: obj = className(args)

2				__del__( self )
				析构方法, 删除一个对象
				简单的调用方法 : dell obj

3				__repr__( self )
				转化为供解释器读取的形式
				简单的调用方法 : repr(obj)

4				__str__( self )
				用于将值转化为适于人阅读的形式
				简单的调用方法 : str(obj)

5				__cmp__ ( self, x )
				对象比较
				简单的调用方法 : cmp(obj, x)
"""	

class Vector:
	"""docstring for Vector"""
	def __init__(self, a,b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d,%d)'%(self.a,self.b)

	"""运算符重载
	
	python 支持运算符的重载
	"""
	def __add__(self,other):
		"""重载向量的加法
		
		两个向量相加
		
		Arguments:
			other {向量对象} -- 向量的实例
		
		Returns:
			向量实例 -- 一个新的向量实例
		"""
		return Vector(self.a+other.a,self.b+other.b)

	def __del__(self):
		classname = self.__class__.__name__
		print('%s 销毁了'% classname)

vv = Vector(10,20)
vs = Vector(-10,20)
print(vv+vs)
		

"""类的属性与方法

类属性与方法
类的私有属性
		__private_attrs：
		两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 
							self.__private_attrs。
类的方法
		在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
类的私有方法
	__private_method：
	两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
"""


class People:
	"""docstring for People"""
	__desposit = 10000 # 私有变量 存款
	nationality ='china' #公开变量 国藉
	def __init__(self, name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
	

	def __str__(self):
		return 'Name:%s \t Country:%s \t Age:%d \t Sex:%s'%(self.name,self.nationality,self.age,self.sex)

jack = People('jack',20,'Man')
jack.nationality= "America"

print(jack)
# print(jack.__desposit) 实例不能访问私有变量
print(jack._People__desposit) # 通过这种方法可以获取到私有变量 格式为：'object._+类名+__+私有变量名'


		






