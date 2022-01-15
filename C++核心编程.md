

[TOC]

# 1 内存分区模型

代码区：函数体的二进制代码

全局区：全局变量 静态变量 常量

栈区：编译器分配释放，存放函数参数值，局部变量

堆区：程序员分配释放，若不释放则系统回收

## 1.1 程序运行前

未执行程序前分为两区：

代码区：

存放CPU执行的机器指令

共享：对频繁被执行的程序只需有一份代码

只读：防止意外修改

全局区：

全局变量，静态变量存放在此，常量区(const修饰的全局常量和字符串常量)也在此，数据在程序结束时由操作系统释放

## 1.2程序运行后

栈区：编译器自动分配释放，存放参数值，局部变量等

不要返回局部变量的地址，其开辟的数据由编译器自己释放

```c++
#include <iostream>
using namespace std;
int* func(int b)
{
  b=100;//形参也放在栈区
  int a=10;//局部变量 存放在栈区，函数执行完后自动释放
  return &a;
}
int main()
{
  int *p=func();
  cout<<*p<<endl;
  cout<<*p<<endl;//会乱码
  return 0;
}
```

堆区：由程序员管理分配释放，若不释放，系统回收

C++中主要利用new开辟内存

```c++
#include<iostream>
using namespace std;
int * func()
{
  int *p=new int(10);
  return p;
}
int main()
{
  int *p=func();
  cout<<*p<<endl;
  return 0;
}
```

## 1.3 new operator

释放利用运算符delete，new会返回对应类型指针

```c++
#include<iostream>
using namespace std;
int * fun()
{
  new int(10);
  int *p=new int (10);
  return p;
}
void test01()
{
  int *p=func();
  cout<<*p<<endl;
  delete p;
}
void test02()
{
  int * arr=new int[10];//10个元素
  for (int i=0;i<10;i++)
  {
    arr[i]=i+100;
  }
  for (int j=0;j<10;j++)
  {
    cout<<arr[i]<<endl;
  }
  delete[] arr;//[]
}
int main()
{
  test01();
  test02();
  return 0;
}
```

# 2 引用

## 2.1 引用的基本使用

作用：起别名

语法：数据类型 &别名=原名；

```C++
int a=10;
int &b=a;
b=100;
cout<<"a"<<"\n"<<"b"<<endl;
```

## 2.2 引用注意事项

引用必须初始化

引用在初始化后不可改变(指针常量)

```c++
int &c;//非法，未初始化
int a=10;
int &b=a;
int &b=c;//非法

```

## 2.3 引用作函数参数

简化指针修改实参

```c++
#include<iostresm>
using namespace std;
void swap01(int a,int b)
{
  int temp=a;
  a=b;
  b=temp;
}
void swap02(int *a,int *b)
{
  int temp=*a;
  *a=*b;
  *b=temp;
}
int swap03(int &a,int &b)
{
  int temp=a;
  a=b;
  b=temp;
}
int main()
{
  int a=10;
  int b=20;
  swap01(a,b);
  cout<<"a="<<a<<"\n"<<"b="<<b<<endl;
  swap02(&a,&b);
  cout<<"a="<<a<<"\n"<<"b="<<b<<endl;
  swap(a,b);
  cout<<"a="<<a<<"\n"<<"b="<<b<<endl;
  return 0;
}
```

## 2.4 引用作函数返回值

不要返回局部变量引用

```C++
int & test01()
{
  int a=10;//栈区
  return a;
}
int & test02()
{
  static int a=10;//静态变量全局区
  return a;
}
int main()
{
  int &ref=test01();
  int &ref2=test02()
  cout<<"ref="<<ref<<endl;
  cout<<"ref="<<ref<<endl;//第二次乱码了
	
  cout<<"ref2="<<ref2<<endl;
  test02()=1000;//返回值是引用则调用可作为左值
  cout<<"ref2="<<ref2<<endl;//输出的是1000
}
```

## 2.5 引用的本质

**指针常量**

## 2.6 常量引用

防止误操作，修饰形参（节约内存）

```C++
#include<iostream>
using namespace std;
void print( const int &a)
{
  a=1000;//会报错
  cout<<"a="<<a<<endl;
}
int main()
{
  //int a=10;
 //写int &ref=10;非法
  //const int &ret=10;
  //相当于 int temp=10;const int &ref=temp;
  int a=100;
  print(a);
  return 0;
  
}
```

# 3 函数提高

## 3.1 函数默认参数

形参可以有默认值

返回值类型 函数名 （参数=默认值）{}

```C++
//如果某个位置有默认值，后面的参数都得有默认值
int func(int a,int b,int c)
{
  return a+b+c;
}
int func02(int a,int b=20,int c=30)
{
  return a+b+c;
}
//如果函数声明有默认参数，那么函数实现就不能有默认参数
int fun03(int a=10,int b=10);
//int fun03(int a=10,int b=10)//illegal（二义性），只能有一个有默认参数
int fun03(int a,int b)
{
  return a+b;
}
int main()
{
  cout<<fun(10,20,30)<<endl;
  cout<<fun02(10)<<endl;
  cout<<fun03()<<endl;
  //如果传fun02(10,30),则相当于b被改了
}
```

## 3.2 函数占位参数

形参列表可以有占位参数，调用函数时必须填补该位置

返回值类型  函数名（数据类型）{}

```C++
#include<isotream>
using namespace std;
void func(int a,int)
{
cout<<"this is function"<<endl;
}
int main()
{
func(10,10);
return 0;
}
```

## 3.3 函数重载

### 3.3.1 函数重载概述

**作用**：函数名可以相同，提高复用性

满足条件：

**·**同一个作用域下

·函数名称相同

·函数参数类型不同/个数不同/顺序不同

```C++
#include<iostream>
using namespace std;
//返回值不同不可以作为函数重载条件
void func()
{
  cout<<"function调用"<<endl;
}
void func(int a)
{
  cout<<"function调用！"<<endl;
}
void func(double a)
{
  cout<<"function调用！！"<<endl;
}
void func(int a,double b);
{
  cout<<"1"<<endl;
}
void func(double a,int b)
{
  cout<<"2"<<endl;
}
int main()
{
  func();
  func(10);
  func(3.14);
  func(10,3.14);
  func(3.14,10);
  return 0;
}
```

### 3.3.2 函数重载注意事项

引用作为重载条件 函数重载与默认参数

```C++
#include<iostream>
using namespace std;
void func(int &a)
{
  cout<<"func()"<<endl;
}
void func(const int &a)
{
  cout<<"func()!"<<endl;
}
void func2(int a,int b=10)
{
  cout<<"!"<<endl;
}
void func2(int a)
{
  cout<<"!"<<endl;
}
int main()
{
  int a=10;
  func(a);
  func(10);//相当于创建temp
  func02(a);//有默认值会出错
	return 0;
}
```

# 4 类和对象

C++面向对象特性：**封装、继承、多态**

C++认为万事万物皆为对象，对象有其属性和行为

对于具有相同性质的**对象**我们可以抽象称为**类**

## 4.1 封装

### 4.1.1 封装的意义

将属性和行为作为一个整体并加以权限控制

意义1.在设计类的时候属性和行为写在一起，表现事物

class 类名{访问权限：属性/行为}

e.g 1:设计一个圆类，求周长

```C++
#include<iostream>
using namespace std;
const double pi=3.14159;
class Circle
{
  //公共权限
	public:
  int r;                  //属性
  double C()              //行为
  {
    return 2*pi*r;
  }
};//;!!
int main()
{
  //实例化：创建具体的圆（对象）
  Circle c1;
  c1.r=10;
  cout<<"C="<<c1.C<<endl;
}
```

e.g 2:学生类

```C++
#include<iostream>
using namespace std;
#include<string>
class Student
{
  public:
  string name;
  string number;
  void ret()
  {
    cout<<name<<endl;
    cout<<number<<endl;
  }
  //赋值操作
  //void set(string Name)
  //{
  // name=Name;
  //}
};//结构体+函数？
int main()
{
  string name;
  string number;
  cout<<"请输入姓名"<<endl;
  cin>>name;
  cout<<"请输入学号"<<endl;
  cin>>number;
  Student s1;
  s1.name=name;
  s1.number=number;
  //或者s1.setname("张三")
  student.ret();
  return 0;
}
```

​	类中的属性和行为统称成员：属性也称成员属性、成员变量；行为也称成员函数、成员方法

意义2.可以把属性和行为放在不同的权限下加以控制

1.public 成员类内可以访问，类外不能访问

2.protected 成员类内可以访问，类外不可以访问

3. private 同上

```C++
class Person
{
  public:
  string name;
  protected:
  string car;
  private:
  string password;
  public:
  void func()
  {
    name="tony";
    car="bicylce";
    password="123456";
  }
};
int main()
{
	Person p1;
  p1.name="terry";
  p1.car="Benz";//访问不到
  p1.password="123";//访问不到
  p1.func();//如果把public改成protected/private访问不到
}
```

### 4.1.2 struct和class区别

唯一的区别在于struct默认权限是public，而class默认权限是private

```C++
class C1
{
  //默认权限是private
  int m_A;
 };
struct C2
{
  //默认是public
  int m_A;
};
int main()
{
  C1 c1;
  c1.m_A=100;//illegal
  C2 c2;
  C2.m_A=100;//legal
}
```

### 4.1.3 将成员属性设置为私有

优点1:将所有成员属性设置成私有，可以自己控制读写权限

优点2:对于写权限，可以检测数据有效性

```C++
#include<iostream>
#include<string>
using namespace std;
class Person
//提供接口
 public:
  void setname(string Name)
  {
    name=Name;
  }
  string getname()
  {
    return name;
  }
  int getage()
  {
    //age=0;//初始化
    return age;
  }
  void setage(int Age)
  {
	  if(Age<0||Age>150)
    {
      Age=0;
      cout<<"开玩笑"<<endl;
      return;
    }
    age=Age;
  }
	void stelover(string Lover)
  {
    lover=Lover;
  }
 private:
  string name;//可读可写
  int age;//可读可写（写必须是0-150）
  string lover;//只写
//属性私有
};
int main()
{
	Person p;
  p.setname("Tony");
  p.setage(18);
  cout<<p.getname()<<endl;
  cout<<p.getage()<<endl;
  p.setlover("无")；
}
```

#### 练习案例1:设计立方体类

```C++
#include<iostream>
using namespace std;
class Cube
{
  public:
  int m_L;
  int m_H;
  int m_W;
  void input()
  {
    cout<<"please give l,h,and w of a cube"<<endl;
    int l;
    int h;
    int w;
    cin>>l;
    cin>>h;
    cin>>w;
    m_L=l;
    m_H=h;
    m_W=w;
    cout<<"输入完毕"<<endl;
  }
  int V()
  {
    return m_L*m_H*m_W;
  }
  int S()
  {
    return (m_L*m_H+m_L*m_W+m_H*m_W)*2;
  }
};
  void test(int V1,int V2,int S1,int S2)
  {
      if (V1==V2&&S1==S2)
    {
    cout<<"相等"<<endl;
      }
    else
    {
        cout<<"不相等"<<endl;
        }
  }
int main()
{
    Cube c1;
    Cube c2;
    c1.input();
    c2.input();
    int V1=c1.V();
    int V2=c2.V();
    int S1=c1.S();
    int S2=c2.S();
    test(V1,V2,S1,S2);
    return 0;
}
//我版
```

```C++
#include<iostream>
using namespace std;
class Cube
{
  private:
  int L;
  int W;
  int H;
  public:
  void setL(int l)
  {
    L=l;
  }
  int getL()
  {
    return L;
	}
	void setW(int w)
  {
    W=w;
  }
  int getW()
  {
    return W;
	}
	void setH(int h)
  {
    H=h;
  }
  int getH()
  {
    return H;
	}
  int S()
  {
    return 2*(L*W+L*H+W*H);
  }
  int V()
  {
		return W*H*L;
  }
  bool samebyclass(Cube &c)
  {
	if(L==c.L&&W==c.W&&H==c.H)
  {
    return true;
  }
  return false;
  }
};
bool same(Cube &c1,Cube &c2)
{
  if(c1.L==c2.L&&c1.W==c2.W&&c1.H==c2.H)
  {
    return true;
  }
  return false;
}
int main()
{
	Cube c1;
  c1.setL(10);
  c1.setW(10);
  c1.setH(10);
  Cube c2;
  c2.setL(10);
  c2.setW(10);
  c2.setH(10);
  bool ret=same(c1,c2)
    if (ret)
    {
      cout<<"same"<<endl;
    }
  	else
  	{
  	cout<<"not same"<<endl;  
    }
  ret=c1.samebyclass(c2);//用成员函数
  	if (ret)
    {
      cout<<"same"<<endl;
    }
  	else
  	{
  	cout<<"not same"<<endl;  
    }
  }
```

#### 练习案例2:点和圆的关系

```C++
#include<iostream>
using namespace std;
class Point
{
  public:
  void setX(int x)
  {
    X=x;
  }
  int getX()
  {
      return X;
  }
  void setY(int y)
  {
    Y=y;
  }
  int getY()
  {
      return Y;
  }
  private:
  double X;
  double Y;
};
class Circle
{
  public:
  void setR(int r)
  {
    R=r;
  }
  int getR()
  {
        return R;
  }
  void setCenter(Point center)
  {
    Center=center;
  }
  Point getCenter()
  {
    return Center;
  }
  private:
  int R;
  Point Center;//类中可以引用另一个类
  
};
void isincircle(Circle &c,Point &p)
{
  int distance=
    (c.getCenter().getX()-p.getX())^2+(c.getCenter().getY()-p.getY())^2;
  int rdistance=c.getR()*c.getR();
  if (distance==rdistance)
  {
        cout<<"圆上"<<endl;
  }
  else if (distance>rdistance)
  {
    cout<<"圆外"<<endl;
  }
  else
  {
    cout<<"圆内"<<endl;
  }
}
int main()
{
  Circle c;
  c.setR(10);
  Point center;
  center.setX(10);
  center.setY(0);
  c.setCenter(center);
  Point p;
  p.setX(10);
  p.setY(10);
  isincircle(c,p);
  return 0;
}
//此处有把point circle类拆成不同文件方法
//头文件放声明，cpp.放具体函数Circle::getR()
```

## 4.2 对象的初始化和清理

### 4.2.1 构造函数和析构函数

被编译器自动调用，但是**空实现**

构造函数：赋值成员属性

类名（）{}

1.没返回值，不用写void

2.函数名和类名相同

3.可以有参数，可以重载

4.在调用对象时会自动调用构造，无需手动调用且只一次

析构函数：清理

～类名（）{}

1.没返回值，不用写void

2.函数名和类名相同，加～

3.不可以参函数，不可以重载

4.在调用对象时会自动调用析构，无需手动调用且只一次



```C++
#include<iostream>
using namespace std;
class Person
{
  //构造函数
  public:
  Person()
  {
		cout<<"构造函数调用"<<endl;
  }
  //析构函数
  ~Person()
  {
    cout<<"析构函数调用"<<endl;
  }
};
void test()
{
	Person p;//栈上的数据
}
int main()
{
	//test();
  Person p;//不会有析构
  system ("pause");//此后才会释放
  return 0;
}
```

### 4.2.2 构造函数的分类及调用

分类：

​	按参数：有参构造，无参构造

​	按类型：普通构造，拷贝构造

调用方式：

​	括号法，显示法，隐式转换法

```C++
#include<iostream>
using namespace std;
class Person
{
  public:
  Person
  {
    cout<<"构造函数调用"<<endl;
  }//无参构造（默认构造）
	Person(int a)
  {
    int age=a;
    cout<<"构造函数调用"<<endl;
  }//有参构造
  //拷贝构造函数
  Person(const Person &p)
  {
		int age=p.age;
  }
  ~Person
  {
    cout<<"析构函数调用"<<endl;
  }
};
//调用
void test()
{
  Person p;//默认函数调用
  Person p2(10);//调有参构造函数
  Person p3(p);//拷贝构造函数调用
  //注意事项
  //调用默认构造函数时不加（），因为会认为是declaration of a function
  Person p2=Person(10)；//显示
  Person p3=Person(p2);
  Person(10);//匿名对象 当前行执行结束后系统立即回收
  cout<<"aaa"<<endl;//会在析构后打印
  //注意，不要利用拷贝构造函数来初始化匿名对象（重定义）
  //隐式转换
  Person p4=10;//等价于Person（10）
  Person p5=p4;
}
int main()
{
  test();
	return 0;
}
```

### 4.2.3 拷贝构造函数调用时机

使用一个已经创建完毕的对象来初始化一个新对象

值传递的方式给参数传值

以值方式返回局部对象

```C++
class Person
{
public:
  Person()
  {
    cout<<"默认构造"<<endl;
  }
	Person(int age)
  {
    Age=age;
    cout<<"有参"<<endl;
  }
  Person(const Person &p)
  {
    Age=p.age;
    cout<<"拷贝"<<endl;
  }
	~Person()
  {
    cout<<"析构"<<endl;
  }
};
void dowork(Person p)
{

}
void test01()
{
	Person p1(20);
  Person p2(p1);
}
void test02();
{
  Person p;
  dowork(p);//形参拷贝
}
Person dowork2()//值方式返回局部对象
{
  Person p1;
  return p1;//返回的是拷贝的新对象
}
void test03()
{
  Person p=dowork();//因此会显示拷贝
}
```

### 4.2.4 构造函数调用规则

默认条件下，编译器至少给一个类添加三个函数

默认构造函数 默认析构函数 默认拷贝函数

如果写有参构造函数，不会定义默认无参构造，但会提供默认拷贝构造

如果定义拷贝构造函数，不会提供其他构造

```C++
class Person
{
public:
  Person()
  {
    cout<<"默认"<<endl;
  }
  Person(int age)
  {
    cout<<"有参构造"<<endl;
    Age=age;
  }
  
  ~Person()
  {
		cout<<"析构"<<endl;
  }
};
void test01()
{
  Person p;
  p.Age=18;
  Person p2(p);
  cout<<p2.Age<<endl;
}
void test02()
{
  Person p;
  
}
```

### 4.2.5 深拷贝与浅拷贝

浅拷贝：简单的赋值拷贝

深拷贝：在堆区重新申请空间进行拷贝

```C++
class Person
{
  public:
  int Age;
  int *Height;
  Person()
  {
    cout<<"默认构造"<<endl;
  }
  Person(int age,int height)
  {
    cout<<"有参"<<endl;
    Age=age;
    Height=new int height;
  }
  Person(const Person &p)
  {
    cout<<"拷贝"<<endl;
    Height=new int (*p.Height);//深拷贝
  }
  ~Person()
  {
    if (Height!=NULL)
    {
      delete Height;
      Height=NULL;
    }
  }
};
void test01()
{
  Person p(18,160);
  Person p2(p);//p2先被释放,先进后出
}
```

属性在堆区开辟一定自己提供浅拷贝

### 4.2.6 初始化列表

构造函数（）：属性1（值1），……{}

```C++
class Person
{
  public:
  Person(int a,int b,int c):A(a),B(b),C(c)
  {
    
  }
  int A;
  int B;
  int C;
};
void test()
{
  Person p(10,20,30);
}
```

### 4.2.7 类对象作为类成员

C++中的对象作为另一个类的成员

```C++
class Phone
{
  public:
  string PName;
  Phone (string Pname)
  {
    PName=Pname;
  }
  ~Phone
  {
    cout<<"Phone的析构函数"<<endl;
  }
};
class Person
{
  public:
  Person (string name,string Pname):Name(name),Phone(Pname)
  {
    
  }
  string Name;
  Phone Phone;
  ~Person
  {
    cout<<"person的析构函数"<<endl;//先析构Person，析构和构造相反
  }
};
void test()
{
  Person p("张三"，"iphone");
}
```

### 4.2.8 静态成员

static+变量/函数

静态成员变量：共享同一份数据，在编译阶段分配内存，类内声明，类外初始化

​               函数：所有对象共享一个函数，静态成员函数只能访问静态成员变量

```C++
class Person
{
public:
  static int A;
private:
  static int B;
}；
int Person::A=100;//类外初始化
int Person::B=200;
void test()
{
  Person p;
  cout<<p.A<<endl;
  Person p2;
  p2.A=200;
  cout<<p.A<<endl;//静态变量不属于某个对象，所有对象共享同一份数据
  //1.通过对象访问
  //2.通过类名访问
  cout<<Person::A<<endl;
  cout<<Person::B<<endl;//不能访问
}
```

```C++
class Person
{
  public:
  static void func()
  {
    A=100;//静态成员函数只能访问静态成员变量
    cout<<"调用"<<endl;
  }//静态成员函数也有访问权限
  static int A;
};
int A=0;
void test()
{
  Person p;
  p.func();
  Person::func();//两种访问方式
}
```

## 4.3 C++对象模型和this指针

### 4.3.1 成员变量和成员函数分开存储

只有非静态成员变量才属于类的对象

```c++
class Person
{
	int a;
  static int b;
  void func()
  {
    //成员函数不在sizeof(p)
  }
};
int b=10;
void test()
{
	Person p;
	cout<<sizeof(p)<<endl;//空的类1字节,加上一个int是4（替换了空）
  //加上static不占p内存
}
```

### 4.3.2 this指针

多个同类型的对象会调用同一段存储成员函数的内存

this指针指向被调用的成员函数所属的对象，隐含在每一个非静态成员函数内的一种指针

形参和成员变量重名时可以区分

返回对象本身时可以 return *this

```C++
class Person
{
  public:
  Person(int sge)
  {
    this->age=age;
  }
  int age;
  Person * Personaddage(Person &p)
  {
    this->age+=p.age;
    return *this;
  }
};
void test()
{
  Person p(18);
  cout<<p.age<<endl;
}
void test01()
{
  Person p1(10);
  Person p2(10);
  p2.Personaddage(p1).Personaddage(p1).Personaddage(p1);//链式编程思想
  cout<<p2.age<<endl;
}
```



### 4.3.3 空指针访问成员函数

```C++
class Person
{
public:
  void showclassname()
  {
    cout<<"Person"<<endl;
  }
  void showpersonage()
  {
    if (this==NULL)
    {
      return;
    }
    cout<<this->Age<<endl;
  }
  int Age;
};
void test()
{
  Person *p=NULL;
  p->showclassname();
  p->showpersonage();
}
```



### 4.3.4 const修饰成员函数

常函数：不可以修改成员属性，而其声明时加mutable则可以修改

常对象只能调用常函数

```C++
class Person
{
  //this指针的本质是指针常量 指针的指向是不能修改的
  //Person * const this
  void showperson() const//让指向也改不了
  {
    A=100;//表达式必须是可修改的左值,相当于 const Person * const this
    this->B=100;
  }
  void func()
  {
    
  }
  int A;
  mutable int B;
};
void test()
{
  Person p;
  p.showperson();
}
void test02()
{
  const Person p;//常对象
  p.A=100;//表达式必须是可修改的左值
  p.B=100;//legal
  p.showperson();
  p.func();//只能调用常函数，illegal，防止修改属性
}
```

## 4.4 友元

友元的目的：一些私有属性也想让类外特殊的一些函数或者类访问

关键字：friend

**全局函数作友元，类作友元，成员函数作友元**

### 4.4.1 全局函数作友元

```C++
class Building
{
  friend void goodfriend(Building *building);
  public:
  string sittingroom;
  Building()
  {
    sittingroom="sittingroom";
    bedroom="bedroom";
  }
  private:
  string bedroom;
};
void goodfriend(Building *building)
{
  cout<<building->sittingroom<<endl;
  cout<<building->bedroom<<endl;
}
void test()
{
  Building building;
  goofriend(&building);
}
```

### 4.4.2 类作友元

```C++
class Building;
class Goodfriend
{
  public:
  	goodfriend();
  	void visit();
    Building *building;
};
class Building
{
  friend class Goodfriend;
public:
  Building();
  string sittingroom;
private:
  string bedroom;
};
Building::Building()
{
  sittingroom="sittingroom";
  bedroom="bedroom";
}
Goodfriend::goodfriend()
{
  building=new Building;
}
void Goodfriend::visit()
{
  cout<<building->sittingroom<<endl;
  cout<<building->bedroom<<endl;
}
void test()
{
  Goodfriend g;
  g.visit();
}
```

4.4.3 成员函数作友元

```C++
class Goodfriend
{
  friend Goodfriend::void visit();
  public:
  Goodfriend();
  Building *building;
  void visit();
};
class Building
{
  public:
  string sitttingroom;
  Building();
  private:
  string bedroom;
};
Building::Building()
{
  sittingroom="sittingroom";
  bedroom="bedroom";
}
Goodfriend::Goodfriend()
{
  building=new Building;
}
void Goodfriend::visit()
{
  cout<<building->sittingroom<<endl;
  cout<<building->bedroom<<endl;
}
void test()
{
  Goodfriend g;
  g.visit();
}
```

## 4.5 运算符重载

对已有的运算符进行定义，赋予其他功能以适应不同数据类型

### 4.5.1 加号运算符重载

```C++
class Person
{
  public:
  Person operator+(Person &p)
  {
    Person temp;
    temp.A=this->A+p.A;
    temp.B=this->B+p.B;
    return temp;
  }
  int A;
  int B;
};
//全局函数重载
Person operator+(Person &p1,Person &p2)
{
  Person temp;
  temp.A=p1.A+p2.A;
  temp.B=p1.B+p2.B;
  return temp;
}//运算符也能重载
Person operator+(Person &p,int num)
{
  Person temp;
  temp.A=p.A+num;
  temp.B=p.B+num;
  return temp;
}
void test()
{
  Person p1;
  Person p2;
  p1.A=10;
  p2.A=10;
  p1.B=10;
  p2.B=10;
  Person p3=p1+p2;
  cout<<p3.A<<endl;
  cout<<p3.B<<endl;
}
```

内置的数据类型表达式运算改变不了

不要滥用运算符重载

### 4.5.2 左移运算符重载

可以输出自定义数据类型

```C++
class Person
{
  friend ostream& operator<<(ostream& cout,Person& p);
  private:
  int A;
  int B;
  public:
  Person(int a,int b)
  {
    A=a;
    B=b;
  }
};
ostream & operator<<(ostream &cout,Person &p)
{
  cout<<"A="<<p.A;
  cout<<"B="<<p.B;
  return cout;
}
void test()
{
  Person p(10,10);
  cout<<p<<endl;
}
```

### 4.5.3 递增运算符重载

实现自己的整型数据

```C++
class Integer
{
  friend ostream & operator<<(ostream &cout,Interger &myint);
  private:
  int Num;
  public:
  Integer()
  {
    Num=0;
  }
  //前置递增
  Integer & operator++()
  {
		Num++;
    return *this;
  }
  //后置递增
  Integer operator++(int)//占位
  {
     Integer temp=*this;
     Num++;
    return temp;
  }
};
ostream & operator<<(ostream &cout,Interger &myint)
{
  cout<<myint.Num;
  return cout;
}
void test()
{
  Integer myint;
  cout<<myint<<endl;
  cout<<myint++<<endl;//先返回
  cout<<++myint<<endl;//会先++
}
```

### 4.5.4 赋值运算符重载

C++还会给一个类添加赋值运算符operator=，对属性值拷贝

```C++
class Person
{
  public:
  Person(int age)
  {
		Age=new int(age);
  }
  ~Person()
  {
    if(Age!=NULL)
    {
      delete Age;
      Age=NULL:
    }
  }
  Person & operator=(Person &p)
  {
    if(Age!=NULL)
    {
      delete Age;
      Age=NULL:
    }
    Age=new int (p.Age);
    return * this;
  }
  int * Age;
  
};
void test()
{
  Person p(18);
  Person p1(20);
  Person p2(30);
  p=p1=p3;//重复释放内存,需深拷贝
  cout<<*p.Age<<endl;
}
```

### 4.5.6 函数调用运算符重载

仿函数

```c++
class Print
{
  public:
  void operator()(string test)
  {
    cout<<test<<endl;
  }
};
void test()
{
  Print p;
  p("hello world");
}
```

```C++
class Add
{
  public:
  int operater()(int num1,int num2)
  {
    return num1+num2;
  }
};
void test()
{
	Add add;
  add(100,100);
//匿名函数对象
cout<<Add()(100,100)<<endl;
}
```

## 4.6 继承

类有级别，下级别的成员除了有上一级的共性还有自己的特性

可以用继承的技术减少代码

### 4.6.1 继承的基本语法

```C++
//普通实现页面
class Java
{
  public:
  void header()
  {
		cout<<"公共头部"<<endl;
  }
  void footer()
  {
		cout<<"公共底部"<<endl;
  }
  void left()
  {
		cout<<"公共分类列表"<<endl;
  }
  void content()
  {
		cout<<"Java"<<endl;
  }
};
class Python
{
  public:
  void header()
  {
		cout<<"公共头部"<<endl;
  }
  void footer()
  {
		cout<<"公共底部"<<endl;
  }
  void left()
  {
		cout<<"公共分类列表"<<endl;
  }
  void content()
  {
		cout<<"Python"<<endl;
  }
};
void test()
{
  Java java;
  Python python;
  cout<<"Java:"<<endl;
  java.header();
  java.footer();
  java.left();
  java.content();
  cout<<"Python:"<<endl;
  python.header();
  python.footer();
  python.left();
  python.content();
}
```

```C++
//继承
class Base
{
  public:
	void header()
  {
		cout<<"公共头部"<<endl;
  }
  void footer()
  {
		cout<<"公共底部"<<endl;
  }
  void left()
  {
		cout<<"公共分类列表"<<endl;
  }
};
class Java:public Base//class 子类（派生类）：继承方式 父类（基类）
{
public:
  void content()
  {
    cout<<"Java"<<endl;
  }
};
class Python:public Base
{
	void content()
  {
		cout<<"Python"<<endl;
  }
};
void test()
{
	Java java;
  Python python;
  cout<<"Java:"<<endl;
  java.header();
  java.footer();
  java.left();
  java.content();
  cout<<"Python:"<<endl;
  python.header();
  python.footer();
  python.left();
  python.content();
}
```

### 4.6.2 继承方式

公共继承 保护继承 私有继承

private都访问不到，protected继承会将public升格为protected，private继承递推

```C++
class Base1
{
	public:
  int A;
  protected:
  int b;
  private:
  int C;
};
class Son1:public Base1
{
  public:
  void func()
  {
		A=10;
    B=10;
    C=10;//报错,父类的私有权限访问不到
  }
};
void test01()
{
	Son1 s1;
  s1.A=100;
  s1.B=100;//报错，B是protected
}
class Base2
{
	public:
  int A;
  protected:
  int b;
  private:
  int C;
};
class Son2:protected Base2
{
  public:
  void. func()
  {
		A=100;
  }
};
void test02()
{
	Son2.s2;
  s2.A=1000;//报错，A变为protected
}
class  Son3:private Base1;
void test03()
{
	Son3.s3;
  s3.B=1000;//变为private，报错
}
class Grandson3:public Son3
{
  void func()
  {
    A=1000;//错了，private了
  }
};
```

4.6.3 继承中的对象模型

```C++
class Son:public Base
{
  int D;
};
class Base
{
  public:
  int A;
  protected:
  int B;
  private:
  int C;
};
void test()
{
	cout<<sizeof(Son)<<endl;//16,父类所有非静态的成员属性都被继承
  //private访问不到但是继承
}
```

### 4.6.4 继承中构造和析构顺序

子类继承父类后，当创建子类对象，也会调用父类构造

```C++
class Base
{
  public:
  Base()
  {
		cout<<"Base构造"<<endl;
  }
  ~Base()
  {
    cout<<"Base析构"<<endl;
  }
};
class Son:public:Base
{
  Son()
  {
		cout<<"Son构造"<<endl;
  }
  ~Son()
  {
    cout<<"Son析构"<<endl;
  }
};
void test()
{
	Son s1;
}
//output:
//Base构造
//Son构造
//Son析构
//Base析构
```

### 4.6.5 继承同名成员处理对象

子类：直接访问

父类：加作用域

```C++
class Base
{
  public:
  int A;
  Base()
  {
		A=100;
  }
  void func()
  {
    cout<<"Base"<<endl;
  }
};
class Son:public Base
{
  public:
  int A;
  Son()
  {
		int A=200;
  }
  void func()
  {
		cout<<"Son"<<endl;
  }
};
void test()
{
  Son s;
  cout<<s.A<<endl;
  cout<<s.Base::A<<endl;
}
void test02()
{
	Son s;
  s.func();
  s.Base::func();
}
```

### 4.6.6 继承同名静态成员处理方式

子类直接访问，父类加作用域

```C++
class Base
{
  public:
  static int A;
  static void func()
  {
		cout<<"Base"<<endl;
  }
};
int Base::A=100;
class Son:public Base
{
  public:
  static int A;
  static void func()
  {
		cout<<"Son"<<endl;
  }
};
int Son::A=1000;
void test()
{
	Son s;
  cout<<s.A<<endl;
  cout<<s.Base::A<<endl;
  cout<<Son::A<<endl;
  cout<<Son::Base::A<<endl;//通过类名访问父类作用域下的成员
}
void test02()
{
  Son s;
  s.func();
  s.Base::func();
  Son::func();
  Son::Base::func();
}
```

和非静态基本一样

### 4.6.7 多继承语法

**class 子类：继承方式 父类1，继承方式 父类2……**

实际开发不建议

```C++
class Base1
{
  public:
	int A;
  Base1()
  {
		A=100;
  }
};
class Base2
{
  public:
  int A;
  Base2()
  {
    A=200;
  }
}
class Son:public Base1,public Base2
{
  public:
  int C;
  int D;
};
void test()
{
	Son s;
  cout<<sizeof(s)<<endl;
  cout<<s.Base1::A<<endl;
}
```

### 4.6.8菱形继承

两个派生类继承同一个基类，另一个类继承两个派生类

问题：二义性，继承最初的父类继承了两份

```C++
class Animal{public: int Age};
//虚继承解决内存浪费
//Animal叫虚基类
class Sheep:virtual public Animal {public:int Age};
class Camel:virtual public Animal {public:int Age};//相当于继承一个指针，经过运算指向同一个量
class Alpaca:public Sheep,public Camel {public:int Age};
void test()
{
  Alpaca alpaca;
  alpaca.Sheep::Age=18;
  alpaca.Camel::Age=28;
  cout<<alpaca.Sheep::Age<<endl;//28
  cout<<alpaca.Age<<endl;//28
}
```

## 4.7 多态

### 4.7.1 多态的基本概念

静态多态：函数重载、运算符重载

动态多态：派生类和虚函数运行时多态

静态多态：函数地址早绑定-编译阶段确定函数地址

动态多态：函数地址晚绑定-运行阶段确定函数地址

```C++
class Animal
{
  public:
  virtual void speak()
  {
    cout<<"anmimal is speaking"<<endl;
  }
}//虚函数，地址晚绑定
class Cat:public Animal
{
  public:
  virtual void speak()
  {
		cout<<"cat is speaking"<<endl;
  }
};
Class Dog:public Animal
{
 	public:
  virtual void speak()
  {
	  cout<<"Dog is speaking"<<endl;
  }
};
void dospeak(Animal &animal)//Animal &animal=cat
{
	animal.speak();
}
void test()
{
  Cat cat;
  dospeak(cat);
  Dog dog;
  dospeak(dog);
}
void test02()
{
  Animal animal;
	cout<<sizeof(animal)<<endl;//4,多了个 virtual function pointer
  //指向 virtual function table，内部记录虚函数地址
  //子类重写虚函数时，vftable内部会被子类覆盖
}
//多态：有继承关系，子类要重写父类的虚函数
//使用：父类的指针或引用指向子类对象
```

### 4.7.2 多态案例一-计算器类

优点：代码组织结构清晰	可读性强	有利于前期扩展和后期维护

```C++
class Calculator
{
  public:
  int Num1;
  int Num2;
  int getResult(string oper)
  {
    if (oper=="+")
    {
      return Num1+Num2;
    }
		else if (oper=="-")
    {
      return Num1-Num2;
    }
		else if (oper=="*")
    {
      return Num1*Num2;
    }
  }
  //如果想扩展新的功能需修改源码
  //真实开发中提倡开闭原则：对扩展进行开发，对修改进行关闭
};
void test()
{
	Calculator c;
  c.Num1=10;
  c.Num2=20;
  c.getResult("+");
	c.getResult("-");
  c.getResult("*");
}
//利用多态实现计算器
class Abstractcalculator
{
  public:
  virtual int getResult();
  {
    return 0;
  }
  int Num1;
  int Num2;
};
class Addcalculator:public Abstractcalculator
{
  public:
  int getResult()
  {
    return Num1+Num2;
  }
};
class Subcalculator:public Abstractcalculator
{
  public:
  int getResult()
  {
    return Num1-Num2;
  }
};
class Mulcalculator:public Abstractcalculator
{
  public:
  int getResult()
  {
    return Num1*Num2;
  }
};
void test()
{
  Abstractcalculator *abc=new Addcalculator;
  abc->Num1=10;
  abc->Num2=20;
  cout<<abc.getResult()<<endl;
  delete abc;
  abc=new Subcalculator;
  abc->Num1=10;
  abc->Num2=20;
  cout<<abc.getResult()<<endl;
  delete abc;
}
```

### 4.7.3 纯虚函数和抽象类

通常父类中虚函数无意义，因此可以写纯虚函数

virtual 返回值类型 函数名（参数列表）=0；

叫做抽象类，无法实例化对象，子类必须重写纯虚函数

```C++
class Base
{
  public:
  virtual void func()=0;
};
class Son:public Base
{
  public:
  virtual void func(){};
};
void test()
{
	Base *base=new Son;
  base->func();
}
```

### 4.7.4 多态案例二-制作饮品

```C++
class Abstractdrinking
{
  public:
  virtual void Boil()=0;
  virtual void Brew()=0;
  virtual void PourInCup()=0;
  virtual void Putsth()=0;
  void makedrink()
  {
    Boil();
    Brew();
    PourInCup();
    Putsth();
  }
};
class Coffee:public Abstractdrinking
{
	public:
  virtual void Boil()
  {
    cout<<"boil water"<<endl;
  }
  virtual void Brew()
  {
    cout<<"brew coffee"<<endl;
  }
  virtual void PourInCup()
  {
    cout<<"put it into the cup"<<endl;
  }
  virtual void Putsth()
  {
    cout<<"put in milk and sugar"<<endl;
  }
};
class Milktea:public Abstractdrinking
{
	public:
  virtual void Boil()
  {
    cout<<"boil water"<<endl;
  }
  virtual void Brew()
  {
    cout<<"brew tea"<<endl;
  }
  virtual void PourInCup()
  {
    cout<<"put it into the cup"<<endl;
  }
  virtual void Putsth()
  {
    cout<<"put in milk and sugar"<<endl;
  }
};
void dowork(Abstractdrinking *abs)
{
	abs->makedrink();
  delete abs;
}
void test()
{
  dowork(new Coffee);
  dowork(new Milktea);
}
```

### 4.7.5 虚析构和纯虚析构

如果子类有属性到堆区 ，父类释放时无法调用子类的析构

用上述方法解决

virtual ～类名（）{}

virtual ~类名 （）{}=0;

```C++
class Animal
{
	public:
  Animal()
  {
    cout<<"Animal构造"<<endl;
  }
  virtual void speak()=0;
  virtual ~Animal()
  {
		cout<<"animal析构"<<endl;
  }
  //or virtual ~Animal()=0;
};
//Animal::~Animal() {cout<<"Animal 析构"<<endl;}
class Cat:public Animal
{
	public:
  Cat(string name)
  {
    cout<<"cat构造"<<endl;
    Name=new string(name)
  }
  virtual void speak()
  {
		cout<<*Name<<" cat is speaking"<<endl;
  }
  string *Name;
  ~Cat()
  {
    if (Name!=NULL)
    {
      cout<<"cat 析构"<<endl;
      delete Name;
      Name=NULL:
    }
  }
};
void test()
{
	Animal * animal=new Cat("Tom");
  animal->speak();
  //父类指针析构后不会调用子类析构
  delete animal;
}
```

### 4.7.6 多态案例三-电脑组装

```C++
class CPU
{
public:
  virtual void calculate()=0;
};
class Videocard
{
public:
  virtual void display()=0;
};
class Memory
{
public:
  virtual void storage()=0;
};
class Computer
{
public:
  Computer(CPU * cpu,Videocard *vc,Memory *mem)
  {
    m_cpu=cpu;
    m_vc=vc;
    m_mem=mem;
  }
  void work()
  {
    m_cpu->calculate();
    m_vc->display();
    m_mem->storage();
  }
  ~Computer()
  {
    if(m_CPU!=NULL)
    {
			delete m_CPU;
      m_CPU=NULL;
    }
    if(m_vc!=NULL)
    {
			delete m_vc;
      m_vc=NULL;
    }
    if(m_mem!=NULL)
    {
      delete m_mem;
      m_mem=NULL:
    }
  }
private:
  CPU *m_cpu;
  Videocard *m_vc;
  Memory *m_mem;
};
class IntelCPU:public CPU
{
public:
  virtual void calculate()
  {
    cout<<"Intel's CPU is functioning"<<endl;
  }
};
class Intelvideocard:public Videocard
{
public:
  virtual void display()
  {
    cout<<"Intel'videocard is functioning"<<endl;
  }
};
class Intelmemory:public Memory
{
public:
  virtual void storage()
  {
    cout<<"Intel'memory is functioning"<<endl;
  }
};
class LenovoCPU:public CPU
{
public:
  virtual void calculate()
  {
    cout<<"Lenovo's CPU is functioning"<<endl;
  }
};
class Lenovovideocard:public Videocard
{
public:
  virtual void display()
  {
    cout<<"Lenovo'videocard is functioning"<<endl;
  }
};
class Lenovomemory:public Memory
{
public:
  virtual void storage()
  {
    cout<<"Lenovo'memory is functioning"<<endl;
  }
};
void test()
{
  CPU * intelCPU=new IntelCPU;
  Videocard * intelCard=new Intelvideocard;
  Memory * intelmem=new Intelmemory;
  Computer *computer1=new Computer(intelCPU,intelCard,intelmem);//或者直接在此new
  Computer1->work();
  delete computer1;
}
```



# 5 文件操作

文件可以将文件持久化

包含头文件<fstream>(file)

文件类型分为文本文件（用ASC）和二进制文件

操作文件：

1.ofstream:写

2.ifstream:读

3.fstream:读写

## 5.1. 文本文件

### 5.1.1 写文件

步骤：

1.包含头文件 #include<fstream>

2.创建流对象 ofstream ofs;

3.打开文件 ofs.open("文件路径"，打开方式);

4.写数据 ofs<<”写入的数据";

5.关闭文件 ofs.close();

| **打开方式** | **解释**                 |
| ------------ | ------------------------ |
| ios::in      | 为读文件而打开文件       |
| ios::out     | 为写文件而打开文件       |
| ios::ate     | 初始位置：文件尾         |
| ios::app     | 追加方式写文件           |
| ios::trunc   | 如果文件存在先删除再创建 |
| ios::binary  | 二进制方式               |

文件打开方式可以配合使用，利用｜

e.g.ios::binary|ios::out

```C++
#include<fstream>
void test()
{
  ofstream ofs;
  ofs.open("text.txt",ios::out);
  ofs<<"张三"<<endl;
  ofs.close();
}
```

### 5.1.2 读文件

1.包含头文件

2.创建流对象 ifstream ifs;

3.ifs.open("文件路径",打开方式)

4.读数据

5.ifs.close();

```c++
#include<fstream>
void test()
{
  ifstream ifs;
  ifs.open("text.txt",ios::in);
  if(!ifs.is_open())
  {
    cout<<"文件打开失败"<<endl;
    return;
  }
  char buf[1024]={0};
  while (ifs>>buf)
  {
    cout<<buf<<endl;
  }
  //或
  char buf[1024]={0};
  while(ifs.getline(buf,sizeof[buf]))
  {
    cout<<buf<<endl;
  }
  //或
  string buf;
  while(getline(ifs,buf))
  {
    cout<<buf<<endl;
  }
  //或
  char c;
  while((c=ifs.get())!=EOF)//end of file
  {
    cout<<c<<
  }
  ifs.close();
}
```

## 5.2 二进制文件

ios::binary

### 5.2.1 写文件

ostream& write(const char * buffer,int len);

```C++
#include<string>
#include<fstream>
class Person
{
  public:
  char Name[64];
  int Age;
};
void test()
{
  ofstream ofs;
  ofs.open("person.txt",ios::out|ios::binary);
  Person p={"张三",18};
  ofs.write((const char *)&p,sizeof(Person));
  ofs.close();
}
```

### 5.2.2 读文件

istream& read(char *buffer,int len);

```C++
#include<fstream>
#include<string>
class Person
{
  public:
  char Name[64];
  int Age;
};
void test()
{
  ifstream ifs;
  ifs.open("person.text",ios::in|ios::binary);
  if(!ifs.is_open())
  {
    cout<<"文件打开失败"<<endl;
    return;
  }
  Person p;
  ifs.read((char *)&p,sizeof(p));
  cout<<p.Name<<endl;
  cout<<p.Age<<endl;
  ifs.close();
}
```

