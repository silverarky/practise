class chain(object):
    def __init__(self,path="get"):
        self._path=path
        
    def __getattr__(self,path):
        return("s%/s%" % (self._path,path))
    
    def __call__(self._path,path):
        return("s%/s%" % (self._path,path))
    
    def __str__(self):
        return self._path
    
    __repr__=__str__
        