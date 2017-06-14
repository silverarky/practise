#-*-coding:utf-8-*- -
def fact(num):
    print("%d=" %num,end="")
    for x in range(2,num+1):
        if num % x== 0:
            print("%d" %x,end="")
            num=num/x
            if not num == 1:
                print("*",end="")
        if num==1:
            break
    
num=input("please enter the number")
num=abs(int(num))
fact(num)