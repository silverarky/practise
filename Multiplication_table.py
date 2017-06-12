#-*-coding:utf-8-*-
try:
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d" %(i,j,i*j),end=" ")
        print("")
        
except Exception as err:
    print(str(err))