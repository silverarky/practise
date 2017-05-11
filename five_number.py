re="r"
con="cont"
while re=="r":
    sum=0
    try:   
        raw_num=input("please enter numbers that you want to culculate the sum.(notice: please split them by ',')"+"\n")
        num=raw_num.split(",")
        if len(num)<5:
            con=input("you have't enter five numbers in the first step,if you wnat to continue, please enter 'cont'; correct enter 'cor';retry please enter other keys"+"\n")
            while con=="cor":
                con=input("please enter the number and position you what to correct,split them by ',',or enter 'q' to quit correct step"+"\n")
                if con=="q":
                    con="cont"
                    break
                else:
                    con=con.split(",")
                    cc=int(float(con[1]))-1
                    num[cc]=con[0]
                    print("now, your number is:",end='')
                    for x in num:
                        print(x,end=",")
                    print("\n")
                    con="cor"
            if con=="cont":
                for x in num:
                    sum+=float(x)
                print("result:"+str(sum))
                re=input("enter 'r' to return to the first step, or enter q to quit this programme"+"\n")
                if re=="q":
                    exit()
        else:
            for x in num:
                sum+=float(x)
            print("result:"+str(sum))
            re=input("enter 'r' to return to the first step, or enter q to quit this programme"+"\n")
            if re=="q":
                exit()
    except:
        print("current step have some problem, please check what you input!")
        re="r"
            