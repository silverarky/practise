num=input("please enter the numbers you wnat to arrange, and split them by ','."+"\n")
num=num.split(",")

for x in range(len(num)-1):
    for i in range(len(num)-1):
        if float(num[i])<float(num[i+1]):
            p=0
            p=num[i]
            num[i]=num[i+1]
            num[i+1]=p
            
print(num)
        