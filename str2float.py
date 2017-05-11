from functools import reduce
def str2float(x):
    convert_dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def single(k):
        if k=='.':
            return k
        else:
            return convert_dict[k]
    integer_list=list(map(single,x[0:x.find(".")]))
    decimal_list=list(map(single,x[x.find(".")+1:]))
    decimal_list.reverse()
    integer_part=reduce(lambda x,y:x*10+y,integer_list)
    decimal_part=reduce(lambda x,y:x*0.1+y,decimal_list)*0.1
    return integer_part+decimal_part

print(str2float('123.456'))

    
    
