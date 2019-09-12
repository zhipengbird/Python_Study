#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-05 14:13:20
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
	      s  = cmp(x,0)
	     	print(s)
	     	res = int(str(x*s)[::-1])*s
	       
	     	return  res * (abs(res)<2**31)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            
            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()