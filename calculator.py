#-*- coding:utf-8 -*- - 
import math

#简单数字计算
def calculator1(method,n1,n2,n3=0):
    n1=float(n1)
    n2=float(n2)
    if method=="+":
        return  n1+n2
    elif method=="-":
        return n1-n2
    elif method=="*":
        return n1*n2
    elif method=="/":
        return n1/n2
    elif method=="%":
        return n1%n2
    elif method=="**":
        return n1**n2
    else:
        print("this culculator cannot support this method.")
        
#几何计算
def calculator2(method,n1,n2=0,n3=0):
    n1=float(n1)
    n2=float(n2)
    n3=float(n3)
    if method=="cir":
        result=math.pi*n1**2
    elif method=="squ":
        result=n1*n2
    elif method=="sph":
        result=4/3*math.pi*n1**3
    elif method=="cub":
        result=n1*n2*n3
    else:
        print("this culculator cannot support this method.")
    if result==0:
        print("you may not input enough data.")
    else:
        return result
    
while True:
    try:
        choose=input("do you want to cualculate numbers or geometry? enter 'num' or 'geo' \n")
        if choose=="num":
            print("you can enter '+', '-', '*', '/','%','**', as method")
            data=input("please enter method and the two numbers:N1,N2, and split them with ','. \n")
            raw=data.split(",")
            print("result:"+str(calculator1(raw[0],raw[1],raw[2])))
        elif choose=="geo":
            print("this calculator can calculate area of circle and square, and volume of cuboid and sphere.")
            print("you can enter 'cir', 'squ', 'cub', 'sph' as mathod. \n")
            data=input("please enter the method and the data:L/R,W,H , and split them with ','.No value, no input. \n")
            raw=data.split(",")
            for i in range(4-len(raw)):
                #补0，将raw补成4元素list
                raw.append("0")
            print("result:"+str(calculator2(raw[0],raw[1],raw[2],raw[3])))
    except Exception as err:
        print(str(err))
        
        