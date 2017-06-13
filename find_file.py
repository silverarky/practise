#-*- coding:utf-8 -*-
#递归函数，查找下一级目录中的文件
import os
def search(dir,text):
    for x in os.listdir(dir):
        if os.path.isfile(x):
            if text in x.splitext(".")[0]:
                print("%s, %s" %str(x))
        if os.path.isdir(x):
            search(os.path.join(dir,x),text)

#寻找目录中的有指定字符串的文件，并将工作目录变为该文件夹
def chpo():
    for x in os.listdir("."):
        if os.path.isdir(x) and "c" in x:
            os.chdir(os.path.join(os.getcwd(),x))
    kk=os.getcwd()
    print(kk)

    