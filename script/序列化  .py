#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-06 14:10:18
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""序列化
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化
"""


import pickle
import pprint

d = dict(name='bob', age=20, score=90)
byte = pickle.dumps(d)
print(byte)

"""pickle



　python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

　　基本接口：

　　pickle.dump(obj, file2, [,protocol])
　　注解：将对象obj保存到文件file2中去。
　　　　　protocol为序列化使用的协议版本，
					0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；
					1：老式的二进制协议；
					2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为0。
　　　　　file2：对象保存到的类文件对象。file2必须有write()接口， file2可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。如果protocol>=1，文件对象需要是二进制模式打开的。

　　pickle.load(file2)
　　注解：从file2中读取一个字符串，并将它重构为原来的python对象。
　　file2:类文件对象，有read()和readline()接口。
"""

data = {'a':[1,2,3,5,4+5j],'b':('string',u'UnicodeDecodeError'),'c':None}
list1= [1,2,3]
# list1.append(list1)
with open('data.pkl','wb') as file2:
	pickle.dump(list1,file2)
	pickle.dump(data,file2,1)


with open('data.pkl','rb') as file2:
	data1 = pickle.load(file2)
	data2 = pickle.load(file2)
	pprint.pprint(data1)
	pprint.pprint(data2)


