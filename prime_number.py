#-*-coding:utf-8-*- -
from math import sqrt
to=0
for x in range(101,201):
    i=0
    for y in range(2,int(abs(sqrt(x)))+1):
        if x % y==0:
            break
        else:
            i+=1
            if i==int(abs(sqrt(x)))-1:
                print(x)
                to+=1
print("Total:"+str(to))       