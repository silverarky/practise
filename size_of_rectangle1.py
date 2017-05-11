try:
    first_line=input("Please enter the first data:")
    second_line=input("Then, the second:")
    size=float(first_line)*float(second_line)
    print("the size of this rectangle is:"+str(size))
except ValueError as err:
    print("Data error:"+str(err))