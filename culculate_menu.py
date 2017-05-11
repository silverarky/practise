class culculate:
    def __init__(self,kk):
        self.num=kk
        
    def sum(self):
        sum=0
        for x in self.num:
            sum+=float(x)
        return sum
        
    def aver(self):
        aver=0
        for x in self.num:
            aver=self.sum()/len(self.num)
        return aver
    
re="r"
try:
    print("now, this culculator is open")
    while re=="r":
        number=input("please enter these number,and split them by ','"+"\n")
        kk=number.split(",")
        number=culculate(kk)
        
        print("function is following:please choose one to run.")
        print("1.sum of these number")
        print("2.average of these number")
        print("enter 'x' to quit this culculator")
        
        chos=input()
        if chos=="1":
            print("Sum of these number is:"+str(number.sum())+"\n")
            re=input("if you want to try another numbers, please enter 'r',quit enter other key."+"\n")
            if not re=="r":
                break
        elif chos=="2":
            print("Average of these number is:"+str(number.aver())+"\n")
            re=input("if you want to try another numbers, please enter 'r',quit enter other key."+"\n")
            if not re=="r":
                break
        elif chos=="x":
            break
        else:
            print("please retry the commend."+"\n")
    exit()
except():
    print("current data have some problems."+"\n")
        
            
    