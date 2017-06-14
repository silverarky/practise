#-*-coding:utf-8-*-
import multiprocessing as mp
import time,os

def user(admin):
    if admin == "reader":
        if check()=="reader_mode":
            read=mp.process(target=read,name="reader"+str(num))
            num+=1
            print("you are the d% readers" %num)
            reader_id.append(os.getpid())
            read.start()
            read.join()
            time.sleep(600)
            cl=input("after 600s you will exit this process")
            time.sleep(600)
            read.terminate()
            reader_id.remove(os.getpid())
            exit()
        else:
            print("sorry,writer is writing, please wait.")
            
    elif admin =="writer":
        if check()=="writer_mode":
            write=mp.process(target=write,name="writer")
            writer_id.append(os.getpid())
            write.start()
            write.join()
            time.sleep(6000)
            write_close()    
        else:
            print("sorry,reader is reading, please wait.")
    else:
        print("your information have some problem,please check!")

def write(name):
    name=input("please enter the file you write")
    with open("new.txt","w") as n_data:
        with open(name,"r") as o_data:
            n_data.append(o_data)

def read():
    with open ("new.txt","r") as data:
        k=data.read()
        print(k)

def check():
    if reader_id:
        return "reader_mode"
    elif writer_id:
        if len(writer_id)==1:
            return "writer_mode"
        
def write_close():
    cl=input("if you want to exit, please enter 'close'")
    if cl=="close":
        write.terminate()
        writer_id.remove(os.getpid())
        exit()
    else:
        write_close()

num=0
reader_id=[]
writer_id=[]
while True:
    admin=input("please enter you are reader or writer")
    user(admin)
    

        
        
