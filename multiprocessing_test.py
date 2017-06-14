import multiprocessing as mp
import time,os,random
def char(st,q):
    print("id: %s" %os.getpid())
    ok=abs(int(st))
    q.put(ok)

def cal1(k):
    print("id: %s" %os.getpid())
    num=k.get(True)
    num=int(num)*int(num)
    k.put(num)
    print(str(num))
    
    
def cal2(k):
    print("id: %s" %os.getpid())
    num=k.get(True)
    num=num*2
    print(str(num))
    
    
if __name__=="__main__":
    num=input("please input")
    q=mp.Queue(10)
    a=mp.Process(target=char,args=(num,q,))
    a.start()
    a.join()
    p=mp.Process(target=cal1,args=(q,))
    p.start()
    p.join()
    k=mp.Process(target=cal2,args=(q,))
    k.start()
    k.join()
    print("end")

