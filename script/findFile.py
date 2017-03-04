#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 21:06:47
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""


import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")

"""中文编码问题

python 3.5 以下
import sys
reload(sys)
sys.setdefaultencoding("utf8")

python3.5 以下
默认编码就是utf8


"""


def findFileListWithsubfix(subfix):
	#分别返回：父目录，所有文件夹，所有文件
	for root,parent,files in os.walk('.'):
		for x in files:
			# strs =''+root+''+x
			if os.path.splitext(x)[1] ==subfix:	
					print(os.path.join(root,x))
			# print('%s'% strs)


if __name__ == '__main__':
	findFileListWithsubfix('.py')