# -*- coding:utf-8 -*-
import os
import os.path,datetime
import glob 
import time
import sys
import shutil




"""
遍历指文件夹下面的所有文件
"""
def iteratorDirFileList(result_dir,reserveCount):
	filelist = os.listdir(result_dir)
	# print(len(filelist))
	filelist.sort(key=lambda fn: os.path.getmtime(os.path.join(result_dir,fn)) 
		if not os.path.isdir(os.path.join(result_dir,fn)) else 0)
	filecount = len(filelist)
	# print('len'+str(filecount))
	# print('count'+ str(reserveCount))
	# print(filecount > reserveCount)
	if filecount > reserveCount:
		deletFilelist =filelist[0:(filecount-reserveCount)]
		print('正在删除...')
		print('--------')
		# print(deletFilelist)
		deleteDirFile(result_dir,deletFilelist)
		print('--------')
		print('删除成功！！！')
		print('文件夹%s共有%d个文件，此次删除%d个文件，剩余%d个文件'%(result_dir,filecount,len(deletFilelist),reserveCount))
		# print(filelist)
	else:
		print("当前文件夹下文件个数小于或等于文件保留个数"+str(reserveCount)+"没有要清理的文件")

"""
删除指定目录下的 文件列表
"""	
def deleteDirFile(result_dir,filelist):
	for file in filelist:
		filepath = os.path.join(result_dir,file)
		if os.path.isfile(filepath):
			os.remove(filepath)
			print('removed :'+filepath)
		else:
			if os.path.isdir(filepath):

				shutil.rmtree(filepath)
				print('Dir removed:'+filepath)
			else:
				print(''+filepath+"不存在")

"""
在指定的文件夹下，遍历所有文件，找到带有指定后缀的文件 ，保留指定文件个数

"""
def iteratorDirFile(result_dir,suffix,reserveCount):
	
	filelist = glob.glob(os.path.join(result_dir,"*."+suffix))
	for file in filelist:
		print(file)
	fileCount = len(filelist)
	print('当前文件共有'+str(fileCount)+"个")
	if  fileCount > reserveCount:
		deletfileList = filelist[0:fileCount-reserveCount]
		deleteDirFile(result_dir,deletfileList)
	else:
		print("当前文件夹下文件个数小于或等于文件保留个数"+str(reserveCount)+"没有要清理的文件")
	




def iteratorDir(rootDir):
	fillist =[]
	logpath ="./log"
	if not os.path.exists(logpath):
		logpath = os.mkdir(logpaths)

	print(logpath)
	recordFile = os.path.join( logpath , time.strftime("%Y年%m月%d日%H_%M_%S", time.localtime())+'.txt')
	print(recordFile)
	open(recordFile,'a').write("%s 下所有文件目录\n" % (rootDir))
	for root, dirs, files in os.walk(os.path.realpath(rootDir)):
		# open(recordFile,'a').write("%s | %s |%s \n" % (root,dirs,files))
		for file in files:
			if '.DS_Store' in file:
				continue
			path = os.path.join(root,file)
			open(recordFile,'a').write("%s\n" % (path))

			print(path)
			fillist.extend(path)
		# print("u%s | u%s |u%s \n" % (root,dirs,files))
		# break
	print('%s 共有 %s个文件'%(rootDir,len(fillist)))
	open(recordFile,'a').write('%s 共有 %s个文件'%(rootDir,len(fillist)))

	# print(fillist)



		
# if __name__ == '__main__':
	# iteratorDirFileList('/Users/yuanpinghua/百度云同步盘/image/4K',20)
	# iteratorDirFile('/Users/yuanpinghua/百度云同步盘/image/4K','jpg',0)
	# iteratorDir('/Users/yuanpinghua/Desktop')

if len(sys.argv)>=3:
	rootDir = sys.argv[1]
	reservecount = int(sys.argv[2])
	iteratorDirFileList(rootDir,reservecount)
	# exit(0)
else:
	print("参数错误：请在参数添加文件夹路径和保留的文件个数关键字，如: python *.py rootdir reservefileCount")



