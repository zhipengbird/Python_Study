#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-24 14:40:29
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os

def maxSubArray(array):
	"""
	1. 数组为空的情况下返回0
	2.  当我们加上一个正数时，和会增加；当我们加上一个负数时，和会减少。
	如果当前得到的和是个负数，那么这个和在接下来的累加中应该抛弃并重新清零，不然的话这个负数将会减少接下来的和
	"""
	if not array:
		return 0

	currSum = 0
	maxSum = array[0]
	startindex = endindex = 0
	index  = 0 # 用于记录当前元素的下标
	for value in array:
		if currSum >= 0:
			currSum += value 
		else:
			currSum = value
			# array.index(maxSum) 这样获取的索引下标（在有多个相同的值时）不准确
			startindex = index

		if currSum > maxSum:
			maxSum = currSum
			endindex = index
		index += 1
	
	if maxSum < 0: # 最大值小于0说明，数组中元素的值都小于0,开始元素下标与结标元素下标为最大值所在的位置
		startindex = endindex = array.index(maxSum)
	print(startindex,endindex)
		
	return (maxSum,array[startindex:endindex+1])


def maxSubArray2(array):
	if not array:
		return 0
		
	curSum = maxSum = array[0] # 全部为负数时，返回数组中的最大值
	for num  in array[1:]:
		#（当前元素，连续子数组和加上元素）取最大值作为当前连续子数组的和
		curSum = max(num,curSum+num)
		# （当前连续子数组的和，最大连续子数组的和） 取最大值作为最大连续子数组的和
		maxSum = max(curSum,maxSum)
	
	return maxSum

def maxSubArray3(nums):
        numsLen = len(nums)
        list = [0 for i in range(numsLen)]
        for i in range(numsLen):
            if i == 0:
                list[0] = nums[0]
                continue
            if list[i - 1] >= 0:
                list[i] = list[i -1] + nums[i]
            if list[i - 1] < 0:                
                list[i] = nums[i]
        print(list) 
        return max(list)

def maxSubArray4(nums):
	if not nums:
		return 0

	curSum = maxSum = 0
	index_start = index_end = 0
	index = 0
	for num in nums:
		curSum += num 
		if curSum < 0:
			curSum = 0
			index_start = index+1
		if curSum > maxSum:
			maxSum = curSum
			index_end =  index
		index +=1

	if maxSum == 0:
		maxSum = max(nums)
		index_start = index_end = nums.index(maxSum)

	return (maxSum,nums[index_start:index_end+1])
	
if __name__ == '__main__':
	array = [-1, -2, -3, -10, -4, -7, -2, -5,-10]
	array = [-2,1,-3,4,-1,2,1,-5,4]
	print(maxSubArray(array))
	print(maxSubArray4(array))