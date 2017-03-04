# -*- coding:utf-8 -*-


import os
import os.path

"""
使用系统ping 指令
"""
# print os.system('ping www.pythonpy.com')

"""
使用系统命令创建 文件夹
"""
if not os.path.exists('test'):
	rs = os.system('mkdir test')
	print rs

"""
使用系统命令删除 文件夹
"""
if os.path.exists('test'):
	rs = os.system('rmdir test')
	print(rs)


"""
ifconfig是linux中用于显示或配置网络设备（网络接口卡）的命令，英文全称是network interfaces configuring。

"""
rs = os.system('ifconfig')
print(rs)



"""
ls 命令显示当前目录的内容.
"""
rs = os.system('ls -version')

print ("fdfas"+str(rs))




