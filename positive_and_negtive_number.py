er="r"
while er=="r":
    try:
        judge=input("please enter the number for judgement:")
        if float(judge) <0:
            print("this number is negative number"+"\n")
        elif float(judge)>0:
            print("this number is positive number"+"\n")
        else:
            print("this number is equal to zero"+"\n")
    except ValueError as err:
        print("Data error:"+str(err)+"\n")
        er=input("enter 'r' to retry, or enter other keys to exit this programme:")
exit()
    