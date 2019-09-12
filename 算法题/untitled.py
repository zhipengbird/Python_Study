#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-05 14:13:20
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

import os
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while x != 0:
        	 res  = res * 10 + x % 10
        	 x  = x // 10 
        return res


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