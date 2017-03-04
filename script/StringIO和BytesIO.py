#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 19:46:25
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[StringIO]

很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
"""

from io import StringIO, BytesIO
##将str写入IO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('word')

# getvalue()方法用于获得写入后的str。
print(f.getvalue())

# 读取IO 可以用一个str初始化StringIO 然后像文件一样读取

read =  StringIO('hello \n word \n')
while True:
	s = read.readline()
	if s =='':
		break 
	print(s.strip())

#写入IO
IO = BytesIO()
IO.write('中国'.encode('utf-8'))
print(IO.getvalue())
#读取IO

IO = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(IO.read())

#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。






