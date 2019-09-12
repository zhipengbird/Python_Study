#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-14 11:02:48
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os

"""冒泡排序

1.算法描述：
（1）共循环 n-1 次
（2）每次循环中，如果 前面的数大于后面的数，就交换
（3）设置一个标签，如果上次没有交换，就说明这个是已经好了的。

时间复杂度O(n2)
"""
def bubble_sort(numbers):
	flag = True 
	for i in range(len(numbers)-1,0,-1):
		if flag:
			flag = False 
			for j in range(i):
				if numbers[j] > numbers[j+1]:
					numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
					flag = True 
		else:
			break 

if __name__ == '__main__':
	numbers = [1,3,2,100,4,20,90,19,20,93,234]
	bubble_sort(numbers)
	print(numbers)
		

