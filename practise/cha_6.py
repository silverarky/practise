#-*- coding:utf-8 -*- - 
import os
os.getcwd()
os.chdir("D:\\w\git\python-challenge\channel")
#测试
with open ("readme.txt","r") as hint:
    h=hint.read()
    print(h)
with open ("90052.txt","r") as examples:
    e=examples.readline()
    print(e)

sp="90052.txt"
try:
    while True:
        with open (sp,"r") as data:
            d=data.readline()
            sp=d.split(" ")[-1]+".txt"
            print(d)
except Exception as err:
    print(str(err))
    