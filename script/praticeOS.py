
# -*- coding: utf-8 -*-
# @Date    : 2017-03-01 20:45:51
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""pratice
#/usr/bin/env python
 [description]
"""


import os
import time
import pwd
import grp

import sys
# from importlib import reload
reload(sys)

# reload() 
sys.setdefaultencoding('utf8')  


def mode_format(mode):

    trans_dict = {'0': '---', '1': '--x', '2': '-w-', '3': '-wx',
                  '4': 'r--', '5': 'r-x', '6': 'rw-', '7': 'rwx'}
    # trans_dict =('0':'---')
    mode = oct(mode)
    mode_f = ''
    if mode[2] == '4':
        mode_f += 'd'
    else:
        mode_f += '-'

    for i in mode[-3:]:
        mode_f += (trans_dict[i])

    return mode_f


def dir_l(dir=None, ignoreHideFile=False):
    '''默认输入的路径为当前路径，默认显示隐藏文件'''
    if dir == None:
        dir = os.getcwd()
    listdir = sorted(os.listdir(dir))

    if ignoreHideFile:
        listdir = [x for x in listdir if x[0] != '.']

    total_size = 0  # 计算目录下文件夹及文件大小
    for x in listdir:  # 注意，每个文件至少占据4096字节
        temp = os.path.join(dir, x)
        total_size += (os.stat(temp).st_size + 4096 - 1)//4096 * 4
    print('total_size:', total_size)
    for x in listdir:
	    x_abs = os.path.join(dir, x)
	    stat = os.stat(x_abs)  # 获取文件信息
	    mode = mode_format(stat.st_mode)  # 获取文件权限码
	    nlink = stat.st_nlink  # 获取node数，有多少链接指向这个文件或文件夹
	    uid = pwd.getpwuid(stat.st_uid)[0]  # 获取文件所有者用户名
	    gid = grp.getgrgid(stat.st_gid)[0]  # 获取文件所有者组名
	    size = stat.st_size  # 获取文件大小，Linux中目录也是文件，大小始终是4096
	    mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))  # 获取文件最后修改时间,并格式化
	    # print(u''.join((x_abs,)).encode('unicode_escape').strip())
	    # print(type(x_abs))
	    print("{:<} {:<} {:<} {:<} {:<8} {:<10} {:<}".format(mode,nlink,uid,gid,size,mtime,u''.join((x,)).encode('utf-8').strip() ))
	    # print(x.encode('gbk2312'), end='\n')
	    # print('%s'%x_abs)
	    # print(unicode(x,'gbk'), end='\n')
	    # print('{:<} {:<} {:<} {:<} {:<8} {:<}'.format(mode, nlink, uid, gid, size, mtime))



if __name__ == '__main__':
    dir_l()
