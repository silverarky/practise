re="r"
while re=="r":
    try:
        num=input("please enter the number you want:"+"\n")
        if float(num)<=100 and float(num)>=1:
            print("this is the right number.")
        else:
            re=input("you number is over the range,if you want to enter again,please enter 'r'."+"\n")
    except ValueError as err:
        print("number error:"+str(err))
exit()