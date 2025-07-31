# 1
# l = []
# for i in range(2000, 3201):
#     if (i%7==0)and(i%5!=0):
#         l.append(str(i))
# print("," .join(l))
# .join()是字符串对象的一个方法，其作用是:
# 把一个可迭代对象（像列表、元组这类）中的元素连接成一个字符串

# 2
# def fact(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     print(res)
# fact(5)

# 3
# def mydict(n):
#     dict = {}
#     for i in range(1, n+1):
#         dict[i] = i*i
#     print(dict)
# mydict(8)

# 4
# import re
# def getNumInStr(s):
#     li = re.findall("\d+", s)
#     print(li)
#     print(tuple(li))
# getNumInStr("34岁，67年，55岁，33岁，12日，98年")

# 5
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         print("请输入字符串: ")
#         self.s = input()
#     def printString(self):
#         print(self.s.upper())
#
# obj = InputOutString()
# obj.getString()
# obj.printString()

# 6
# 题都说不明白，不写了

# 7
# def doubleDimension(X,Y):
#     lio = []
#     for i in range(X):
#         lii = []
#         for j in range(Y):
#             lii.append(i*j)
#         lio.append(lii)
#     print(lio)
#
# doubleDimension(3,5)

# 8
# def wordSord(li):
#     li.sort()
#     print(li)
#
# wordSord(["without", "hello", "bag", "world"])

# 9
# def upperAll(s):
#     print(s.upper())
#
# s = "aadsfhuiefuabofha"
# upperAll(s)

# 10
# def wordSort(s):
#     li = s.split(" ")
#     se = set(li)
#     li = list(se)
#     li.sort()
#     print(li)
# wordSort("hello world and practice makes perfect and hello world again")

# 11
# def filterFive(li):
#     for i in li:
#         if i % 5 == 0:
#             print(bin(i))
#
# filterFive((0b0100,0b0011,0b1010,0b1001))

# 12
# def printAllDouble():
#     li = []
#     for i in range(1000, 3001):
#         s = str(i)
#         if(int(s[0])%2==0)and(int(s[1])%2==0)and(int(s[2])%2==0)and(int(s[3])%2==0):
#             li.append(i)
#     print(li)
#
# printAllDouble()

# 13
# import re
# def staticWordNum(s):
#     word = re.findall("([a-zA-Z])", s)
#     print(len(word))
#     num = re.findall("\d", s)
#     print(len(num))
#
# staticWordNum("Hello world! 123")

# 14
# import re
# def staticUpperNum(s):
#     up = re.findall("([A-Z])", s)
#     print("UPPER CASE",len(up))
#     lower = re.findall("([a-z])", s)
#     print("LOWER CASE", len(lower))
#
# staticUpperNum("Hello world!")

# 15
# def fourBitAdd(n):
#     char = str(n)
#     num = n
#     for i in range(2,5):
#         s = char * i
#         num += int(s)
#     print(num)
#
# fourBitAdd(9)

# 16 列表推导式
# li = [1,2,3,4,5,6,7,8,9]
# numbers = [x for x in li if x%2!=0]
# print(numbers)

# 17

# 18
# 以下是一个使用生成器定义的类，它可以在给定范围0和n之间迭代可被7整除的数字：
# class DivisibleBySeven(object):
#     def __init__(self, n):
#         self.n = n
#     def __iter__(self):
#         for num in range(self.n + 1):
#             if num % 7 == 0:
#                 yield num
#
# if __name__ == "__main__":
#     n = 30
#     divisibles = DivisibleBySeven(n)
#     print(f"0 到 {n} 之间可被 7 整除的数字：")
#     for num in divisibles:
#         print (num)

# 19
# def staticWordNum(s):
#     li = s.split(" ")
#     word_dict = {}
#     for i in li:
#         if i in word_dict:  # 检查键是否已存在
#             word_dict[i] += 1
#         else:
#             word_dict[i] = 1  # 首次遇到该单词，初始化为1
#     sorted(word_dict.items(), key=lambda x: x[0])
#     print(word_dict)
#
# s = "New to Python or choosing Python 2 and Python 3? Read Python 2 or Python 3"
# staticWordNum(s)

# 20
# 写一个可以计算数字平方值的方法，要使用**运算符
# def pingfang(n):
#     return n**2
# print(pingfang(5))

# 21
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

# 22
# class Person(object):
#     name = "gyj"
#     def __init__(self, name = None):
#         self.name = name
#
# obj = Person("zzk")
# print(Person.name)
# print(obj.name)

# 23
# 定义一个可以计算两数之和的函数
# def myadd(x,y):
#     return x+y
# print(myadd(7,9))

# 24
# 定义一个可以将整数转换为字符串并在控制台中打印的函数
# 提示：使用str()将整数转换为字符串
# def inttostr(n):
#     return str(n)
# print(inttostr(599))
# print(type(inttostr(599)))

# 25
# 定义一个函数，它可以接收两个字符串形式的整数并计算她们的和，然后在控制台中输出
# 提示：使用int()将字符串转换为整数
# def strtointadd(s1,s2):
#     return int(s1)+int(s2)
# print(strtointadd("599","701"))
# print(type(strtointadd("599","701")))

# 26
# 定义一个函数，可以将两个字符串拼接起来
# 提示：可以使用+
# def straddstr(s1,s2):
#     return s1+s2
# print(straddstr("hello", "python"))

# 27
# def printLongStr(s1,s2):
#     if len(s1)>len(s2):
#         print(s1)
#     elif len(s1)<len(s2):
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# printLongStr("hello","world")
# printLongStr("six","star")
# printLongStr("Cracked","robot")

# 28
# 检测一个输入的数字是偶数还是奇数
# def checkNumDouble(n):
#     if n%2==0:
#         print("它是偶数")
#     else:
#         print("它是奇数")
#
# checkNumDouble(654)

# 29
# def miDict():
#     dict = {}
#     for i in range(1,4):
#         dict[i] = i**2
#     print(dict)
#
# miDict()

# 30

# 31

# 32

# 33
# def printList():
#     li = []
#     for i in range(1,21):
#         li.append(i**2)
#     print(li)
# printList()

# 34
# def printList():
#     li = []
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[0:5])
# printList()

# 35
# def printList():
#     li = []
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[-5:])
# printList()

# 36
# def printList():
#     li = []
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[5:])
# printList()

# 37
# def printList():
#     li = []
#     for i in range(1,21):
#         li.append(i**2)
#     print(tuple(li))
# printList()

# 38
# tup = (1,2,3,4,5,6,7,8,9,10)
# print(tup[:5])
# print(tup[5:])

# 39
# tup = (1,2,3,4,5,6,7,8,9,10)
# li = []
# for i in tup:
#     if i%2 == 0:
#         li.append(i)
# tup2 = tuple(li)
# print(tup2)

# 40
# print("请输入字符串：")
# s = input()
# if s == "yes" or s == "YES" or s == "Yes":
#     print("Yes")
# else:
#     print("No")

# 41
# li = [1,2,3,4,5,6,7,8,9,10]
# def myfilter(li):
#     evennumber = filter(lambda x:x%2==0,li)
#     for even in evennumber:
#         print(even)
#
# myfilter(li)

# 42
# li = [1,2,3,4,5,6,7,8,9,10]
# squre = map(lambda x:x**2, li)
# print(list(squre))

# 43
# li = [1,2,3,4,5,6,7,8,9,10]
# squre = map(lambda x:x**2, filter(lambda x:x%2==0,li))
# print(list(squre))

# 44
# swq = map(lambda x:x**2, range(1,21))
# # print(list(swq))

# 45
# class American(object):
#     @staticmethod
#     def printNationality():
#         print("American")
#
# a = American()
# a.printNationality()
# American.printNationality()

# 46
# class American(object):
#     pass
# class NewYorker(American):
#     pass
# anAmerican = American()
# aNewyorker = NewYorker()
# print(anAmerican)
# print(aNewyorker)

# 47
# class Circle(object):
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return 3.14*self.radius**2
#
# acircle = Circle(2)
# print(acircle.area())

# 48
# class Rectangle(object):
#     def __init__(self, l, w):
#         self.length = l
#         self.width = w
#     def area(self):
#         return self.length * self.width
# rect = Rectangle(7,4)
# print(rect.area())

# 49
# class Shape(object):
#     def area(self):
#         print("形状的面积为0")
# class Square(Shape):
#     def __init__(self, n):
#         self.n = n
#     def area(self):
#         print(f"形状的面积为{self.n**2}")
#
# shape = Shape()
# shape.area()
# square = Square(5)
# square.area()

# 50
# 请引发RuntimeError异常
# raise RuntimeError("something wrong")

# 51
# try-catch的使用
# def throws():
#     return 5/0
# try:
#     throws()
# except ZeroDivisionError:
#     print("division by zero")
# except ExceptionError:
#     print("Caught an exception")
# finally:
#     print("In finally block for cleanup")

# 52
# class MyException(object):
#     def __init__(self, msg):
#         self.msg = msg
# err = MyException("something wrong")

# 53
# import re
# s = "username@companyname.com"
# def getusername(s):
#     res = re.match("(\w+)@((\w+\.)+(com))", s)
#     li = res.group().split("@")
#     print(li[0])
# getusername(s)

# 54
# import re
# s = "username@companyname.com"
# def getusername(s):
#     res = re.match("(\w+)@((\w+\.)+(com))", s)
#     li = res.group().split("@")
#     li2 = li[1]
#     li3 = li2.split(".")
#     print(li3[0])
# getusername(s)

# 55
# import re
# s = "2 cats and 3 dogs"
# def getNum(s):
#     res = re.findall("\d", s)
#     print(res)
# getNum(s)

# 56
# ui = u"hello world"
# print(ui)

# 57
# python中的解码与编码
# s = "图灵python"
# enc = s.encode("utf-8")
# print(enc)
# dec = enc.decode("utf-8")
# print(dec)

# 58
# 编写一个特殊注释，来表明python源代码文件是的unicode格式的
# -*- coding:utf-8 -*-
# ----------------------

# 59
# def jishu(n):
#     if n == 1:
#         return float(1/2)
#     return float(n/(n+1)) + jishu(n-1)
#
# res = jishu(5)
# print(res)

# 60
# def recursion(n):
#     if n <= 0:
#         return 0
#     return 100 + recursion(n-1)
# res = recursion(5)
# print(res)

# 61
# 斐波那契数列
# def fiberna(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fiberna(n-1) + fiberna(n-2)
# res = fiberna(7)
# print(res)

# 62
# 使用生成器
# def evenGenerator(n):
#     i = 0
#     while i <= n:
#         if i%2 == 0:
#             yield i
#         i += 1
# values = []
# for i in evenGenerator(16):
#     values.append(i)
# print(values)

# 63
# def numgenerator(n):
#     for i in range(n+1):
#         if i%35==0:
#             yield i
# values = []
# for i in numgenerator(100):
#     values.append(i)
# print(values)

# 64
# 请写assert语句来验证列表[2,4,6,8]中的每个数字都是偶数
# 提示：使用断言表达式进行断言
# li = [2,4,6,8,9]
# for i in li:
#     assert i%2==0

# 65
# 基本数学表达式解析
# s = "35 + 3"
# print(eval(s))

# 66
# 随机生成一个1-100的数
# import random
# res = random.randint(1,100)
# print(res)

# 67
# import random
# res = random.random()*100
# print(res)

# 68
# import random
# res = random.choice([i for i in range(11) if i%2==0])
# print(res)

# 69
# import random
# res = random.choice([i for i in range(110) if i%35==0])
# print(res)

# 70
# import random
# res = random.sample(range(100, 201), 5)
# print(res)

# 71
# import random
# res = random.sample([i for i in range(100, 201) if i%2==0], 5)
# print(res)

# 72
# import random
# res = random.sample([i for i in range(100, 1000) if i%35==0], 5)
# print(res)

# 73
# import random
# res = random.randrange(7,16)
# print(res)

# 74
# import zlib
# s = b"hello world!hello world!hello world!hello world!"
# t = zlib.compress(s)
# print(t)
# r = zlib.decompress(t)
# print(r)

# 75
# from timeit import Timer
# t = Timer("for i in range(1000):1+1")
# print(t.timeit())

# 76
# from random import shuffle
# li = [3,6,7,8]
# shuffle(li)
# print(li)

# 77
# who = ["I", "You"]
# do = ["Play", "Love"]
# obj = ["Hockey", "Fottball"]
# for i in who:
#     for j in do:
#         for k in obj:
#             sentence="%s %s %s."%(i,j,k)
#             print(sentence)

# 78
# li = [5, 6, 77, 45, 22, 12, 24]
# li = [x for x in li if x % 2 != 0]
# print(li)

# 79
# li = [12, 24, 35, 70, 88, 120, 155]
# li = [x for x in li if x % 35 != 0]
# print(li)

# 80
# li = [12, 24, 35, 70, 88, 120, 155]
# li = [x for (i, x) in enumerate(li)if i%2!=0]
# print(li)

# 81
# import numpy as ny
# array = [[[0 for col in range(8)] for col in range(5)]for row in range(4)]
# print(array)

# 82
# li = [12, 24, 35, 70, 88, 120, 155]
# li = [x for (i,x) in enumerate(li)if i not in (0,4,5)]
# print(li)

# 83
# li = [12, 24, 35, 70, 88, 120, 155]
# # li.remove(24)
# # print(li)

# 84
# 打印两个列表的交集
# set1 = set([1,3,6,78,35,55])
# set2 = set([12, 24, 35, 70, 88, 120, 155])
# set1 &= set2
# li = list(set1)
# print(li)

# 85
# li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# set1 = set(li)
# li2 = list(set1)
# li2.sort()
# print(li2)

# 86
# class Person(object):
#     def getGender(self):
#         print("human")
# class Male(Person):
#     def getGender(self):
#         super().getGender()
#         print("Male")
# class Female(Person):
#     def getGender(self):
#         super().getGender()
#         print("Female")
#
# man = Male()
# man.getGender()
# woman = Female()
# woman.getGender()

# 87
# s = 'abcdefgab'
# dict ={}
# for i in s:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
#
# print("\n".join(['%s,%s' % (k, v)for k, v in dict.items()]))

# 88
# x = ["ll", "uu", "kk", "hh"]
# y = [1,2,3,4,5,6]
# for x1,y1 in zip(x, y):
#     print(x1,y1)

# 89
# my_string  = "rise to vote sir:"
# li = list(my_string)
# li = li[::-1]
# print(li)

# 90
# s = "H1e2l3l4o5w607r8l9d"
# li = list(s)
# li = li[::2]
# print(li)

# 91
# 打印[1,2,3]所有的排列
#

# 92
# 鸡兔同笼
# def solve(numhead, numlegs):
#     ns = "No solutions"
#     for i in range(numhead + 1):
#         j = numhead - i
#         if 2*i + 4*j == numlegs:
#             return i, j
# print(solve(35,94))

# 93

# 94
# s = "hello_world_yoyo"
# li = s.split("_")
# print(li)

# 95
# 打印99乘数表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{i} x {j} = {i*j}", end=" ")
#     print('\n')

# 96
# 输入一个姓名，判断是否姓王？
# s = "朱增宽"
# li = list(s)
# if li[0] == "王":
#     print("确实姓王")
# else:
#     print("不姓王")

# 97
# import re
# s = "Hello, welcome to my world."
# res = re.findall("w",s)
# print(len(res))

# 98
a = [1, -6, 2, -5, 9, 4, 20, -3]
for i in range(len(a)):
    a[i] = abs(a[i])
print(a)