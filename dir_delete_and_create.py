#-*-coding:utf-8-*- -
import os,time,string
#在当前目录下创建新文件夹
def cur_path(dir):
    new_path=os.path.join(os.getcwd(),dir)
    print("\n"+new_path)
    os.mkdir(new_path)
    print("directory has created.")
    time.sleep(5)
    os.rmdir(new_path)
    print("directory has deleted.\n")

#在上一级文件夹中创建新文件夹
def parent_path(dir):
    n_path=os.path.split(os.getcwd())[0]
    n_path=os.path.join(n_path,dir)
    print("\n"+n_path)
    os.mkdir(n_path)
    print("directory has created.")
    time.sleep(5)
    os.rmdir(n_path)
    print("directory has deleted.\n")
    
#判断文件夹名字的合法性
def check_dir(dir):
    for x in dir:
        if not x.isalpha() or x.isdigit() or x.isspace():
            print("your directory's name have some problem.")
            return True

#函数指向和方法检查
def check_method(command,dir_name):
    if command=="1":
        if check_dir(dir_name):
            raise StopIteration()
        cur_path(dir_name)
    elif command=="2":
        if check_dir(dir_name):
            raise StopIteration()
        parent_path(dir_name)
    else:
        print("It cannot support this method, please enter again.\n")
    
#主程序
while True:
    try:
        print("we offer two method to create directory and delete it.")
        print("1.In current path.\n2.In parent path.")
        comm=input("please enter number relate to te method you want.\n")
        dir_name=input("Then, you should enter the name of new derictory.\n")
        check_method(comm,dir_name)
    except Exception as err:
        print(str(err))