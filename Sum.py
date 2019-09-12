#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 22:30:44
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os

def Sum_Solution(n):
	 sumresult = n 
	 sumresult and Sum_Solution(n-1)
	 return sumresult

if __name__ == '__main__':
	print(Sum_Solution(10))
