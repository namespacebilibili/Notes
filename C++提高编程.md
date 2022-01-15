[TOC]



# C++提高编程

泛型编程与STL技术

# 1 模版

## 1.1 模版的概念

模版是建立通用的模具，提高复用性

·模板不可以直接使用

·模板的通用不是万能的

## 1.2 函数模板

模板机制：函数模板、类模板

### 1.2.1 函数模板语法

建立一个通用函数，其返回值类型和形参类型可以不具体制定，用一个虚拟的类型来代表

语法：

```C++
template<typename T>
函数声明或定义
```

template——声明创建模板

typename——后面的符号是数据类型，可以用class代替

T——通用的数据类型，通常用大写字母

```C++
void swapint(int &a,int &b)
{
  int temp=a;
  a=b;
  b=temp;
}
void swapfloat(float &a,float &b)
{
  float temp=a;
  a=b;
  b=temp;
}
template<typename T>
void swap(T &a,T &b)
{
  T temp=a;
  a=b;
  b=temp;
}
void test()
{
	int a=10;
  int b=20;
  swap(a,b);//编译器自己推导
  swap<int>(a,b);
}
```

### 1.2.2 函数模版注意事项

·自动类型推导必须推出一致的数据T

·模版必须确定出T的数据类型才能使用

```C++
template<typename T>
void swap(T &a,T &b)
{
  T temp=a;
  a=b;
  b=a;
}
void test()
{
	int a=10;
  int b=20;
  swap(a,b);//正确
  char c='c';
  swap(a,c);//错误
}
template<typename T>
void func()
{
  cout<<" "<<endl;
}
void func()
{
  func();//错误
  func<int>();//正确
}
```

### 1.2.3 函数模板案例

封装排序函数对不同数据类型数组排序

```C++
template<class T>
void swap(T&a,T&b)
{
  T temp=a;
  a=b;
  b=temp;
}
template<typename T>
void sort(T arr[],int len)
{
	for (int i=0;i<len;i++)
  {
    int max=i;
    for (int j=i+1;j<len;j++)
    {
      if(arr[max]<arr[j])
         {
           max=j;
         }
    }
      if (max!=i)
      {
        swap(arr[max],arr[i]);
      }
   }
}
template <typename T>
void print(T arr[],int len)
{
  for (int i=0;i<len;i++)
  {
    cout<<arr[i]<<" ";
  }
  cout<<endl;
}
void test()
{
  char chararr[]="badfce";
 	sort(chararr,sizeof(chararr)/sizeof(chararr[0]));
  print(chararr,sizeof(chararr)/sizeof(chararr[0]));
  int intarr[]={1,2,3,4,6,5};
}
```

### 1.2.4 普通函数与函数模版的区别

·普通函数调用时可发生自动类型转换（隐式转换）

·函数模版调用时，如果利用自动类型推导，不会发生隐式类型转换

·利用显示指定类型会发生

```C++
int Add(int a,int b)
{
  return a+b;
}
void test()
{
	int a=10;
  int b=20;
  cout<<Add(a,b)<<endl;
  char c='c';
  cout<<Add(a,c);//把char强转成int
}
template<class T>
T add(T a,T b)
{
  return a+b;
}
void test02()
{
  int a=10;
  char c='c';
  add(a,c);//报错
  add<int>(a,c);
}
```

### 1.2.5 普通函数和函数模版的调用规则

如果都能实现，优先调用普通函数

可以通过空模版参数列表强制调用函数模版

函数模版可以发生重载

如果函数模版可以发生更好的匹配，优先调用函数模版

```C++
void print(int a,int b)
{
  cout<<"普通"<<endl;
}
template <class T>
void print(T a,T b)
{
  cout<<"模版"<<endl;
}
void test()
{
	int a=10;
  int b=20;
  print(a,b);//普通
}
```

```C++
void print (int a,int b);
template <class T>
void print(T a,T b)
{
  cout<<"模版"<<endl;
}
void test()
{
	int a=10;
  int b=20;
  print(a,b);//报错
}
```

```C++
void print(int a,int b)
{
  cout<<"普通"<<endl;
}
template <class T>
void print(T a,T b)
{
  cout<<"模版"<<endl;
}
template <class T>
void print(T a,T b,T c)
{
  cout<<"模版2"<<endl;
}
void test()
{
	int a=10;
  int b=20;
  print(a,b);//普通
  print<>(a,b);//空模版参数列表强制调用模版
	print<>(a,b,100);
  char c='a';
  char d='c';
  print(c,b);//更匹配
}
```

### 1.2.6 模版的局限性

```C++
template<class T>
void f(T a,T b)
{
  a=b;//a和b是数组则不行
  //再比如a>b，如果a,b是自定义数据类型则不行
}
```

解决：

```C++
class Person
{
  public:
  Person(string name,int age)
  {
    this->name=name;
    this->age=age;
  }
  string name;
  int age;
};
template<class T>
bool compare(T &a,T &b)
{
  if(a==b)
  {
    return true;
  }
  else
  {
    return false;
  }
}
template<> bool compare(Person &a,Person &b)
{
  if(a.name==b.name&&a.age==b.age)
  {
    return true;
  }
  else
  {
    return false;
  }
}
void test()
{
  int a=10;
  int b=20;
  bool ret=compare(a,b);
  if(ret)
  {
    cout<<"="<<endl;
  }
  else
  {
    cout<<"!="<<endl;
  }
}
void test()
{
  Person p1("Tom",10);
  Person p2("Tom",10);
	bool ret=compare(p1,p2);
  if(ret)
  {
    cout<<"="<<endl;
  }
  else
  {
    cout<<"!="<<endl;
  }
}
```

## 1.3 类模板

### 1.3.1 类模版语法

建立一个通用类，成员数据类型可以不具体制定

```C++
class Person
{
public:
  string name;
  int age;
};
template<class Nametype,class Agetype>
class Person
{
public:
  Nametype name;
  Agetype Age;
  Person(Nametype name;Agetype age)
  {
    this->name=name;
    this->age=age;
  }
};
void test()
{
  Person<string,int> p("Tony",18);
}
```

### 1.3.2 类模版和函数模版的区别

类模版不能自动推导

类模版在模版参数列表中可以默认参数

```C++
template<class Nametype,class Agetype=int>
class Person
{
public:
  Nametype name;
  Agetype Age;
  Person(Nametype name;Agetype age)
  {
    this->name=name;
    this->age=age;
  }
};
void test()
{
  Person p("孙悟空",1000);//错误
  Person p<string>("RB",18);//可
}
```

### 1.3.3 类模版中成员函数创建时机

普通类中成员函数一开始就能创建

类模版成员函数调用时才能创建

```C++
class Person1
{
  public:
  void showPerson1()
  {
    cout<<"Person 1"<<endl;
  }
};
class Person1
{
  public:
  void showPerson1()
  {
    cout<<"Person 2"<<endl;
  }
};
template<class T>
class Class
{
public:
  T obj;
  void func()
  {
    obj.showPerson1();//未确定obj时不会创建
  }
  void  func2()
  {
    obj.showPerson2();
  }
};
```

### 1.3.4 类模版对象做函数参数

指定传入类型

参数模版化

整个类模版化

```C++
template<class T1,class T2>
class Person
{
public:
  Person (T1 name,T2 age)
  {
    this->name=name;
    this->age=age;
  }
  void showinfo()
  {
    cout<<this->name;
    cout<<this->age;
    T1 name;
    T2 age;
  }
};
void printperson(Person<string,int>&p)//指定参数类型
{
  p.showinfo();
}
template<class T1,class T2>//参数模版化
void print2(Person<T1,T2> &p)
{
  p.showinfo();
  cout<<typeid(T1).name()<<endl;
}
template<class T>
void print3(T)//整个类模版化；
{
  p.showinfo();
  cout<<typeid(T).name();
}
void test01()
{
  Person<string,int> p("Tony,18");
  printperson(p);
}
void test02()
{
	Person<string,int> p("Tony,18");
  print2(p);
}
void test03()
{
  Person<string,int> p("wesley",18);
  print3(p);
}
```

### 1.3.5 类模版与继承

子类继承的父类是模版时必须指定T

如果灵活，子类也需为类模版

```C++
template<class T>
class Base
{
  T m;
};
class Son:public Base<int>//不指定时为错
{
  
};
template<class T2,class T1>
class Son2:public Base<T2>//类模版
{
  T1 obj;
};
void test()
{
  Son2<int,char>s2;
}
```

### 1.3.6 类模版成员函数类外实现

```C++
template<class T1,class T2>
class Person
{
public:
  Person(T1 name,T2 age);
  void showperson();
  T1 name;
  T2 age;
};
template<class T1,class T2>
Person<T1,T2>::Person(T1 name,T2 age)
{
		this->name=name;
    this->age=age;
}
template<class T,class T2>
void Person<T1,T2>::showperson()
{
    cout<<this->name<<endl;
    cout<<this->age<<endl;
}
```

### 1.3.7 类模版分文件编写

类模版中成员函数创建时在调用阶段，分文件编写时链接不到

person. hpp:

```C++
#pragema once
#include<iostream>
using namespace std;
#include <string>
template<class T1,class T2>
class Person
{
public:
  Person(T1 name,T2 age);
  T1 name;
  T2 age;
};
  
```

person.cpp

```C++
#include "person.hpp"
//或 #include "person.cpp"	
template<class T1,class T2>
Person<T1,T2>::Person(T1 name,T2 age)
{
  
}
```

### 1.3.8 类模版和友元

全局函数类内实现：直接在类内声明友元

类外：让编译器提前知道全局函数

```C++
template<class T1,class T2> class Person;
template<class T1,class T2> void printperson2(Person<T1,T2> p)
{
    cout<<p.age<<endl;
    cout<<p,name<<endl;
}
template<class T1,class T2>
class Person
{
  friend void printperson<>(Person<T1,T2>p)
  {
    cout<<p.age<<endl;
    cout<<p,name<<endl;
  }
  friend void printperson2(Person<T1,T2> p);
  public:
  Person(T1 name,T2 age)
  {
    this->name=name;
    this->age=age;
  }
  private:
  T1 name;
  T2 age;
};
void test()
{
  Person<string,name>p("Tony",20);
 	printperson(p);
}
void test2()
{
  Person<string,name>p("Tony",20);
 	printperson2(p);
}
```

### 1.3.9 类模版案例

# 2 STL初识

## 2.1 STL诞生

C++面向对象和泛型编程思想目的是复用性提升

数据结构和算法的标准：STL

## 2.2 STL基本概念

STL：standard template library

STL广义上分为：容器(container)、算法(algorithm)、迭代器(iterator)

容器与算法之间通过迭代器衔接

STL几乎所有的代码都采用了模版类或者模版函数

## 2.3 STL组件

容器 算法 迭代器 仿函数 适配器（配接器）空间配置器

容器：各种数据结构,如vector list deque set map,来存放数据

算法：sort find copy for_each etc.

迭代器：容器与算法的胶合剂

仿函数：行为类似函数，可作为算法的某种策略

适配器：一种用来修饰容器或者仿函数或迭代器接口的东西

空间配置器：负责空间的配置和管理

## 2.4 STL中容器、算法、迭代器

**容器：**将运用最广泛的一些数据结构实现

比如数组、链表、树、栈、队列、集合、映射表

序列式容器：强调值的排序，每个元素都有固定的位置

关联式结构：二叉树结构，没有严格的物理顺序关系

**算法：**有限的步骤逻辑或数学解决问题algorithm

质变算法：运算过程会更改区间内的元素内容：拷贝、替换、删除

非质变算法：不会改变，查找计数遍历等

**迭代器**：提供一种方法使之能依序寻访某个容器的各个元素，而又无需暴露容器内部的表示方式

每个容器都有专属迭代器

使用类似指针，可以先理解成指针

| 种类           | 功能                             | 支持运算                               |
| -------------- | -------------------------------- | -------------------------------------- |
| 输入迭代器     | 只读访问                         | 只读，支持++、==、！=                  |
| 输出迭代器     | 只写访问                         | 只写，支持++                           |
| 前向迭代器     | 读写操作，并且能向前推动迭代器   | 读写，支持++、==、！=                  |
| 双向迭代器     | 读写操作，并且能向前或是向后操作 | 读写，支持++、—                        |
| 随机访问迭代器 | 读写操作，跳跃方式访问任意数据   | 读写，支持++、–、[n]、-n、<、<=、>、>= |

常用容器迭代器是后两个

## 2.5 容器算法迭代器初识

最常用的容器是vector，可以理解成数组

### 2.5.1 vector存放内置数据类型

```C++
#include<vector>
#include<algorithm>
void print(int val)
{
cout<<val<<endl;
}
void test()
{
	vector<int> v;
  v.push_back(10);
  vector<int>::iterator itBegin=v.begin();//起始iterator，指向第一个元素
  vector<int>::iterator itEnd=v.end();//结束iterator，指向最后一个元素的下一个位置
  while(itBegin！=itEnd)
  {
    cout<<*itBegin<<endl;
    itBegin++;
  }
  //or
  for(vector<int>::itetator it=v.begin();it!=v.end();it++)
  {
    cout<<*it<<endl;
  }
  //or
  for_each(v.begin(),v.end(),print);
}
```

### 2.5.2 vector存放自定义数据类型

```C++
#include<vector>
class Person
{
  public:
  Person(string Name,int Age)
  {
		this->name=Name;
    this->age=Age;
  }
	string name;
  int age;
};
void test()
{
  vector<Person>v;
  Person p1("RB",10);
  Person p2("rb",18);
  v.push_back(p1);
  v.push_back(p2);
  for(vector<Person>::itetator it=v.begin();it!=v.end();it++)
  {
    cout<<(*it).name<<endl;
    cout<<(*it).age<<endl;//or it->name
  }
}
void test2()
{
  vector<Person*>v;
  Person p1("RB",10);
  Person p2("rb",18);
  v.push_back(&p1);
  v.push_back(&p2);
  for(vector<Person*>::iterator if=v.begin();it!=v.end();it++)
  {
		cout<<(*it)->name<<endl;
  }
}
```

### 2.5.3 vector容器嵌套容器

```C++
#include<vector>
void test()
{
  vector<vector<int>>v;
  vector<int> v1;
  vector<int> v2;
  for (int i=0;i<2;i++)
  {
    v1.push_back(i+1);
    v2.push_back(i+2);
  }
  v.push_back(v1);
  v.push_back(v2);
  for(vector<vector<int>>::iterator it=v.begin();it!=v.end();it++)
  {
    for(vector<int>::iterator vit=*it.begin();vit!=(*it).end();vit++)
    {
      cout<<*vit<<" ";
    }
    cout<<endl;
  }
}
```

# 3 STL-常用容器

## 3.1 string容器

### 3.1.1 string基本概念

Char *是指针，string是类，封装char\*,管理这个字符串，是一个char *型容器

string内部成员方法：find copy delete replace insert

String管理char*分配的内

### 3.1.2 string构造函数

构造函数原型：string();string（const char* s);string(const string&str);string(int n,char c)

```C++
#include<string>
void test()
{
		string s1;
  	const char * str="hello world";
  	string s2(str);
  	string s3(s2);
  	string s4(10,'a');
}
```

### 3.1.3 string赋值操作

String& operator=(const char* str)

String& operator=(const string &s)

string& operator=(char c)

string& assign(const char *s)

String& assign(const char *s,int n)//前n个字符

String& assign(const string&s)

string& assign(int n, char c)

```C++
void test()
{
	string str1;
  str1="hello world";
  string str2=str1;
  string str3='c';
  string str4;
  str4.assign("hello world");
  string str5;
  str5.assign("hello world",5);
  string str6;
  str6.assign(str2);
  string str7;
  str7.assign(5,'c');
}
```

### 3.1.4 string字符串拼接

String& operator+=(const char* str)

String& operator+=(const string &s)

string& operator+=(const char c)

string& append(const char *s)

String& append(const char *s,int n)//前n个字符

String& append(const string&s)

string& append(const string &s,int pos,int n)//从pos开始截取n个

```C++
void test()
{
  string str1="RB";
  stl1+="lang";
  str1+=':';
  string str2="definitely";
  str1+=str2;
  string str3="I";
  stl3.append("love");
  str3.append("game adash",4);
  str3.append(str2);
  str3.append(str2,0,3);
}
```

### 3.1.5 string查找和替换

```c++
void test1()
{
	string str1="hello world";
  int pos=str1.find("ld");//默认值pos=0;没有会返回-1;find找第一次出现位置
  if(pos==-1)
  {
    cout<<"未找到"<<endl;
  }
  else
  {
    cout<<pos<<endl;
  }
  pos=str1.rfind("ld");//rfind找最后一次（从右往左)
}
void test02()
{
  string str2="acdefg";
  str2.replace(1,3,"1111");
}
```

### 3.1.6 string字符串比较

按字符的ASCll码

= return 0;> return 1;< return -1

Int compare(const string &s/const char *s) const;

```c++
void test()
{
  string str1="hello";
  string str2="hello";
  if(str1.compare(str2)==0)
  {
    cout<<"="<<endl;
  }
}
```

### 3.1.7 string单个字符存取

Char& operator[](int n)

Char& at(int n)

```C++
void test()
{
  string str="hello";
  for(int i=0;i<str.size();i++)
  {
    cout<<str[i]<<" ";
  }
  cout<<endl;
  for(int i=0;i<str.size();i++)
  {
    cout<<str.at(i)<<" ";
  }
  cout<<endl;
  str[0]='x';
}
```

### 3.1.8 string插入和删除

insert erase

```C++
void test()
{
  string str="hello";
  str.insert(1,"111");
  str.erase(1,3)//1开始删3个
    
}
```

### 3.1.9 string子串

substr()

```C++
void test()
{
  string str="abcdef";
  string Substr=str.substr(1,3);//bcd
}
void test02()
{
  string email="hello@sina.com"<<endl;
  int ret=email.find('@');
  string name=email.substr(0,ret);
}
```

## 3.2 vector 容器

### 3.2.1 vector基本概念

vector数据结构与数组类似，也称为单端数组

数组是静态空间而vector可以动态扩展

动态扩展：找更大的内存空间，然后将所有原数据拷贝并释放原有空间

### 3.2.2 vector构造函数

`vector<T> v;`

`vector(v.begin(),v.end())，将[]区间内的元素拷贝给自身`

`vector(n,elem)`;

`vector(const vector &vec)`;

```C++
#include<vector>
void print(vector<int>&v)
{
  for(vector<int>::iterator it=v.begin();it!=v.end();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  vector<int> v1;
  v1.push_back(1);
  v1.push_back(2);
  print(v1);
  vector<int>v2(v1.begin(),v1.end());
  print(v2);
  vector<int>v3(10,100);
  print(v3);
  vector<int>v4(v3);
}
```

### 3.2.3  vector赋值操作

重载等号/`assign（beg,end)`/`assign (n,elem)`

```C++
#include<vector>
void print(vector<int>&v)
{
  for(vector<int>::iterator it=v.begin();it!=v.end();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  void<int> v1;
  for(int i=0;i<q0;i++)
  {
    v1.push_back(i);
  }
  print(v1);
  vector<int> v2=v1;
  vector<int> v3;
  v3.assign(v1.begin(),v1.end());
  print(v3);
  vector<int> v4;
  v4.assign(10,100);
}
```

### 3.2.4 vector容量和大小

`empty()`

`capacity()//容量 `

`size()//元素个数` 

`resize(int num)//重定长度`

`resize（int num,elem)//以elem替换`
```C++
#include<vector>
void print(vector<int>&v)
{
  for(vector<int>::iterator it=v.begin();it!=v.end();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  vector<int> v1;
  for(int i=0;i<10;i++)
  {
    v1.push_back(i);
  }
  if(v1.empty())
  {
    cout<<"empty"<<endl;
  }
  else
  {
    cout<<"not empty"<<endl;
    cout<<v1.capacity()<<endl;//13
    cout<<v1.size()<<endl;
  }
  v1.resize(15);//默认以零填充
  v1.rezize(15,3);
}
```

### 3.2.5 vector插入和删除

`push_back pop_back insert(const_iterator pos,ele) erase clear`

```C++
#include<vector>
void print(vector<int>&v)
{
  for(vector<int>::iterator it=v.begin();it!=v.begin();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  vector<int> v1;
  for(int i=0;i<10;i++)
  {
    v1.push_back(i);
  }
  print(v1);
  v1.pop_back()
  print(v1);
  v1.insert(v1.begin(),100); //v1.begin()->v1[0]
  print(v1);
  v1.insert(v1.begin(),2,1000);//参数是迭代器
  print(v1);
  v1.erase(v1.begin()); //在头部擦除一个元素
  print(v1);
  v1.erase(v1.begin(),v1.end()); //从头到尾全删掉,v.end()代表最后一个元素的下一个元素
  v1.clear();
}
```

### 3.2.6 vector数据存取

`at(int index)`

`Operator[]`

`front()`

`b`ack()`

```c++
#include<vector>
void test()
{
  void<int> v1;
  for(int i=0;i<10;i++)
  {
    v1.push_back(i);
  }
  for(int i=0;i<v1.size();i++)
  {
    cout<<v1.[i]<<" ";//or v1.at(i)
  }
  cout<<endl;
  cout<<v1.front()<<v1.back()<<endl;
}
```

### 3.2.7 vector互换容器

`swap（vec)`

```C++
#include<vector>
void print(vector<int>&v)
{
  for(vector<int>::iterator it=v.begin();it!=v.begin();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  void<int> v1;
  for(int i=0;i<10;i++)
  {
    v1.push_back(i);
  }
  vector<int> v2;
  for(int i=10;i>0;i--)
  {
    v2.push_back(i);
  }
  v1.swap(v2);
  print(v1);
  print(v2);
}
void praticaluse()
{
  vector<int> v;
  for(int i=0;i<10000;i++)
  {
    v.push_back(i);
  }
 	cout<<v.capacity()<<endl;
  cout<<v.size()<<endl;
  v.resize(3);
  cout<<v.capacity();//浪费capacity
  //swap收缩内存
  vector<int>(v).swap(v);
  cout<<v.capacity()<<endl;//vector<int>(v)匿名对象调用拷贝构造函数
}
```

### 3.2.8 vector预留空间

减少动态扩展的扩展次数

`reserve(int len)`;

```C++
#include<vector>
void test()
{
  void<int> v1;
  v.reserve(100000);//预留空间
  int num;
  int *p=NULL;
  for(int i=0;i<100000;i++)
  {
    v1.push_back(i);
    if(p!=&v[0])
    {
      p=&v[0];
      num++;
    }//判断开辟过几次
  }
 
}
```



## 3.3 deque容器

### 3.3.1 deque容器基本概念

双端数组，可对头部删除和插入

deque访问头部比vector快，vector访问内部快

deque内部有中控器，维护缓冲区地址

### 3.3.2 deque构造函数

类vector

```C++
#include<deque>
void print(deque<int>&d)//若想防止其被修改，迭代器改为const_iterator
{
  for(deque<int>::iterator it=d.begin();it!=d.begin();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  deque<int> d1;
  for(int i=0;i<10;i++)
  {
		d1.push_back(i);
  }
  print(d1);
  deque<int> d2(d1.begin(),d1.end());
  deque<int> d3(d2);
}
```

### 3.3.3 deque赋值操作

类vector

```C++
#include<deque>
void test()
{
  void print(deque<int>&d)//若想防止其被修改，迭代器改为const_iterator
{
  for(deque<int>::iterator it=d.begin();it!=d.begin();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
  deque<int> d1;
  for(int i=0;i<10;i++)
  {
    d1.push_back(i);
  }
  print(d1);
  deque<int> d2=d1;
  print(d2);
  deque<int> d3;
  d3.assign(d1.begin(),d1.end());
  deque<int> d4;
  d4.assign(10,100);
}
```

### 3.3.4 deque大小操作

同vector，除了无capacity

### 3.3.5 deque插入和删除

```C++
#include<deque>
void test()
{
  deque<int> d1;
  d1.push_back(10);
  d1.push_front(20);
  d1.pop_back();
  d1.pop_front();
  d1.clear();
  d1.push_back(10);
  d1.push_back(20);
  d1.insert(d1.begin(),1,100);
  deque<int> d2;
  d2.push_back(10);
  d2,push_back(200);
  d1.insert(d1.begin(),d2.begin(),d2.end());
  d1.erase(d1.begin());
}
```

### 3.3.6 deque数据存取

```C++
#include<deque>
void test()
{
  deque<int> d;
  d.push_back(10);
  d.push_back(20);
  for(i=0;i<d.size();i++)
  { 
    cout<<d[i];
    cout<<d.at(i);
  }
  cout<<d.front()<<d.back()<<endl;
}
```

### 3.3.7 deque排序

```C++
#include<deque>
#include<algorithm>
void test()
{
	deque<int> d;
  d.push_back(20);
  d.push_front(30);
  sort(d.begin(),d.end());//升序,vector也可以,迭代器随机访问即可
}
```

## 3.4 案例

## 3.5 stack容器

### 3.5.1 stack基本概念

先进后出结构，只有一个栈顶出口

[^FILO]: First in Last Out

栈中只有顶端的元素才能被外界访问，因此不允许有遍历行为

但可以返回size和empty//进的时候就记录num++

进入push出栈pop

### 3.5.2 stack常用接口

构造函数 赋值= push(elem) pop() top() empty() size()

## 3.6 queue容器

### 3.6.1 queue基本概念

先进先出，队列型排列

[^FIFO]: First In First Out

只能使用队头和队尾，不能遍历，push pop

### 3.6.2 queue常见接口

构造函数 =赋值 
`push(elem)//入队(从队尾入队) `
`pop()//队头出去` 
`back()//调用最后一个元素` 
`front()//调用最前面一个元素` 
`empty()//是否为空 size()//大小`

## 3.7 list容器

### 3.7.1 list基本概念

功能：数据链式存储，物理单元非连续，数据的逻辑顺序通过指针链接

链表由一系列结点组成

结点：存储数据的数据域，存储下一个结点地址的指针域

STL的链表是双向循环链表

对任意位置进行快速插入或删除元素，但遍历速度不如数组，占用空间大

list的迭代器是双向迭代器

list采用动态存储分配，不会造成内存浪费和溢出

### 3.7.2 list构造函数

基本一样

```C++
#include<list>
void print(const list<int> &l)
{
  for(list<int>::const_iterator it=l.begin();it!=l.end();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
void test()
{
	list<int> l1;
  l1push_back(10);
  l1.push_back(20);
  print(l1);
  list<int> l2(l1.begin(),l1.end());
  list<int> l3(l2);
  list<int> l3(10,1000);
}
```

### 3.7.3 list赋值和交换

```C++
#include<list>
void test()
{
  list<int> L1;
  L1.push_back(10);
  L2.push_back(20);
  list<int> L2=L1;//operater=
  L2.assign(L1.begin(),L1.end());
  L2.assign(10,1000);
  L1.swap(L2);
}
```

### 3.7.4 list大小操作

size() empty() resize(num) resize(num,elem)

```c++
#include<list)
void test()
{
  list<int> L1;
  L1.push_back(10);
  L1.push_back(20);
  if(L1.empty())
  {
    cout<<"list is empty"<<endl;
  }
  else
  {
    cout<<"not empty"<<endl;
    cout<<L1.size();
  }
 	L1.resize();
}
```

### 3.7.5 list插入和删除

remove（elem):删除与elem一样的数据

```C++
#include<list>
void test()
{
	list<int> L1;
  L1.push_back(10);
  L1.push_front(1200);
  L1.pop_back();
  L1.pop_front();
  L1.insert(L1.begin(),10000);
  L1.push_back(10);
  L1.push_back(20);
  list<int>::itereator it=L1.begin();
  it++;
  L1.erase(++it);
  L1.remove(20);
}
```

### 3.7.6 list数据存取

只有front（）back（），不能[]、at()

### 3.7.7 list反转和排序

reverse sort

```C++
#include<algorithm>
bool compare(int v1,int v2)
{
  //降序：第一个数大于第二个
  return v1>v2;
}
void test()
{
  list<int> L1;
  L1.push_back(10);
  L1.push_back(20);
  L1.reverse();
  sort(L1.begin(),L1.end());//报错，不支持随机访问的迭代器不能用标准算法,而内部会提供成员函数
  L1.sort();//升序
  L1.sort(compare);//降序
}
```

### 3.7.8 排序案例

## 3.8 set/multiset容器

### 3.8.1 set基本概念

所有元素会自动被排序

关联式容器，底层用二叉树实现

set不允许重复，multiset允许重复

### 3.8.2 set构造与赋值

```C++
#include<set>
void test()
{
  set<int> s1;
  //只能insert插入
  s1.insert(10);
  s1.insert(20);
  set<int> s2(s1);
}
```

### 3.8.3 set大小与交换

### 3.8.4 set插入和删除

erase（elem)//删elem

### 3.8.5 set查找和统计

Find(key)//若存在返回迭代器，不存在返回end

count（key)

```C++
void test()
{
  set<int> s1;
  s1.insert(10);
  s1.insert(20);
  set<int>::iterator pos=s1.find(30);
  if(pos==s1.end())
  {
    cout<<"未"<<endl;
  }
  else
  {
    cout<<*pos<<endl;
  }
  int num=s1.count(10);
  cout<<num<<endl;//set只会是0/1
}
```

### 3.8.6 set和multiset的区别

set插入时会检测重复

```C++
#include<set>
void test()
{
	set<int> s;
  s.insert(10);
  s.insert(20);
  pair<set<int>::iterator,bool> ret=.s.insert(10);//返回一个bool值和pos
  if(ret.second())
  {
    cout<<"inserted successfully"<<endl;
  }
  multiset<int> s1;
  s1.insert(10);//只会返回迭代器
  
}
```

### 3.8.7 pair对组

返回两个数据	

pair<type,type> p=make_pair();

pair<type,type> p();

```C++
void test()
{
  pair<int,string> p(18,"RB");
  cout<<p.first<<endl;
  cout<<p.second<<endl;
  pair<int,string> p2=make_pair(18,"RB");
}
```

### 3.8.8 set排序

利用仿函数改变排序规则

```C++
#include<set>
class Compare
{
 public:
  bool operator()(int v1,int v2) const
  {
    return v1>v2;
  }
};
void test()
{
  set<int,Compare> s1;
  s1.insert(10);
  s1.insert(20);
  s1.insert(30);
}
```

```C++
#include<set>
class Person
{
  public:
  string Name;
  int Age;
  Person(string name,int age)
  {
    this->Name=name;
    this->Age=age;
  }
}
class Compare{
public:
  bool operator()(const Person &p1,const Person &p2){
    return p1.age>p2.age;
  }
};
void test()
{
  set<Person> s;
  Person p1("RB",18);
  Person p2("rb",29);
  s.insert(p1);
  s.insert(p2);
}
```

## 3.9 map/multimap容器

### 3.9.1 map基本概念

map所有元素都是pair，pair中第一个元素为key值，起索引作用，第二个元素是value

根据键值自动排序

关联式容器，底层结构二叉树

可以根据key值找到value值

map不能重复，multimap可以重复key值

### 3.9.2 map构造和赋值

```C++
#include<map>
void test()
{
  map<int,int> m;
  m.insert(pair<int,int>(1,10));
  m.insert(pair<int,int>(2,20));
  for(map<int,int>::iterator it=m.begin();it!=m.end();it++)
  {
    cout<<(*it).first<<endl;
    cout<<it->second<<endl;
  }
}
```

### 3.9.3 map大小和交换

size empty swap

### 3.9.4 map插入和删除

```C++
#include<map>
void test()
{
  map<int,int> m;
  m.insert(pair<int,int>(1,10));
  m.insert(make_pair(2,10));
  m.insert(map<int,int>::value_type(3,10));
  m[4]=40;//不建议,用途是用键值访问value
  m.erase(m.begin());
  //m.erase(m.begin(),m.end());
  m.insert(pair<int,int>(1,10));
  m.erase(1);
  m.clear();
}
```

### 3.9.5 map查找和统计

```C++
#include<map>
void test()
{
  map<int,int> m;
  m.insert(make_pair(1,10));
  m.insert(make_pair(2,20));
  map<int,int>::iterator mit=m.find(1);
  if(mit==m.end())
  {
		cout<<"don't exist"<<endl;
  }
  else
  {
    cout<<"find it,pos is"<<it->first;
  }
  cout<<m.count(2)<<endl;//0 or 1
}
```

### 3.9.6 map排序

```C++
class Compare
{
  public:
  bool operator()(int m1,int m2) const
  {
    return m1>m2;
  }
};
void test()
{
  map<int,int,Compare> m;
  m.insert(make_pair(1,10));
  m.insert(make_pair(2,20));
}
```

## 3.10 案例

# 4 函数对象

### 4.1.1 函数对象概念

重载operator的类，对象常称为函数对象

函数对象使用（）类似函数调用，称作仿函数 

### 4.1.2 函数对象使用

可以像普通函数那样调用，可以有参数，可以返回值

函数对象超出普通函数概念：可以有自己的状态

函数对象可以作为参数传递

```C++
#include<string>
class Add
{
  public:
  int operator()(int s,int b)
  {
    return s+b;
  }
};
class Print
{
  public:
  Print()
  {
    this->count=0;
  }
  void operator()(string name)
  {
    cout<<name;
    this->count++;
  }
  int count;
};
void test()
{
	Add add;
  cout<<add(10,10);
  Print print;
  print("RB");
  print("rb");
  cout<<Print.count<<endl;
}
void doprint(Print &p,string name){p(name);}
void test02()
{
  Print print;
  doprint(print,"rB");
}
```

## 4.2 谓词

### 4.2.1 谓词概念

返回bool类型的仿函数叫谓词

operator接受一个参数叫一元谓词，两个叫二元谓词

### 4.2.2 一元谓词

```C++
#include<algorithm>
class Five
{
  public:
  bool operator()(int val)
  {
    return val>5;
  }
};
void test()
{
  vector<int> v;
  for(int i=0;i<10;i++)
  {
    v.push_back(i);
  }
  //查找有无大于五的数据
  vector<int>::iterator it=find_if(v.begin(),v.end(),Five());//Five（）匿名函数对象
  if(it==v.end())
  {
    cout<<"nop"<<endl;
  }
  else
  {
    cout<<*it<<endl;
  }
}
```

### 4.2.3 二元谓词

```C++
#include<algorithm>
class Compare
{
  public:
  bool operator()(int val1,int val2)
  {
    return val1>val2;
  }
};
void test()
{
  vector<int> v;
  for(int i=0;i<10;i++)
  {
    v.push_back(i);
  }
  sort(v.begin(),v.end(),Compare());
  for(vector<int>::iterator it=v.begin();it!=v.end();it++)
  {
    cout<<*it<<" ";
  }
  cout<<endl;
}
```

## 4.3 内建函数对象

### 4.3.1 内建函数对象意义

算数仿函数 关系仿函数 逻辑仿函数

### 4.3.2 算数仿函数

实现四则运算 negate是一元运算，其他是二元运算

```C++
#include<functional>
void test()
{
  negate<int> n;
  cout<<n(50);//-50
  plus<int> p;
  cout<<p(10,20);
}
```

### 4.3.3 关系仿函数

equal not_equal greater etc.

```C++
#include<functional>
#include<algorithm>
void test()
{
	vector<int> v;
  v.push_back(10);
  v.push_back(20);
  sort(v.begin(),v.end(),greater<int>());
}
```

### 4.3.4 逻辑运算符

logical_and logical_or logical_not

```C++
#include<fucntional>
#include<algorithm>
void test()
{
  vector<bool> v;
  v.push_back(true);
  v.push_back(false);
  vector<bool> v2;
  v2.resize(v);
  transform(v.begin(),v.end(),v2.begin(),logical_not<bool>());
  
}
```

# 5 STL-常用算法

algorithm numeric functional

## 5.1 常用遍历算法

for_each transform

### 5.1.1 for_each

```C++
#include<algorithm>
void print(int val)
{
  cout<<val<<" ";
}
class Print
{
 public:
  void operator()(int val)
  {
    cout<<val<<" ";
  }
};
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  for_each(v.begin(),v.end(),print);//函数名
  for_each(v.begin(),v.end(),Print());//匿名对象
}
```

### 5.1.2 transform

```c++
#include<algorithm>
class Transform
{
  public:
  int operator()(int v){return v+100;}
};
void test()
{
  vector<int> v;
  for(int i=0;i<10;i++)
  {
    v.push_back(i);
  }
  vector<int> target;
  target.resize(v.size());
  tranform(v.begin(),v.end(),targrt.begin(),Tranform());
}
```

## 5.2 常用查找算法

Find find_if adjacent_find binary_find count count_if

### 5.2.1 find

查找指定元素，返回迭代器，找不到则返回end

find（iterator beg,iterator end, value)

```C++
#include<algorithm>
class Person
{
  public:
  Person(string Name)
  {
    this->name=Name;
  }
  string name;
  bool operator==(const Person &p)
  {
    if(this->name==p.name){return true;}
    else{return false;}
  }
};
void test01()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int>::iterator it=find(v.begin(),v.end(),5);
  if(it==v.end())
  {
    cout<<"nop"<<endl;
  }
  else
  {
    cout<<*it<<endl;
  }
}
void test()
{
  vector<Person> v;
  Person p1("rb");
  Person p2("rb");
  v.push_back(p1);
  v.push_back(p2);
  vector<Person>::iterator it=find(v.begin(),v.end(),p2);
  if(it==v.end())
  {
    cout<<"nop"<<endl;
  }
  else
  {
    cout<<(*it).name<<endl;
  }
}
```

### 5.2.2 find_if 

Find_if(iterator beg,iterator end,Pred)

```C++
class Greaterfive
{
  public:
  bool operator()(int val)
  {
    return val>5;
  }
};
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int>::iterator it=find_if(v.begin(),v.end(),Greaterfive());
  if(it==v.end())
  {
    cout<<"nop"<<endl;
  }
  else
  {
    cout<<*it<<endl;
  }
}
class Person
{
  public:
  Person(string Name,int Age)
  {
    this->name=Name;
    this->age=Age;
  }
  string name;
};
class Twenty
{
  public:
  bool operator()(Person &p)
  {
    return p.age>20;
  }
};
void test02()
{
  vector<Person> v;
  Person p("rb",18);
  Person p2("RB",18);
  v.push_back(p);
  v.push_back(p2);
  vector<Person>::iterator it=find_if(v.begin(),v.end(),Twenty());
  if(it==v.end())
  {
    cout<<"nop"<<endl;
  }
  else
  {
    cout<<(*it).name<<endl;
  }
}
```

### 5.2.3 adjacent_find 

查找相邻重复元素

```C++
#include<algorithm>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int>::iterator it=adjacent_find(v.begin(),v.end());
  if(it==v.end())
  {
    cout<<"nop"<<endl;
  }
  else
  {
    cout<<(*it).name<<endl;
  }
}
```

### 5.2.4 binary_search 

返回true和false

在无序序列中不能用

```C++
#include<algorithm>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  bool flag=binary_search(v.begin(),v.end(),5);
}
```

### 5.2.5 count

```C++
#include<algorithm>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  int num=count(v.begin(),v.end(),10);
  cout<<num<<endl;
}
class Person
{
  public:
  Person(string Name,int Age)
  {
    this->name=Name;
    this->age=Age;
  }
  string name;
  int age;
  bool operator==(const Person &p)
  {
    return p.name==this->name&&p.age==this->age;
  }
};
void test02()
{
  vector<Person> v;
  Person p("rb",18);
  Person p2("RB",18);
  v.push_back(p);
  v.push_back(p2);
  Person RB("Rb",18)
  int num=count(v.begin(),v.end(),RB);
}
```

### 5.2.6 count_if 

谓词

```C++
class Ten
{
  public:
  bool operator()(int val)
  {
    return val>20;
  }
};
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  int num=count_if(v.begin(),v.end(),Ten());
}
class Person
{
  public:
  Person(string Name,int Age)
  {
    this->name=Name;
    this->age=Age;
  }
  string name;
  int age;
  bool operator==(const Person &p)
  {
    return p.name==this->name&&p.age==this->age;
  }
};
class Twentyyear
{
  public:
  bool operator()(const Person &p)
  {
    return p.name>20;
  }
};
void test02()
{
  vector<Person> v;
  Person p("rb",18);
  Person p2("RB",18);
  v.push_back(p);
  v.push_back(p2);
  int num=count_if(v.begin(),v.end(),Twentyyear());
}
```

## 5.3 常用排序算法

sort random_shuffle merge reverse

### 5.3.1 sort

```C++
#include<algorithm>
#include<functional>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
	sort(v.begin(),v.end(),greater<int>);
}
```

### 5.3.2 random_shuffle

```C++
#include<algorithm>
#include<ctime>
void test()
{
  srand((unsigned time)time(NULL));
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  random_shuffle(v.begin(),v.end());
}
```

### 5.3.3 merge

必须有序且相同

```C++
#include<algorithm>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int> v1;
  v1.push_back(20);
  v1.push_back(30);
  vector<int> target;
  target.resize(v.size(),v1.size());//扩列
  merge(v.begin(),v.end(),v1.end(),v1.end(),target.begin());//10,20,20,30
}
```

### 5.3.4 reverse

```C++
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  reverse(v.begin(),v.end());
}
```

## 5.4 常用拷贝和替换算法

copy replace replace_if swap

### 5.4.1 copy

```C++
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int> v1;
	v1.resize(v.size());
  copy(v.begin(),v.end(),v2.begin());
}
```

### 5.4.2 replace

```C++
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  replace(v.begin(),v.end(),20,200000);
}
```

### 5.4.3 replace_if

```C++
class Greater10
{
  public:
  bool operator()(int val)
  {
    return val>10;
  }
}
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  replace_if(v.begin(),v.end(),Greater10(),200000);
}
```

### 5.4.4 swap

```C++
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int> v1;
  v1.push_back(20);
  v1.push_back(30);
  swap(v2,v1);
}
```

## 5.5 常用算术生成算法

numeric

### 5.5.1 accumulate

```C++
#include<numeric>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  int sum=accumulate(v.begin(),v.end(),0);//10+20+0
}
```

### 5.5.2 fill

```C++
#include<numeric>
void test()
{
  vector<int> v;
	v.resize(10);
  fill(v.begin(),v.end(),10);//全是10
}
```

## 5.6 常用集合算法

set_intersection set_union set_difference

### 5.6.1 set_intersection

```C++
#include<algorithm>
void print(int val)
{
  cout<<val<<" ";
}
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int> v1;
  v1.push_back(20);
  v1.push_back(30);
  vector<int> target;
  target.resize(min(v1.size(),v.size()))
  vector<int>::iterator itend=set_intersection(v.begin(),v.end(),v1.begin(),v1.end(),target.begin());
  for_each(target.begin(),itend(),print);//注意不要用target.end()
}
```

### 5.6.2 set_union

必须是有序序列

```C++
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int> v1;
  v1.push_back(20);
  v1.push_back(30);
  vector<int> target;
  target.resize(v.size()+v2.size());
  vector<int>::iterator itend=set_union(v.begin(),v.end(),v1.begin(),v1.end(),target.begin());
  
}
```

### 5.6.3 set_difference

```C++
#include<algorithm>
void test()
{
  vector<int> v;
  v.push_back(10);
  v.push_back(20);
  vector<int> v1;
  v1.push_back(20);
  v1.push_back(30);
  vector<int> target;
  target.resize(max(v1.size(),v.size()));
  vector<int>::iterator itend=set_difference(v.begin(),v.end(),v1.begin(),v1.end(),target.begin());
  //(v-v1)
  vector<int>::iterator itend=set_difference(v1.begin(),v1.end(),v.begin(),v.end(),target.begin());
  //(v1-v)
}
```

