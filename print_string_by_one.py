re="r"
while re=="r":
    try:
        print("\n")
        leng=0
        st=input("please enter the string:")
        length=len(st)
        while leng<length:
            print(st[leng],end=" ")
            leng+=1
    except ValueError as err:
        print("string error:"+str(err)+"\n")
        re=input("enter 'r' to retry, or enter other keys to quit")
exit()
    
    
    