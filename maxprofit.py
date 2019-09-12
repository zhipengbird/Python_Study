#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-27 21:15:20
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os
import sys
def maxprofit(prices):
	max  = 0
	length = len(prices)
	for i in range(1,length):
		print(prices[i])
		if prices[i] > prices[i-1]+2 :
			max  = max + (prices[i]- prices[i-1]-2)
			print(u'buy:%s,sale:%s'%(prices[i-1],prices[i]))
	return max 
	

def maxProfit(prices):
	minprice = sys.maxsize
	# print(minprice)
	profit = 0
	length = len(prices)
	for index  in range(0,length):
		if prices[index] < minprice:
			minprice = prices[index]
		elif prices[index]-minprice > profit:
			profit = prices[index] - minprice
	print(profit)
	return profit
			
		




if __name__ == '__main__':

	prices =  [0, 2, 1, 8, 4, 9]
	max=  maxprofit(prices)
	print(max)

	# print(maxProfit(prices))