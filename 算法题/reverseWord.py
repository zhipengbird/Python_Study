#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-05 14:00:27
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import sys

def reverseWord(sentence):
	return ' '.join(reversed(sentence.split()))


print(reverseWord('I love you'))

def reverse(x):
     s  = cmp(x,0)
     print(s)
     res = int(str(x*s)[::-1])*s
       
     return  res * (abs(res)<2**31)

print(reverse(-100))