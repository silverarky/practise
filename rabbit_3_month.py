class rabbit(object):
    def __init__(self):
        self.a,self.b=1,1
        self.c=1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        self.c+=self.b
        if self.c>10000:
            raise StopIteration()
        return self.c
    
for i in rabbit():
    print(i)