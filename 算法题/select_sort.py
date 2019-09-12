#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-14 10:49:03
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os

""" 选择排序

对于一组关键字{K1,K2,…,Kn}， 首先从K1,K2,…,Kn中选择最小值，假如它是 Kz，则将Kz与 K1对换；
然后从K2，K3，… ，Kn中选择最小值 Kz，再将Kz与K2对换。
如此进行选择和调换n-2趟，第(n-1)趟，从Kn-1、Kn中选择最小值 Kz将Kz与Kn-1对换，
最后剩下的就是该序列中的最大值，一个由小到大的有序序列就这样形成。
"""
def select_sort(numbers):
	for i in range(0,len(numbers)):
		min = i 
		for j in range(i+1,len(numbers)):
			if numbers[j] < numbers[min]:
				min = j
		numbers[i],numbers[min] = numbers[min],numbers[i]

if __name__ == '__main__':
	numbers = [1,3,2,100,4,20,90,19,20,93,234]
	select_sort(numbers)
	print(numbers)