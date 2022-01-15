[TOC]
# Python学习笔记
zen of python:
```pyt----------
import this
```
```pyt
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than `*right*` now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
## 基础知识

### 内容编码

python2解释器编码时采用ASCII，python3解释器采用utf8,因此用python2输出中文时会报错，应这样写：
```python
# *-* coding utf-8 -*-
print "你好世界"
```
###  注释
当行注释 `#这是当行注释`
多行注释 `'''多行注释'''` 或者 `"""被注释内容"""`

### 变量

#### 声明变量
```python
name="python"
```
python直接操作地址
#### 常量
python里面没有专门声明变量的方式，约定俗成用大写字母，e.g `AGE=56`

### 输入输出
```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
name = input("请输入用户名：")
print(name)
```
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = input("What is your name?")
age = input("How old are you?")
hometown = input("Where is your hometown?")

print("Hello ",name , "your are ", age , "years old, you came from",hometown)
```
`a,b=map(int,input().split())`    #一行输入两个数字
### 数字
Python Number 数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。

int long,Python3里不再有long
没有一个上限
`bit_length()`:用二进制的最少表示位数
```python{cmd=true}
v=11
print(v.bit_length())
```
floating point real values/complex numbers

可以用 `del` 删除对象引用
```python
val1=1
val2=1
del val1,val2
```
数据类型转换：
`int(x[,base ])`  #base代表进制
```python{cmd=true}
print(int('123',8))
```
`long(x[,base ])`转成长整数
`float(x)`转成浮点数
`complex(real [,imag ])`创建复数
```python{cmd=true}
print(complex(1,2))
val=complex(1,2)
print(val)
```
`str(x)`转成字符串
`repr(x)`转成表达式字符串
`eval(str)`用来计算在字符串中的有效Python表达式,并返回一个对象
`tuple(s)`将序列 s 转换为一个元组
`list(s)`将序列 s 转换为一个列表
`chr(x)`将一个整数转换为一个字符
`unichr(x)`将一个整数转换为Unicode字符
`ord(x)`将一个字符转换为它的整数值
`hex(x)`将一个整数转换为一个十六进制字符串
`oct(x)`将一个整数转换为一个八进制字符串

**math模块和cmath模块**
```python{cmd=true}
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cmath    #cmath主要复数
import math #math主要是浮点
print(dir(cmath))
print(dir(math))
print(cmath.sqrt(2))
a=round(3.1415926,4)
print(a)
```
随机数函数
```python{cmd=true}
import random
a=random.choice(range(10))
print(a)
a=random.randrange(1,10,2)  #2 denotes foot step
print(a)
a=random.random()   #generate x in [0,1)
print(a)
#shuffle(list):change a list
a=random.uniform(1,2)
print(a)
del a
```

`hypot(x,y)`:return $\sqrt{x^2+y^2}$
`degrees(x)`:弧度化角度；`radians(x)`:角度化弧度

### 列表(list)
```python{cmd=true}
list1=['python','java','cpp']
print list1[0]
print list1[0:3]
list1.append(1)
print list1
del list1[1]
print list1
for x in list1:
    print x
print 'python' in  list1
list1*=4
```
`cmp(list1, list2)`比较两个列表的元素
`len(list)`列表元素个数
`max(list)`返回列表元素最大值
`min(list)`返回列表元素最小值
`list(seq)`将元组转换为列表
`list.append(obj)`在列表末尾添加新的对象
`list.count(obj)`统计某个元素在列表中出现的次数
`list.extend(seq)`在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
`list.index(obj)`从列表中找出某个值第一个匹配项的索引位置
`list.insert(index, obj)`将对象插入列表
`list.pop([index=-1])`移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
`list.remove(obj)`移除列表中某个值的第一个匹配项
`list.reverse()`反向列表中元素
`list.sort(cmp=None, key=None, reverse=False)`排序

python 创建二维列表，将需要的参数写入 cols 和 rows 即可
`list_2d = [[0 for col in range(cols)] for row in range(rows)]`
`dp = [[0]*n for _ in range(m)]`
### 元组
和列表类似，但是元素不能修改
元组只包含一个元素时要加逗号 `tup1=[1,]`
不能修改但是可以拼接和整个的del

无符号对象默认是元组：
```python{cmd=true}
x,y=1,2
print x,y
```
`cmp(tuple1, tuple2)`比较两个元组元素。
`len(tuple)`计算元组元素个数。
`max(tuple)`返回元组中元素最大值。
`min(tuple)`返回元组中元素最小值。
`tuple(seq)`将列表转换为元组。
### array代替list
`import numpy`
```python{cmd=true}
import numpy as np
array1=np.zeros(10)
print array1
array1[5]=2
print (type(array1))
array2=np.arange(10,26).reshape(4,4)    #4 * 4
print array2
array3=np.sqrt(array2)
array2=np.where(array2<3,9,array2)
print (array2*array3)
```
### 字符串
加了引号就是字符串 但是里面有单引号外面要双引 多行字符串要用多引号
```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
  
poem='''
when I was young I use python
and guaguagua
'''
print(poem)
```
字符串内置+号，乘号

字符串的索引和切片：
```python{cmd=true}
a='ABCDEFG'
print(a[0])
print(a[0:3])
print(a[0:]) #the last one
print(a[0:-1]) #-1 denotes the last one
print(a[0:5:2]) #step length is 2
print(a[5:0:-2])
```
**格式化输出**
```python{cmd=true}
#!/usr/bin/python3
# -*- coding: utf-8 -*-
name = 'python'
age = 10

job = 'python'
hobbie = 'python'

info = '''
------------ info of %s -----------  
Name  : %s  #代表 name 
Age   : %d  #代表 age  
job   : %s  #代表 job 
Hobbie: %s  #代表 hobbie 
------------- end -----------------
''' %(name,name,age,job,hobbie) 

print(info)
```
查看数据类型：`print((type)name)`
input接受的数据类型默认是字符串，所以要强制转换`int(input("age:"))
`
转义%： `%%`

打印转义字符：`r'\x'`: `print r'\n'`

字符串常用方法：
```python{cmd=true}
#capitalize swapcase title
name='pYthon'
print(name.capitalize())
print(name.swapcase())
msg='hello world'
print(msg.title())
ret=msg.center(20,"*") #str.center(width, fillchar)
print(ret)
```
[懒得写了](https://www.runoob.com/python/python-strings.html)

### 布尔值 
true or false

### 运算符
`a**b`: 返回$a$的$b$次幂
`a//b`: 返回整除部分
`a<>b`: 判断两数是否不相等
`a and b` `a or b` `not(a and b)`：字面意思

优先级：`()>not>and>or`

`in not in`: 判断元素是否在字典/列表/集合

```python{cmd=true}
print('a' in 'bcvd')
print('a' in 'abcd')
```
`is`:判断是否属于同一片地址，和`==`基本一样
### `if`语句
```python{cmd=true}
AGE=48
if AGE>50:
    print('too old')
else:
    print('young')
``` 
同一级别的代码缩进要一致
多条件判断：
```python
if a>0:
    print('a=1')
elif a=0:
    print('a=0')
elif a<0:
    print('a=-1')
```
### `while`循环
```python
count=0
while count<=100:
    count+=1
    print("loop:",count)
    if count>=5:
        break
print("end")
```
while-else:如果中间没有被break中断，就会执行else的内容
```python
count=0
while count<5:
    print("loop",count)
    if count==3:
        break
    count+=1
else
    print("end")
```
### `pass`语句
pass用来占位，与continue类似
```python{cmd=true}
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 
# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter
print "Good bye!"
```
### 字典
`d={key1:value1,key2:value2}`
```python
tinydic={'name':'python','age':1}
print tinydic['name']
tinydic['class']='language'    #append element
tinydic.clear()
```
### 日期和时间
`import time`
`print time.time()`不支持1970年之前
```python{cmd=true}
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime
```
```python

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import time
 
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

```
```python{cmd=true}
import calendar
cal=calendar.month(2022,1)
print cal
```
### 函数
```python
del functionname(parameters):
    funtion_body
    return [expression]
```
可变对象和不可变对象
```python
del changeint(a)
    a=10
b=2
changeint(b)
print b     #2
del changelist(l)
    l.append([1,])
list1=[1,2,3]
changelist(list1)
print(list1)
```
关键字参数：允许传入顺序和函数声明的时候不同
```python

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )
```
不定长参数：
```python
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```
如果要给函数内的全局变量赋值，必须使用 global 语句。
匿名函数
`lambda [arg1 [,arg2,.....argn]]:expression`
`sum=lamba arg1,arg2:arg1+arg2`

### 模块
```python
from math import acos
```
`dir()`函数能显示模块内容

### 文件处理（待续）
最简单的输出方法是用print语句，你可以给它传递零个或多个用逗号隔开的表达式。此函数把你传递的表达式转换成一个字符串表达式，并将结果写到标准输出

输入: `raw_input()` `input()`:前者读取一行文本，input还可以读取一个Python表达式并输出结果

```python{cmd}
str=input()
print str
```
可以输入 `x*2 for x in range (2,10,2)`

文件读写：
`file object=open(file_name[,access_mode][,buffering]`

[access_mode](https://www.runoob.com/python/python-files-io.html)

`file.close(),file.closed() #返回布尔值,file.name(),file.mode(),file.write(),file.read()`

### 异常处理（待续）

## Python提高

### 面向对象
```python
class ClassName:
    'information og this class' #use ClassName._doc_ to see this
    class_suite
```
```python
class Employee:
    empCount=0
    def _init_(self,name,salary)
        self.name=name
        self.salary=salary
        self.empCount+=1
    def displayCount(self)
        print Employee.empCount
    def displayEmployee(self)
        print self.name,self.salary
```
empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。可以在内部类或外部类使用 Employee.empCount 访问。

self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。self代表当前对象的地址，而 `self._class_` 则指向类。

```python
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```
`getattr(obj, name[, default])` : 访问对象的属性。
`hasattr(obj,name)` : 检查是否存在一个属性。
`setattr(obj,name,value)` : 设置一个属性。如果属性不存在，会创建一个新属性。
`delattr(obj, name)` : 删除属性。
```python{cmd=true}

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
 
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__ #父类
print "Employee.__dict__:", Employee.__dict__
```
运算符重载

```python
#!/usr/bin/python
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2   #print调用了_str_的重载
```
析构：`_del_`

`__foo__`: 定义的是特殊方法，一般是系统定义名字 ，类似 `__init__()` 之类的。

`_foo`: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

`__foo`: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了

### 正则表达式
`re.match` 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。函数语法：`re.match(pattern, string, flags=0)`

`re.search` 扫描整个字符串并返回第一个成功的匹配。函数语法：`re.search(pattern, string, flags=0)`

`import re`

pattern:匹配的正则表达式
string：要匹配的字符串
flags：标志位

```python{cmd=true}
import re
str='Python is python and py'
res=re.match('P',str)
print res.group()
```