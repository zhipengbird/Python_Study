#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 13:00:34
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : $Id$

"""mergeArray

Given 2 sorted arrays, A and B, where A is long enough to hold the contents of A and B, 
write a function to copy the contents of B into A without using any buffer or additional memory.
"""

import os

def mergeArray(arrayA,arrayB,aLength,bLength):
    aIndex = aLength-1
    bIndex = bLength-1
    mergeIndex = aLength+bLength-1

    while aIndex >=0 and bIndex >= 0:
        if arrayA[aIndex] > arrayB[bIndex]:
            arrayA[mergeIndex] = arrayA[aIndex]
            aIndex -= 1 
        else:
            arrayA[mergeIndex] = arrayB[bIndex]
            bIndex -= 1 


        mergeIndex -= 1

    while bIndex >= 0:
        arrayA[mergeIndex] = arrayB[bIndex]
        bIndex -= 1
        mergeIndex -= 1 


if __name__ == '__main__':
    a = [1,3,5,9,0,0,0]
    b = [2,4,6]
    mergeArray(a,b,4,3)
    print(a)



