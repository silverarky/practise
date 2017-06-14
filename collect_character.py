#-*-coding:utf-8-*- -
import string
def collect(st):
    alp=0
    stripp=0
    num=0
    els=0
    for x in st:
        if x.isalpha():
            alp+=1
        elif x.isspace():
            stripp+=1
        elif x.isdigit():
            num+=1
        else:
            els+=1
    print("number of alpha:%d" %alp)
    print("number of strip:%d" %stripp)
    print("number of number:%d" %num)
    print("number of else chracter:%d" %els)
    
sti=input("please enter the string you want\n")
collect(sti)