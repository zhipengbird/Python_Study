#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-06 11:19:17
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[summary]

 [description]
"""

import random
import os

box1 = 10
box2 = 20 
box3 = 30

def  getValueFromBox(box):
			return random.randint(1,box)
box1_get1 = getValueFromBox(box1)
box2_get2 = getValueFromBox(box2)
box3_get3 = getValueFromBox(box3)
print('the value from  box1:%d ,\tbox2:%d, \tbox3:%d'%(box1_get1,box2_get2,box3_get3))

def compression(boxlist,boxlistvalue):
		
		temp = 1 
		value = 0
		index =0
		for (box, value1) in zip(boxlist,boxlistvalue):
			if index==0:
					index+=1
					value +=value1
					temp  = temp * box 
			else:
					index +=1
					temp  = temp * box 
					value += value1*temp 
		return [value,temp]  



compress = compression([box1,box2,box3],[box1_get1,box2_get2,box3_get3])
print('compress value = %d ,temp  = %d '%(compress[0],compress[1]))

#compress
temp = box1 
value = box1_get1
print("compress step1: temp:%d value:%d"%(temp,value))

temp = temp * box2
value = value + box2_get2 * temp 
print("compress step2 : temp:%d value:%d"%(temp,value))


temp = temp * box3 
value = value + box3_get3 * temp 

print("compress step3 :temp:%d value:%d"%(temp,value))

#decompression

#---------------
box3_value = value//temp 
print("decompression step1: the value from box3 is : %d"%(box3_value))
value = value%temp
temp = temp/box3
print("decompression step1:temp:%d value:%d"%(temp,value))

#---------------
box2_value = value//temp 
print("decompression step2: the value from box2 is : %d"%(box2_value))
value = value % temp 
temp  = temp/box2 
print("decompression step2:temp:%d value:%d"%(temp,value))

#---------------

box1_value = value  
print("decompression step1: the value from box1 is : %d"%(box1_value))







