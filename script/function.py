# -*- coding:utf-8 -*-

"""函数的使用

该文本主要记录函数的使用方式方法，及一些基本注意事项
"""


"""函数的定义

定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
1. 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
2. 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
3. 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
4. 函数内容以冒号起始，并且缩进。
5. return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""

def functionName(parameters):
		"""函数文档
		
		[函数的描述]
		
		Arguments:
			parameters {[type]} -- [description]
		"""
			# pass
		print(parameters)

#函数的调用
functionName('aa')



"""
可变(mutable)对象与不可变(immutable)对象
在python中 ,strings ,tuples ,和numbers 是不可变对象，list,dict等则是可变对象
不可变对象类型: 变量赋值 a = 5 后再典赋值 a = 10 这里实际是新生成一个int值对象10,再让a指向它,而5被放弃，不是改变a 的值
相当于新生成了a
可变类型： 变量赋值la =[1,2,3,5]后再赋值la[2]=20 则是将list la的第二个元素值更改，本身la没有动，只是内部的一部分值被修改了

"""
a =5
a = 'a'
print(a)
la =[1,2,3,5,6]
la[2]=10
print(la)



"""参数传递
python函数的参数传递：
 1. 不可变类型：类似C++的值传递 如整数，字符串 ，元组 如fun(a) 传递的只是a的值，没有影响a对象本身。在函数内部修改a的值，只是修改另一个复制的对象，不影响a 本身

 2. 可变类型： 	类似c++的引用传递，如列表，字典 如fun(la) 则是将la真正的传过去，在函数内部修改和在外部修改都会影响la对象本身
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

"""

def immutableVar(var):
		var +=1 
		print(var)

def mutableVar(la):
		la[0]= 1000

a = 100
immutableVar(a)
print(a)
a  = 90
print(a)
la = [100,20]
mutableVar(la)
print(la)


"""变量作用域

变量作用域
一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
1. 全局变量
2. 局部变量
全局变量和局部变量
1. 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
2.局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
"""





"""匿名函数
python 使用 lambda 来创建匿名函数。
1. lambda只是一个表达式，函数体比def简单很多。
2. lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3. lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
4. 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法： lambda [arg1 [,arg2,.....argn]]:expression
"""

sumf =lambda x,y:x+y
print(sumf(10,20))
print((lambda x,y:x-y)(100,200) )

print((lambda x:x**3)(3))
print((lambda y:y**2)(30))

"""filter函数使用
filter(function, sequence)
Arguments:
		function {[type]} -- [函数]
		sequence {[type]} -- [sequence]

对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple(取决于sequence类型）返回
"""

def filterList(la):
	return la % 2 != 0 and la %3!=0

list=filter(filterList,range(2,23))
print(list)

list = filter(lambda x :x%2!=0 and x%3!=0,range(10,20))
print(list)

"""map函数使用
map(function, sequence)

Arguments:
		function {[type]} -- [函数]
		sequence {[type]} -- [sequence]
对sequence中的item依次执行function（item），将执行结果组成一个List返回
另外map也支持多个sequence，当然这也要求function支持相应数量的参数输入

"""
def cube(x):
	return x**3

list = map(cube,range(2,8))
print(list)
print(map(lambda x:x**3,range(2,8)))


"""reduce

reduce（function，sequence，starting_value):
Arguments:
		function {[type]} -- [函数]
		sequence {[type]} -- [sequence]
		starting_value {[type]} --[初始值]
对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值
"""
def add(x,y):
	return x+y

list = reduce(add,range(1,10))
print(list)
print(reduce(add,range(1,10),20))

print(reduce(lambda x,y:x+y ,range(1,20)))











