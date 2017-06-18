##python 学习##

movie=["A","B","c"]  
返回当前定义所有名称的集合：locals（）  
嵌套列表：movie=["a",["b","e",["c"]],"d"]  
其中第一个数据在堆栈中的编号为0  

## 数据统计和处理 ##
输入：name=input（）  
输入：name=raw_input()【两者区别：input输入的数值中如果为纯数字，返回int类型。raw_仅返回str类型】  
List（）【返回一个列表】  
方法串联：data.Strip().split(“，”)  
创建空列表：movie=[]  
简单列表生成：movie=list(range(1,11))  
去除空白符：movie=movie.strip()  
倒序输出：movie.reverse()  
项数：len(movie)-->3  
调取：movie[1：3]-->B【其中0为第一行，-1为最后一行】  
嵌套列表调取：movie[1][2][1]-->"c"  
列尾增加：movie.append("k")-->movie=["A","B","c","k"]  
列尾增加集合：movie.extend(["q","w"])-->movie=["A","B","c","q","w"] 【原地操作，不返回list】 
列尾减少：movie.pop（）-->movie=["A","B","c"]  
特定位置之前增加：movie.insert(0，"l")-->movie=["l","A","B","c"]  
指定项删除：movie.remove("c")-->movie=["A","B"]  
原地排序：data.sort()【默认升序，参数reverse=TRUE降序】  
复制排序：data2=sorted(data)  
### 计算和参数 ###
**【乘方】；//【整除】；%【余数】；~【取反，结果和原值的和为-1】；==【逻辑等于】  
divmod:divmod(12,7)-->(1,5)【整除返回商和余数的元组】  
    Import math  
    Math.pi；math.cos,sin,tan  
    Math.pi/6=30°   

pow（a,b,c）【相当于（a**b）%c】
cmp（a,b）【如果a<b返回负整数，a=b返回0，a>b返回正整数】
num=[1,2,3]  
calc(*num)【将num中的元素作为可变参数输入，为tuple，也可以在定义函数时将参数定义为可变参数】  
calc（**num）【关键字参数，为dict，可以接收除可变和不变参数外多个信息。输入具体数值时需加上参数名，x=“asd”】  
def person(name, age, *, city, job):【命名关键字参数，接收指定名称参数值，输入具体数值时需加上参数名,x=“asd”】  
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数  

### 推导列表 ###
data1=[lol(x) for x in data]【前面的条件也可以是x*x】  
[x * x for x in range(1, 11) if x % 2 == 0]【加if条件，if为TRUE时进行循环】  
[m + n for m in 'ABC' for n in 'XYZ']【两层循环】  
### 集合 ###
set（）【无序，无重复项，可用于删除重复项】  
S.add(4)【向集合中添加元素】  
交集：S1 & S2；并集S1 | S2  
元组（tuple）：cla=(1,2)【元组中的元素不能改变】  
### 字典 ###
x={}  
x[“name”]=[“a”,“b”，“c”]  
x[“occupation”]=[“d”，“e”，“f”]  
x=dict()  
x={“name”:[“a”，“b”，“c”],“occupation”:[“c”，“d”，“e”]}  
x=dict([('a',1),('b',2)])  
【可以在函数内部返回字典项后，在外部定义字典名】  
d.get(“tos”,-1)【检查“tos”的key是否在dict中，不存在返回-1】  
for key，value in x【字典键，值迭代】  
x.clear【清除字典中的所有数据】  
x.pop('a')【删除键和所对应的值】  
x.popitem()【随机删除字典中的key和value】


----------

### 类 ###
    Class Athlete：
    	Def__init__(self,x,y)：
    		【类的项目初始化】
    		self.x=x【普通定义变量，外部可以更改】
    		self.__y=y【双下划线，私有变量，子类无法访问，外部无法更改，保护数据不被更改】  
			self._z=z【单下划线，保护变量，子类可以访问，其余同双下划线】
		__slots__=("names","age")【定义允许绑定的属性名称，当绑定之外的名称时，返回AttributeError，只有当有明确的限定需求时才使用，能节省内存】
    	Def tops（self）
    		【类下方法定义】【子类重新定义的函数，会将父类的函数覆盖】

		def top():  
			pass【外部定义函数】  
	student.top=top【将外部函数绑定到实例，成为仅属于该instance的方法，但是不绑定到class】
	from types import MethodType
	student.top=MethodType(top,student)【将外部函数绑定到instance，成为属于class的方法】
	
    D=Athelete(x,c)【D对应self，x,c对应x，y】【定义类】
    D.tops()【类下方法调用】
    Class Athlete（list）：【继承类】【多态：继承的子类拥有父类的type（既是Athlete也是list）】
    	Def__init__(self,name)
    	List.__init__([])【将继承的类初始化】  
	class MyTCPServer（TCPserver，FockingMixIn）：
		pass【使用MixIn进行多重继承，如果继承的关系不是纯粹的上下关系，而是并行关系，可以使用MixIn添加新类的额外功能。】【使用MixIn时，如果不同父类之间继承的方法有重复，子类会选择第一个继承的方法】

    	@property【将一个方法作为属性调用】【getter】
    	def width(self):
			return self.__width
		@width.setter【使用property后创建的装饰器，如果不设定setter，属性就为只读对象】
		def width(self,value):
			self.__value=value
		@width.deleter
		def width(self):
			del self.width【使用时输入del obj.width】
	
		width=property(fget,fset,fdel)【可以用property指定get、set、del的函数，设定fget为none为该属性无法读取】
		
【定义的类和str、int这些type是相似的】  
对象属性和方法测试：【不知道的情况下使用，能用obj.x就不用getattr（obj,"x"）】  
hasattr(obj,"x")-->True【判断属性：是否有属性x（self.x）或方法x】  
setattr(obj,"y",19)【设定属性：obj.y=19】  
getattr(obj,"y"，404)-->19【获取属性y，如果属性不存在返回默认值404】【y也可以是类中方法，结果是获取方法】
type(Athlete,(object),dict(hello=fn))【创建Athlete类对象;名称，继承父类，绑定fn方法】  

**定制类**  

    class person:
    	def __init__(self,name,gender):
        	self.name=name
        	self.gender=gender

    	def __str__(self):【当从外部直接使用print（instance）的时候，通过__str__方法优化输出】
        	return"person: %s, %s" %(self.name,self.gender)
		__repr__=__str__【当从外部直接输出instance时，通过__repr__优化输出。通过=方法避免重复定义】
	print(p)
	p

    class fib():
    	def __init__(self):
    		self.a,self.b=0,1
    
    	def __iter__(self):【迭代器，将类作为可迭代对象，可在外部使用迭代方法】
    		return self【如果需要使用类进行迭代，需要定义__iter__方法，实例本身为迭代对象时返回self】
    
    	def __next__(self):【每次调用类时，返回迭代器的下一个数值】
    		self.a,self.b=self.b,self.a+self.b
    		if self.a>100000:
    			raise StopIteration()【当while True时，可以返回程序起始点】
    		return self.a
	for i in Fib():
		print(i)
    
    class fib():
		def __getitem__(self.n):【生成器，将类作为list使用，可使用切片方法，n为之后的切片】	
    	if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
        return a
        if isinstance(n,slice):【n有可能是整数也有可能是slice对象】
            start=n.start【slice对象有start和stop两个属性，对应冒号前后，可直接调用】
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
                return L
	fib()[0]=1
	fib()[1:3]=

    class Chain(object):
    	def __init__(self, path=''):
        	self._path = path
    	def __getattr__(self, path):【当没有找到属性时，会调用__getattr__，使path=status。默认返回none】
        	return Chain('%s/%s' % (self._path, path))【如果出现链式调用属性，当前一个属性调用后即消失】
    	def __str__(self):
        	return self._path
    	__repr__ = __str__
	Chain().status.user.timeline.list-->'/status/user/timeline/list'

		def __setattr__(self,key,value)【当师徒对对象进行赋值时调用】
			self[key]=value

    class studenet(object):
    	def __init__(self,name):
    		self.name=name
    
    	def __call__(self):【将类作为函数调用】
    		print("my name is %s" % self.name)
    s=student("michael")
    s()  

**enum模块**（定义枚举类）
  
    from enum import Enum
    class Color(Enum):【继承Enum的枚举类属性】
    	red = 1【name：red；value=1】
    	orange = 2
    	yellow = 3
    	green = 4
   	 	blue = 5
    	indigo = 6
    	purple = 7
【成员名称不允许重复】  
【两个相同值的成员，第二个成员的名称被视作第一个成员的别名】  
【相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员】  
【限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique】

    from enum import Enum, unique
    @unique
    class Color(Enum):
    	red = 1
    	red_alias = 1
    for color in Color:【枚举类支持迭代】【不列出重复对象】
    	print(color)

    for name,number in Color.__menber__.item(): 【列出 重复对象】
## 数据类型 ##
Float()【转换为浮点数】  
Str()【转换为字符串】  
coerce（a,b）【将b转变为a的类型，返回tuple】
b=a.replace（”a”,”A”）【将字符串中的某个字符进行更改,但是变化过后a不变，只能讲变化结果赋值给其他对象】  
‘asdfghjl’[:3]-->asd【str也可以看作是一个list进行切片操作】  
Int(item,base=2)【转换为整数类型,2进制。default base=10】  
Abs()【绝对值】  
Max()；min()  
Bool()【数字只有0为false，其他为true】 
oct()【将整数转变为8进制】 
hex()【将整数转变为16进制】  
chr（）【将ASCII码转变为字符】  
ord（）【将字符转变为ASCII码】  
换行：/n；制表符：/t  

    import types  
    type(f)==type.FunctionType
【判断是否是函数类型】

**random模块**【返回伪随机数】  
randrange【参数和range一样，随机返回范围内的数。给变量赋值后无效】  
uniform（min，max）【返回浮点数】  
random（）【注意开头小写，返回0.0-1.0之间的浮点数】  
random.randint(10,20)【生成一个指定范围的整数】

## 函数内部控制 ##
### 迭代 ###
    **for** x in movie：  
    	print（x）  
每一次迭代，x（目标标识符）的值都会顺序改变  
迭代固定次数(range和for连用)：for x in range（4）-->0,1,2,3（迭代相应次数） 
 
    num=['a','b','c']  
    for i,j in enumerate(num)  
	print i,j
    0 a【enumerate（）在for中用于遍历元素及其坐标;for 的需指定2个目标标识符，顺序：编号，值】  
    1 b  
    2 c  

    count=0  
    **while** count<len(movie):  
    	print(movie[count])  
    	count=count+1  

### 判定 ###
isinstance（movie,（list，str））-->true【后面的判断条件可以是tuple】  
any（）【有一个是true，就返回true】  
all（）【全为true时返回true】

    **if** （not）len(movie)>3:
    	print("t")
    else:
    	print("k")

    from collections import Iterable
    isinstance('abc', Iterable)【判断‘abc’是否可迭代】

### 创建函数 ###
    def lol(x)
    	函数代码
    	Yield b【函数运行到yield关键字时会停止，并返回lol（b）值，使用next（）继续函数运行】
    return（x）【返回x的值】
可选参数：def lol(x=0)"增加缺省值"  
F=abs（）F()=abs()【变量可以指向函数】  

**调用模块中函数**  
nester.lol(x)

**导入模块**  
import.nester  
from nester import lol as L【添加模块到当前命名空间】【简化函数名】  
from tkinter import *【将模块中的所有方法导入，使用时不用加前缀】

**生成器**  
    Def odd():  
    	N=1  
    	While True:  
    		n+=1  
    	yield n  
    
    l=（x*x for xa in range(1,10)）
【只要是有yield的，都被定义为生成器，生成器每次只能通过next（）调取下一个值，但是生成器本身相当于一个列表】

**返回函数**  

    def lazy_sum(*args):  
    def sum():  
        ax = 0  
        for n in args:  
            ax = ax + n  
        return ax  
    return sum  
【这种方法称为闭包，外函数保存了内函数的变量和最后的计算值，需要调用外函数将值显示出来。在函数内定义的所用变量和内函数，在外部是无效的。】

**装饰器**

    import functools

    def log(text):
    def decorator(func):
        @functools.wraps(func)【functools.wrap()用于外部保存函数的名称，以便在下一级函数中使用】  
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

    @log
    def now():
    	print('2015-3-25')
【装饰器也是闭包结构，一层函数用于设置装饰器的参数，二层用于返回函数，三层是具体的使用装饰的函数。设置需要装饰的函数时，使用@，相当于log（now（））】  

### 高阶函数 ###
**Map**  
List（（map（str，[1,2,3,4,5]）））【map（）需要两个参数，第一个是计算函数名，第二个是可迭代对象。map将第二个参数中的所有元素进行迭代计算】【返回的仅是map对象，需要list（）】  
**Reduce**  

    from functools import reduce
	reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)  
【reduce（）需要参数和map（）相同，它将第二个参数中的所有元素进行累计计算】  
**filter**  
k=list（filter（f，[]））【f为返回bool值的函数，false时，filter将列表中的该数去掉】  
**sorted**  
sorted（[],key=f,reverse=True）【key为函数,函数仅用作判断，输出的还是原列表中的元素。reverse反转顺序。sorted默认升序，字符串时按照先a后z，先大写后小写排序】
### 匿名函数 ###
K=reduce(lambda x,y:x*y,[1,2,3,4,5])-->120【格式为lambda x：f，用于简单函数命名】  
### 偏函数 ###
    import functools
    int2=functools.partial(int,base=2)
    max=functools.partial(max,10)
【偏函数可以简单的根据原有函数创建新的函数，并可以固定原函数中的参数。如果不指定参数名，partial会将函数的后的数添加到每一次函数计算中】
## 文件处理 ##
打开和读取：
Data=open(‘ds.txt’，“w”)【w为覆盖写入模式，a为追加写入模式，默认为仅读取】【在非仅读取模式下，如果目录中没有该文件，open可以直接创建】  
with open（“sd.txt”） as data【不用close】  
read()【整体读取，直到末尾，作为字符串返回】  
readlines（）【读取所有行，并把其作为字符串列表返回】  
readline（）【读取一行，作为字符串返回】  
写入：  
print（“asd”，file=data）【屏幕标准输出：file=sys.stdout】      
data.writeline(item):【写完换行】  
write（）：【写完不换行】  

刷新输出（文件关闭）：  
Data.close()【文件不存在时错误】  
print（x，end=’ ‘）【end取消默认结尾回车】    
Print(r””)【r表示内部的字符串默认不转译】  
Print（’’’line1  
…line2  
…line3’’’）【以…为提示符进行多行输出】
print("%d*%d=%d" %(i,j,i*j))【format格式的输出】     
返回文件起始位置：data.seek（0）  
按行读取：data.readline（）【需print】  
分割：split（“：”，1）【1表示分为两部分】  
寻找：find（“：”）【找不到返回-1，找到返回索引值】  

**io模块**  
from io import StringIO()  
d=StringIO("hello world!")【在内存中写入字符串】  
print（d.getvalue()）【obj.getvalue方法读取内存中对象内容】  
【操作在内存中的字符串时，read相关方法不会将stream position归零，需要用obj.seek（0）将位置归零】  

**pprint模块**  
pprint.pprint(res)【更加美观的输出，能够从控制器的输出较直观的发现数据之间的关系】

**os模块**  
系统名称：name   
环境变量：environ   
获取环境变量：environ.get("key")  
获取进程id：os.getpid()
获得当前工作目录：getcwd（）【current working directory】    
改当前工作目录为：os.chdir（""）【change directory】  
创建目录：os.mkdir("")  
删除目录：os.rmdir（""）  
删除文件：os.remove（""）  
重命名文件：os.rename（"past name","present name"） 
列出当前目录下的所有文件和目录名：os.listdir('.') 
拆分路径：os.path.split（"/Users/michael/testdir/file.txt"）【会将最后一个/后的名称进行拆分】【[0]为需要的路径】      
当前目录的绝对路径：os.path.abspath（"."）  
表示完整路径：os.path.join("/Users/michael","testdir")【创建新路径时要用join将完整路径表示出来，再用mkdir】     
检查文件是否存在：os.path.exists(“sd.txt”)     
判断是否是目录：os.path.isdir()  
判断是否是文件：os.path.isfile()  
[x for x in os.path.isfile(x) and os.path.splitext(x)[1]=='.py']【列出当前目录下所有py文件】  
【path.splitext返回路径名和文件扩展名的元组】  

**shutil模块**  

**Pickle模块**【序列化】 【只能用于保存不重要的数据】  

    With open（“sd.txt”,“wb”）as data【b表示二进制】
	pickle.dump（obj，file）【将对象序列化保存】

    With open（“sd.txt”,“rb”）as data2
	Data3=pickle.load（data2）【反序列化读取】
	Data3=pickle.Unpickler（data2）.load()【Unpickler，反序列化,调用文件的read方法，等于上面】  

**json模块**【通用的序列化方法】  

	json.dump(obj,data,default=lambda obj:obj.__dict__)【用class自身的dict属性储存instance】  
	json.load(obj) 

## 网页处理 ##
**request模块**  
html=request.get("URL")【获取网页】  
res=html.text【将get方法中得到的源码读取并将变量指向源码】  

**urllib.request模块**  
html=urllib.request.urlopen("URL")【获取网页】  
res=html.read()【将urlopen方法中得到的源码读取并将变量指向源码】  
res=close()【将读取的数据关闭，read()后都要close()】  


## 错误处理 ##
**Try/except/finally模式  **  
    try:  
    	【需要尝试保护的代码】  
    except ValueError（IOError、AttributeError、NameError）【特定指定异常：以下代码仅解决指定的错误；不进行指定则解决所有错误】:  
    	pass【代码出现错误时运行的修正代码】  
    finally：【	在所有的代码之后运行，如关闭文件】  
      
    except IOError as err【给异常指定名称】  
    	print（“file error：”+str（err））  

**raise**  

    if not instance(value,int):
    	raise ValueError("score must be integer")
	except Exception as err:
		 err += ('more info',)【传递前对异常信息进行更新】
		raise【后面的不加异常对象时，传递异常】
【引发一个异常】

a=”abc”  
pass
【不确定写什么的时候用pass占位】  

**调试**

----------
**断言**  

    assert n!= 0, 'n is zero!'【断言n!= 0表达式为True，否则返回AssertionError：n is zero!】

**logging模块**【记录日志】  
 
    import logging
	except Exception as err:
	logging.basicConfig(level=logging.WARNING,filename="",filemode="a",format="")【纪录级别、记录文件、记录模式、记录格式%】
	logging.exception(err)【错误记录后程序继续运行】
	
日志分为五个级别【从低到高，设置级别以上的才被跟踪】：   
DEBUG：详细的信息,通常只出现在诊断问题上  
INFO：确认一切按预期运行  
WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。  
ERROR：更严重的问题,软件没能执行一些功能  
CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行  

**unittest模块**单元测试   

	import unittest
    class Dict(dict):  
    d=Dict(a=1)  

	class TestDict(unittest.TestCase)
    self.assertTure  
    self.assertEqual(d.a,1)  
    self.assertRaises(AttributeError)[断言能够抛出相应的错误]

需要测试的有init，key、attribute、error

## 进程与线程 ##
【多进程耗空间，但是节省时间，而且不容易假死】  
【多线程节省空间，但是浪费时间，且容易假死，不用跨进程边界传递信息】  
**multiprocessing模块**  

    import multiprocessing as mp
    obj=mp.Process(target=,args=())【将对象指定为子进程对象】【target指定执行函数，args指定函数传入参数】  
    obj.start()  
    obj.join(timeout)【等待子进程结束后在向下运行，用于进程间的同步】【timeout设置超时时间】
	obj.terminate（）

	mp.pool【进程池，用于启动多个子进程】
	obj = Pool(4)【限制运行的子进程量】
	obj.mp.Pool.apply_async(f,args=(","))【向进程池提交目标请求】【非阻塞】
	obj.mp.Pool.apply【阻塞】 
	obj.close()【调用close后不产生新的进程】

	mp.Queue(size)【进程间通信】
	q=Queue()
	q.put(value)【在Queue中放入数据】
	num=q.get(True)【按顺序一个一个读取Queue中数据】
	【Queue只能指定2个子进程分别进行读和写，指定后其他子进程无法进行读和写】  
	mp.cpu_count()【计算cpu的数量】
    --------------------------------------------------------------
	【分布式进程】
	import queue
	task_queue=queue.Queue()
	mp.Manager.BaseManager【分布式进程需要用到的类】
	class QueueManager(BaseManager):【只从网络上获取Queue】
		pass
	【主manager】
	QueueManager.register("get_task_queue",callable=lambda：task_queue)【register：BaseManager自带方法,将get_task_queue注册到manager中，并将其与task_queue关联】
	QueueManager.register("get_result_queue",callable=lambda:result_queue)【需要分别设置get和put的queue】
	m=QueueManager（address=（""，port），authkey=）【address，authkey：BaseManager自带属性，设置连接地址和验证码】【主机不用设置ip】
	m.start()【启动Queue】
	task=manager.get_task_queue()【设置manager中的代理序列】
	result=manager.get_result_queue()
	task.put(obj)
	r=result.get(timeout=10)
	manager.shutdown()【关闭manager】
	【分布manager】
	m=QueueMnager(address=(ip,port),authkey=)【指定manager】
	m.connect()【连接到网络相应地址的Queue】
	task=m.get_task_queue()
	result=m.get_result_queue()
	n=task.get(timeout=)
	put.result(obj)
	
**threading模块**  
	
	local=threding.local()【创建全局Threadinglocal对象】
	local.key=value【local.key对象的存入】
	obj=local.key【local.key对象的取出】
	【在LocalThread中，每一个线程都拥有对应的局部属性，即使属性相同也互不影响】

    lock=threading.Lock()【创建锁】【线程的变量共享，设置锁可以避免线程交叉改变量】
    lock.acquire()【获取锁】【当一个线程获取锁时，其他线程不能获取】【注意死锁】  
    lock.release()【释放锁】【当一个线程调用的函数结束时，需要释放锁让其他线程获取】  

    threading.current_thread().name【返回当前线程名】【主线程的线程名为Mainthread】  
    t=threading.thread(target=loop,name="LoopThread")【设置线程】  
    t.start  
    t.join  

**time模块** 
time.sleep(x)【将运行进程休眠x秒】
t=time.time（）【当前时间，可用于时间加减运算】
time.ctime()【返回当前时间】

**datetime模块** 
 
    datetime.datetime.now()【返回当前日期和时间，类型为datetime】  
    datetime.datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')【将字符串转换为datetime格式】  
	obj.strftime('format')【将datetime转换为str格式】  
    utc_dt=datetime.datetime.utcnow()【获得UTC时间】  
    
	datetime.datetime(y,m,d,h,min,sec)【构造时间，format：2015-04-19 12:20:00】  
    obj.timestamp()【将datetime类型转化为timestamp类型】  
    datetime.fromtimestamp(obj)【将timestamp转为datetime，与本地时间作转换】  
    datetime.utcfromtimestamp(obj)【与utc时间作转换】  
	tz=datetime.timezone(datetime.timedelta(hours=))【直接生成时区】【可用replace直接替换】
    now-/+datetime.timedelta(days=,hours=)【时间计算，在timedelta的参数中填入计算量】  
    
    utc_dt=datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)【设置UTC+0：00】
    bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))【转换时区】
    m=datetime.timezone(datetime.timedelta(hours=8))【创建时区UTC+8:00】  
    dt=datetime.datetime().now.replace(tzinfo=m)【强制设置UTC+8：00】  

## 对象操作 ##
dir（obj）【获得操作该对象的所有方法和属性】

**字符串**  
*：A*3-->AAA  
**Capitalize**：aASaDs .Capitalize()-->Aasads  
**Center**（居中）:str.center(width,"sep")
Str=kkk  
Str.center(5,”a”)-->akkka  
ljust（左对齐）/rjust（右对齐）  
**find**：str.find（”f”）【无值返回-1】  
**str.startswith**(“”)/.endswith()【检查字符串是否以某字符串结尾，返回bool值】  
**isalpha**【是否都是字母】/isdigit【是否都是数字】/isalnum【数字和字母混合】/isspace【空格】【非list】   
**join**：(sep).join(str.list)【一定要定义之前sep，不然"name 'join' is not define."】  
str=["aa","bb","cc"]  
print "/".join(str)-->aa/bb/cc  
**splitlines**("keepend")【按照换行符切割】  
**partition**:str.patition("sep")【只运行到第一次分割，返回三个对象：分割的子字符串、分隔符和剩余字符串】    
**strip**("sep")/lstrip()/rstrip()【从字符串两端移除空白，也可移除相应的字符串】  
**replace**：str.replace(old, new[, max])  
str = "this is string example....wow!!! this is really string";  
print str.replace("is", "was", 3);【替换不超过max次】-->  
thwas was string example....wow!!! thwas is really string    

**string模块**  
str.**maketrans()&translate（）**:  

	from string import maketrans
    trantab=str.maketrans(input,output)  `
    print (raw.translate(trantab))  
【先建立一个转换table，用maketrans设定后，用translante进行转换】  

**template()&substitute():** 
 
	from string import Template  
    s1=template(‘$who like $what’)  
    print(s1.substitute(who=’tim’,what=’kun’))  
    print(s1.safe_substitute(who=’tim’,what=’kun’))  
【safe_substitute和substitute的区别：如果输入有缺值，safe会将原值直接输出，substitute会报错】   

**预定义字符串**  

    import string  
    string.ascii_letter  
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  
    string.ascii_uppercase  
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string.ascii_lowercese  
    'abcdefghijklmnopqrstuvwxyz'

**re模块**【正则表达式模块】【Regular Expression】  
**pattern格式：**  
	. 【匹配除换行符之外的字符】  
	\d【数字：0-9】  
	\D【非数字】  
	\w【单词字符:A-Za-z0-9】  
	\s【匹配空格】  
	*【匹配前一个字符0或无限次】  
	+【匹配前一个字符1或无限次】  
	？【启用非贪婪匹配，当使用*和+时，使表达式尽可能少的匹配】
	{}【匹配前一个字符m次】【{3,8}表示3-8个数字】  
	[]【表示范围，[]内仅匹配一个数字或字符等，如[0-9a-z\_]】 
	()【用于分组，之后用group()提取分组】 
	^【匹配字符串开头，^\d表示以数字开头】  
	$【匹配字符串结尾，\d$表示以数字结尾】  
	^py$【仅匹配py】
	|【左右表达式任意匹配一个，先左后右,如（P|p）ython】  
	【特殊字符要用\进行转义，pattern使用r前缀避免内部转义】

re.match(pattern,obj)【判断obj是否符合pattern，符合返回match对象，不符合返回none】 
pattern.match(obj) 【match的为另一种写法，pattern要经过compile】
re.split(pattern,obj)【使用+】  
re.compile()【将正则表达式的字符串形式编译为re对象，可以使用r不表达转义字符】  
re.findall(pattern,str)【按照pattern开始进行匹配，并逐个返回字符串list，匹配多个】  
re.search(pattern,str)【按照pattern，从左到右，找到即返回match对象，仅匹配一个】  
re.groups(0)【提出search或match出来的字符串，1，2，3表示第几个字符串，空时提取全部】【一定记得是groups不是group】
    
**列表**  
**count**:str.count(sub, start= 0,end=len(string))【返回sub在字符串中出现的次数】  

**字典**  
**get**(key, default=None)【当键值不存在时返回default值】  
**pop**（key）  
**clear**【清除字典的内容】  

**集**  
a=set（）【设定空集】  
frozenset【不可变集，内容不可变，只支持一部分集操作】  
a={1,2,3,4,5}【注意和字典的区别】  
s.**issubset**(x)【集s是否是集x的子集，返回bool值】  
**s^x**【返回不在两者交集中的所有元素】  
**s-x**【返回在集合s中有，x没有的元素】  
**discard**【移除元素】  
**pop**【随机移除元素】 
**clear**【清除集元素】 


## 其他模块 ##
**collections模块**  
	
	【namedtuple】
    point=colections.namedtuple("point",['x','y'])
	p=point()
	p.x【'point'指定类的名称，[x,y]指定类的内容数量，存入的数值可以当做属性来调用】
	【由于tuple的不可变属性，在input后将数据存入namedtuple的类中更稳定】  
    
	【deque】
	q=collections.deque(list)
	q.popleft() / q.appendleft()
	【高效删除和添加list中的元素】
	
	【defaultdict】
	dd=collections.defaultdict(lambda: 'N/A')
	【当查找的key不存在时返回N/A，而不是KeyError】

	【OrderDict】
	dd=collections.OrderDict([('a',1),('b',2)])
	list(dd.keys())
	【按照输入顺序储存dict中的key】
	dd.popitem(last=False)【last为False时，先加入的先移除】
	dd.move_to_end(key,last=Ture)【last为True时移到末尾，False时移到开头】

	【Counter】
	c=Counter()
	for ch in "programming":
		c[ch]=c[ch]+1
	c
	【Counter也是dict的一个子类，设定key的时候，默认key的value为0】
	【Counter的默认排序是按照value降序排列】
	
	


1.用open和with打开的文件数据，需要用ReadLine或for对文件中的每一项数据进行赋值后进行读取。没读取前是一整块文件数据，python只能读分解的数据。  
2.在while和if中的条件句，判断一个值是否等价（一样），使用==（不是=）。  
3.定义函数后需要return，可以return多个结果，使用函数时也要用多个参数进行接收。  
4.str（），abs（），float（）算作是函数  
5.字典中的value一定是可以计算的float或int。  
6.生成器本身可以代表一个列表，所以用生成器进行的运算都具有map（f，[]）的效果，如generator%n==map[lambda x，y：x%y，generator]。（多用生成器，少创建列表）  
7.打开文件后，使用其中一种read()类型函数（readline、readlines、read）时，不能使用另一种read()类型函数。重开文件后可重新使用。  
8.[a-z][A-Z]表示大写字母和小写字母  
9.创建类的时候要避免实例的属性暴露、随便修改，可以使用双下划线在__init__中定义限制属性，也可以使用@property装饰器将函数作为属性调用

