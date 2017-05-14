while True:
    try:
        dollar=input("please enter how much dollar you want to culculate. \n")
        cent=[25,10,5,1]
        coin=["a","b","c","d"]
        dollar_1=int(float(dollar)*100)
        rest=0
        for i in range(4):
            coin[i],rest=divmod(dollar_1, cent[i])
            dollar_1=rest
        print("the number of cent coin you need is:")
        print("25cents:%i coins \t 10cents:%i coins \t 5cents:%i coins \t 1cent:%i coins" % (coin[0],coin[1],coin[2],coin[3]))
    except ValueError as err:
        print("Data error:%s" % str(err))
        
    
