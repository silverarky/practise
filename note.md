##python 学习##

movie=["A","B","c"]  
返回当前定义所有名称的集合：locals（）  
嵌套列表：movie=["a",["b","e",["c"]],"d"]  
其中第一个数据在堆栈中的编号为0  
Print(r””)【r表示内部的字符串默认不转译】  
Print（’’’line1  
…line2  
…line3’’’）【以…为提示符进行多行输出】 

a=”abc”  
pass
【不确定写什么的时候用pass占位】  

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
**【乘方】；//【整除】；%【余数】  
divmod:divmod(12,7)-->(1,5)【整除返回商和余数的元组】  
    Import math  
    Math.pi；math.cos,sin,tan  
    Math.pi/6=30°  

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
【可以在函数内部返回字典项后，在外部定义字典名】  
d.get(“tos”,-1)【检查“tos”的key是否在dict中，不存在返回-1】  
for key，value in x【字典键，值迭代】  
### 类 ###
    Class Athlete：
    	Def__init__(self,x,y)：
    		【类的项目初始化】
    		self.x=x【普通定义变量，外部可以更改】
    		self.__y=y【类中私有变量，外部无法更改，保护数据不被更改】
    	Def tops（self）
    		【类下方法定义】【子类重新定义的函数，会将父类的函数覆盖】
    D=Athelete(x,c)【D对应self，x,c对应x，y】【定义类】
    D.tops()【类下方法调用】
    Class Athlete（list）：【继承类】【多态：继承的子类拥有父类的type（既是Athlete也是list）】
    	Def__init__(self,name)
    List.__init__([])【将继承的类初始化】
【定义的类和str、int这些type是相似的】  
对象属性和方法测试：【不知道的情况下使用，能用obj.x就不用getattr（obj,"x"）】  
hasattr(obj,"x")-->True【判断属性：是否有属性x（self.x）或方法x】  
setattr(obj,"y",19)【设定属性：obj.y=19】  
getattr(obj,"y"，404)-->19【获取属性y，如果属性不存在返回默认值404】【y也可以是类中方法，结果是获取方法】

## 数据类型 ##
Float()【转换为浮点数】  
Str()【转换为字符串】  
b=a.replace（”a”,”A”）【将字符串中的某个字符进行更改,但是变化过后a不变，只能讲变化结果赋值给其他对象】  
‘asdfghjl’[:3]-->asd【str也可以看作是一个list进行切片操作】  
Int(item,base=2)【转换为整数类型,2进制。default base=10】  
Abs()【绝对值】  
Max()；min()  
Bool()【数字只有0为false，其他为true】  
Hex()【将整数转变为16进制】  
chr（）【将ASCII码转变为字符】  
ord（）【将字符转变为ASCII码】  
换行：\n；制表符：\t  

    import types  
    type(f)==type.FunctionType
【判断是否是函数类型】
## 函数内部控制 ##
### 迭代 ###
    **for** x in movie：  
    	print（x）  
每一次迭代，x（目标标识符）的值都会顺序改变  
迭代固定次数(range和for连用)：for x in range（4）-->0,1,2,3（迭代相应次数） 
 
    num=['a','b','c']  
    for i,j in enumerate(num)  
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
from nester import lol(添加模块到当前命名空间)  

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
lazy_sum（）【称为闭包，外函数保存了内函数的变量和最后的计算值，需要调用外函数将值显示出来。在函数内定义的所用变量和内函数，在外部是无效的。】

**装饰器**

    import functools

    def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

    @log
    def now():
    	print('2015-3-25')
【装饰器也是闭包结构，一层函数用于设置装饰器的参数，二层用于返回函数，三层是具体的使用装饰的函数。设置需要装饰的函数时，使用@，相当于log（now（））】  
【functools.wrap()用于外部保存函数的名称，以便在下一级函数中使用】

### 高阶函数 ###
**Map**  
List（（map（str，[1,2,3,4,5]）））【map（）需要两个参数，第一个是计算函数名，第二个是可迭代对象。map将第二个参数中的所有元素进行迭代计算】【返回的仅是map对象，需要list（）】  
**Reduce**  

    from functools import reduce
	reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)  
【reduce（）需要参数和map（）相同，它将第二个参数中的所有元素进行累计计算】  
**filter**k=list（filter（f，[]））【f为返回bool值的函数，false时，filter将列表中的该数去掉】  
**sorted**  
sorted（[],key=f,reverse=True）【key为函数，reverse反转顺序。sorted默认升序，字符串时按照先a后z，先大写后小写排序】
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

刷新输出（文件关闭）：Data.close()【文件不存在时错误】  
print（x，end=’ ‘）【end取消默认结尾回车】  
返回文件起始位置：data.seek（0）  
按行读取：data.readline（）【需print】  
分割：split（“：”，1）【1表示分为两部分】  
寻找：find（“：”）【找不到返回-1，找到返回索引值】  
逻辑等于：==  

**os模块**  
获得当前工作目录：getcwd（）【current working directory】  
改当前工作目录为：chdir（’’）【注意加双单引】【change directory】  
检查文件是否存在：path.exists(“sd.txt”)  
列出当前目录下的所有文件和目录名：.listdir('.')  
**Pickle模块**【解决同文件数据格式不同问题】  

    With open（“sd.txt”,“wb”）as data【b表示二进制】
	pickle.dump（obj，file）

    With open（“sd.txt”,“rb”）as data2
	Data3=pickle.load（data2）
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
**isalpha**【是否都是字母】/isdigit【是否都是数字】/isalnum【数字和字母混合】【非list】  
**join**：(sep).join(str.list)  
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

**re模块**【正则表达式模块】  
**pattern格式：**  
	. 【匹配除换行符之外的字符】  
	\d【数字：0-9】  
	\D【非数字】  
	\w【单词字符:A-Za-z0-9】  
	*【匹配前一个字符0或无限次】  
	+【匹配前一个字符1或无限次】  
	{}【匹配前一个字符m次】  
	^【匹配字符串开头】  
	$【匹配字符串结尾】  
	|【左右表达式任意匹配一个，先左后右】  

re.compile()【将正则表达式的字符串形式编译为Pattern实例，可以使用r不表达转义字符】
re.findall(pattern,str)【按照pattern开始进行匹配，并逐个返回字符串list，匹配多个】  
re.search(pattern,str)【按照pattern，从左到右，找到即返回match对象，仅匹配一个】  
re.group(0)【提出search出来的字符串，0表示全部，1，2，3表示第几个字符串】  
    
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


 


  
1.用open和with打开的文件数据，需要用ReadLine或for对文件中的每一项数据进行赋值后进行读取。没读取前是一整块文件数据，python只能读分解的数据。  
2.在while和if中的条件句，判断一个值是否等价（一样），使用==（不是=）。  
3.定义函数后需要return，可以return多个结果，使用函数时也要用多个参数进行接收。  
4.str（），abs（），float（）算作是函数  
5.字典中的value一定是可以计算的float或int。  
6.生成器本身可以代表一个列表，所以用生成器进行的运算都具有map（f，[]）的效果，如generator%n==map[lambda x，y：x%y，generator]。（多用生成器，少创建列表）  
7.打开文件后，使用其中一种read()类型函数（readline、readlines、read）时，不能使用另一种read()类型函数。重开文件后可重新使用。
8.[a-z][A-Z]表示大写字母和小写字母

