#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 20:18:19
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""


import os


print(os.name) #posix
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#
 
#要获取详细的系统信息，可以调用uname()函数 
print(os.uname())
#注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。



#环境变量
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key')：
print('----')
print(os.environ.get('DISPLAY'))
print('----')
print(os.environ.get('PWD'))
print('----')
print(os.environ.get('USER'))
print('----')
print(os.environ.get('_'))
print('----')
print(os.environ.get('PWD'))
print('----')
print(os.environ.get('LOGNAME'))
print('----')
print(os.environ.get('PATH'))
print('----')
print(os.environ.get('HOME'))
print('----')
print(os.environ.get('TMPDIR'))


# 操作文件和目录

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
path = os.path.join(os.path.abspath('.') ,'sub')
print(path)
# 然后创建一个目录:
if not os.path.exists(path):
 	os.mkdir(path)
# 删掉一个目录:
os.rmdir(path)

#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

print(os.path.split('/Users/michael/testdir/file.txt'))
print( os.path.splitext('/path/to/file.txt'))

try:

	os.rename('test2.txt','test.txt')
except Exception as e:
	print(e)

try:
	os.remove('text.html')

except Exception as e:
	print(e)

L = [x for x in os.listdir('/Users/yuanpinghua') if os.path.isdir(x)]
print(L)

# 要列出所有的.py文件，也只需一行代码：
L = [x.encode('utf-8') for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] =='.py']
print(L)








