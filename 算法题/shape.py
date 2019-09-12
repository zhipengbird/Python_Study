#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-31 12:33:15
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os
import sys

def shape(num):
	for i in range(num):
		for j in range(num-i):
			sys.stdout.write(' ')
		for k in range(2*i+1):
			sys.stdout.write('*')
		print()
	for i in range(num-1):
		for j in range(i+2):
			sys.stdout.write(' ')
		for k in range((num-1-i)*2-1):
			sys.stdout.write('*')
		print()


if __name__ == '__main__':
	shape(4)
