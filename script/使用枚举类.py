
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 12:54:59
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""[使用枚举类]
#!/usr/bin/env python
 
"""
__author__ = '袁平华'

from enum import Enum


# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

# from Enum  import Enum
# @unique装饰器可以帮助我们检查保证没有重复值。
# @unique
class Months(Enum):

    """docstring for Month"""
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class WeekDay(Enum):

    """docstring for WeekDay"""
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

for name, member in Months.__members__.items():
    print(name, '=>', member, ',', member.value)

for name, member in WeekDay.__members__.items():
    print(name, '=>', member, ',', member.value)