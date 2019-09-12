import os
def findFileListWithsubfix(subfix,path):
    # 分别返回：父目录，所有文件夹，所有文件
    result =[]
    for root ,parent ,files in os.walk(path):
        for x in files:
            # strs =''+root+''+x
            if os.path.splitext(x)[1] == subfix:
                print(os.path.join(root ,x))  # print('%s'% strs)
                result.append(os.path.join(root ,x))



if __name__ == '__main__':
	findFileListWithsubfix('.png','/Users/yuanpinghua/Downloads/emoj')