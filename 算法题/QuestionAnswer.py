#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 14:34:27
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os

"""
    NSMutableArray * array = [NSMutableArray array];
    for (int i  = 0; i<100; i++) {
        [array addObject:@(i)];
    }
    NSMutableIndexSet * indexSet = [NSMutableIndexSet indexSet];
    [array enumerateObjectsUsingBlock:^(id  _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
        if (idx%2==0) {
            [indexSet addIndex:idx];
        }
    }];
    [array removeObjectsAtIndexes:indexSet];
"""



"""给定一个含有n个元素的整型数组a，求a中所有元素的和

"""
def sumArray(array,arraylength):
	if arraylength==0:
		return 0
	else:
		return sumArray(array,arraylength-1)+ array[arraylength-1]
	
"""给定一个含有n个元素的整型数组a，找出其中的最大值和最小值

常规的做法是遍历一次，分别求出最大值和最小值，但我这里要说的是分治法(Divide and couquer)，
将数组分成左右两部分，先求出左半部份的最大值和最小值，再求出右半部份的最大值和最小值，然后综合起来求总体的最大值及最小值。
这是个递归过程，对于划分后的左右两部分，同样重复这个过程，直到划分区间内只剩一个元素或者两个元素
"""
def maxAndMinInArray(array,left_startIndex,right_end_index):

	if left_startIndex == right_end_index : # l与r之间只有一个元素
		return (array[left_startIndex],array[right_end_index])

	if left_startIndex +1 == right_end_index: # l与r之间只有两个元素
		if array[left_startIndex]> array[right_end_index]:
			return(array[left_startIndex],array[right_end_index])
		else:
			return(array[right_end_index],array[left_startIndex])


	middle = (left_startIndex + right_end_index)//2  # 求中点
	print(middle)

	(leftmax,leftMin) = maxAndMinInArray(array,left_startIndex,middle) # 递归计算左半部份
	(rightmax,rightmin) = maxAndMinInArray(array,middle+1,right_end_index) # 递归计算右半部份

	return(max(leftmax,rightmax),min(leftMin,rightmin))



def onlyrepeatNumInarray(array,max):

	return sum(array) - sum(range(0,max))

def onlyappearOnceInArray(array):
	num = array[0]
	for index  in range(1,len(array)):
		num ^= array[index]
	return num

if __name__ == '__main__':
	array = range(2,100,3)
	for value  in array:
		print(value,sep='\t',end='\t')
	print()
	print(sumArray(array,len(array)))

	print(maxAndMinInArray(array,0,len(array)-1))


	print(onlyrepeatNumInarray([1,3,4,5,6,8,9,2,7,8,0],10))
	print(onlyappearOnceInArray([4,5,6,6,5,4,7,7,9]))
