while True:
    try:
        year=input("please enter the year you want to judge \n")
        if int(year)%4==0 and int(year)%4!=0 or int(year)%400==0:
            print("%s is Leap year" % year)
        else:
            print("%s is not Leap year" % year)
    except ValueError as err:
        print("Data error: %s" % str(err))
    