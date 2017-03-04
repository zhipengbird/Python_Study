# -*- coding:utf-8 -*-


#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
#
print(int('12345'))
print(int('12345',base =8))
print(int('12345',base =16))
print(int('100101001',base =2))
# 
 
import functools

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int,base =2)

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
print(int2('1001'))

max2 = functools.partial(max,10)
print(max2(1,4,2))


