# -*- coding:utf-8 -*-

"""生成器

在Python中，这种一边循环一边计算的机制，称为生成器：generator。

""" 


'''要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：'''

L = [x * x for x in range(10)] #列表
print(L)
G = (x*x for x in range(10)) # 生成器
print(G) #<generator object <genexpr> at 0x10a976c30>

print(next(G))
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。


# 不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
# 
for x in G:
 	print(x) 


"""
		
创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
"""
def fib(max):
	"""斐波拉契数列（Fibonacci
	
		除第一个和第二个数外，任意一个数都可由前两个数相加得到：

		1, 1, 2, 3, 5, 8, 13, 21, 34, ...
	
	Arguments:
		max {[数值]} -- [最大第几个数值]
	"""
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b = b,a+b 
		n= n+1
	return'done'

fib(10)


'''仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了

'''

def fibGenerator(max):
	n,a,b = 0,0,1
	while n<max:
		yield b 
		a,b =b,a+b
		n+=1
	# return'done'

for x in fibGenerator(10):
	print(str(x)+'\t')


def triangle(max):
	L =[1]
	n = 0
	while n<max:
		yield L 
		L.append(0)
		L = [L[i-1] +L[i]  for i in range(len(L))]
		n+=1

for x in triangle(2):
	print(x)

"""
Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
"""

