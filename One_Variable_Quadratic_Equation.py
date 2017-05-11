import math

def quadratic(a,b,c):
    first_re=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    second_re=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return first_re,second_re

def check(a,b,c):
    sx=b**2-4*a*c
    if sx<0 or a==0:
        return False
    else:
        return True

while True:
    try:
        fac=input("please enter the factor:a,b,c, and split them by ','."+"\n")
        fac=fac.split(",")
        if not len(fac)==3:
            print("you should input three numbers, please check your data.")
        else:
            print("now a="+fac[0]+", b="+fac[1]+", c="+fac[2])
            re=input("if you have comfirmmed, enter 'y',if you want to input again, enter other keys."+"\n")
            if re=="y":
                a=float(fac[0])
                b=float(fac[1])
                c=float(fac[2])
                
                if check(a,b,c)==True:
                    (fir_an,sec_an)=quadratic(a,b,c)
                    print("anwser is: "+str(round(fir_an,3))+", "+str(round(sec_an,3)))
                    qu=input("if you want to quit, enter 'q', again enter other keys."+"\n")
                    if qu=="q":
                        break
                else:
                    print("your factor cannot meet the 'b^2-4ac> or a<>0' commend,please input again"+"\n")
                    
    except():
        print("there are some problems in current step, please check."+"\n")
exit()
