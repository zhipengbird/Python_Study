#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 19:18:37
# @Author  : 袁平华 (yuanpinghua@yeah.net)
# @Link    : yuanph.org
# @Version : 1.0

"""将文件夹下面的GIF动图转成plist文件


"""


import os
import shutil
from biplist import *


def findFileListWithsubfix(subfix, path):
    # 分别返回：父目录，所有文件夹，所有文件
    result = []
    index = 1
    for root, parent, files in os.walk(path):
        subindex=1
        package = {}
        item = []
        for file in files:
            if os.path.splitext(file)[1] == subfix:
                newname = "%zd_%zd.gif"%(index,subindex)
                itemdic = {"id": '%d' % index, "imageGIF": newname, "text": os.path.splitext(file)[0], "type": 1,"key":"custom_emoji/%s"%(newname)}
                item.append(itemdic)
                sourcefile = os.path.join(root, file)
                moveFileAndRename(sourcefile,os.path.basename(root).splitext(' ')[1],)
                subindex+=1

            else:
                if os.path.splitext(file)[1] == '.pdf':
                    print("%s " % os.path.basename(root))
                    packageDes = {"packageName": os.path.basename(
                        root), "packageImage": os.path.splitext(file)[0], "type": 1}
                    package.update({"package": packageDes})

        if len(item) > 0:
            index += 1
            package.update({"items": item})
            result.append(package)
        # writePlist(package, './emoji/'+ os.path.basename(root)+".plist")
        # result.append(package)
        writePlist(result, "builtin_GIF.plist")
    return result


def moveFileAndRename(sourcefile, detinationFile='', newName=''):
    print("fdasf"+detinationFile)
    shutil.move(sourcefile, '/Users/yuanpinghua/Desktop/emoji/%s.gif'%(detinationFile))


if __name__ == '__main__':
    result = findFileListWithsubfix(
        '.gif', '/Users/yuanpinghua/Desktop/new Project/GIFEmoji')
