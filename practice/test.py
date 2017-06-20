import itertools

for key,group in itertools.groupby("AaaBBbcCAAa",lambda x:x.upper()):
    print(key,list(group))
    
print(list(itertools.takewhile(lambda x:x,itertools.chain('ABC','def'))))
    