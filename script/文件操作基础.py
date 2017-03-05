#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-05 14:22:23
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""文件

文件对象不仅可以用来访问普通的物理文件，也可以访问任何其他类型抽象层面上的‘文件’。
"""

"""内建函数（open()/file()）
内建函数open()/file()提供了初始化输入／输出操作的通用接口
open()成功打开文件后会返回一个文件对象，否则引发一个错误（IOerror）。
 
file_object=open(filename ,access_mode='r',buffering=-1)
1. filename: 包含要打开的文件名字的字符串，它可以是相对路径或绝对路径
2. access_mode: 也是一个字符串，代表文件打开的模式 
3. buffering:用于指示访问文件所采用的缓冲方式。其中0表示不缓冲，1表示只缓冲一行数据。其他任何大于1的值代表给定值作为缓冲区的大小

file()和open()	函数具有相同的功能。可以任意替换，
建议使用open()来读写文件，在处理文件对象时使用file().eg:if instance(f,file)
""" 

# 文件方法可以分为四类：输入／输出／文件移动／杂项操作

"""文件输入
read()方法用来直接读取字节到字符串中，最多读取给定数目个字节，没有给定（默认-1)或负数 文件将读取至末尾
readline()方法读取打开文件的一行。
readlines() 读取所有剩余行，然后把它们作为一个字符串列表返回。可选参数sizHint表示返回最大字节大小。

""" 


"""输出

write()把含有文本数据或二进制数据块的字符串写入到文件中去。
writelines()方法是针对列表的操作，它接受一个字符串列表作为参数，将它们写入文件。行结束符不会自动加入，若需要，需在调用writelines()前给每行加入换行符。

""" 

"""文件内移动

seek()方法可以在文件中移动文件指针到不同位置。
1.offset 字节表示对于某个位置偏移量。
		1. 0: 默认值
		2. 1: 代表从当前位置算起
		3. 2: 代表从文件末尾算起
"""


"""文件迭代

一行一行访问文件
for eachline in file:
	print(eachline)
"""

with open('jsonArray.js') as file:
	for line in file:
		print(line)

import os
print(os.curdir)
print(os.pardir)
print(os.pathsep)
print(os.linesep)
print(os.sep)

"""os 模块属性
os 模块模性     	描述
linesep					用于在文件中分隔行的字符串
sep           	用来分隔文件路径名的字符串
pathsep					用于分隔文件路径的字符串
curdir					当前工作目录的字符串名称
pardir					当前目录的父目录字符串名称

"""
with open('jsonArray.js') as file:
	print(file.closed)
	print(file.encoding)
	print(file.mode)
	print(file.name)
	print(file.newlines)
	print(file.softspace)

"""文件内建属性

文件对象属性  				描述
file.closed				表示文件是否关闭，否则为False
file.encoding			文件所使用的编码 ，若为None时使用系统默认编码
file.mode 				access文件打开时使用的访问模式
file.name 				文件名字
file.newlines			未读取到行分隔符时为None 只有一种行为时为一个字符串，当文件有多种类型的行结束符时，则为一个包含所遇到的行结束符的列表
file.softspace  	为0表示在输出一数据后，要加上一个空格符，1表示不加。这个属性一般开发人员用不上。
"""


"""命令行参数

sys模块通过sys.argv属性提供了对命令行参数的访问。 命令行参数是调用某个程序时除程序名以外的其他参数
1. sys.argv 是命令行参数的列表
2. len(sys.argv)是命令行参数的个数
"""
import sys 
print('you enter '+str(len(sys.argv))+"arguments")








