def triangles():
    line=[1]
    yield line
    line[1,1]
    while True:
        yield line
        line=[1]+[line[i]+line[i+1] for i in range(len(line)-1)]+[1]