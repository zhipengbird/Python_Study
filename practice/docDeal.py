
# -*- coding: utf-8 -*-
import  os
import  docx
import exception
from docx2txt import docx2txt


def findFileListWithsubfix(subfix,path):
    # 分别返回：父目录，所有文件夹，所有文件
    result =[]
    for root ,parent ,files in os.walk(path):
        for x in files:
            # strs =''+root+''+x
            if os.path.splitext(x)[1] == subfix:
                print(os.path.join(root ,x))  # print('%s'% strs)
                result.append(os.path.join(root ,x))


    return result

if __name__ == '__main__':
    rs = findFileListWithsubfix(".docx", "/Users/yuanpinghua/Downloads/袁/201603")
    print(rs)
    doc  =docx.Document(rs[1])
    par = doc.paragraphs()
    for pa in par:
    	pass