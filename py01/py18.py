# 1.可迭代对象iterable
# 遍历（迭代）：依次从对象中，把一个个元素取出来的过程
# 数据类型：str, tuple, dict, set等
# for i in 1234:
#     print(i)
# 1.2 可迭代对象的条件
# 1.对象实现了__iter__()方法
# 2.__iter__()方法返回了迭代器对象
# 1.3 for循环工作原理
# 1. 先通过__iter__()获取可迭代对象的迭代器
# 2. 对获取到的迭代器不断调用__next__()方法来获取下一个值，并将其赋值给临时变量i
# 1.4 isinstance(): 判断一个对象是否是可迭代对象或者是一个已知的数据类型
# 导入模块
from collections.abc import Iterable
st = '123'
# isinstance(o,t):o:对象，t：类型，可以是直接或间接类名，基本类型或元组
print(isinstance(123, Iterable))
print(isinstance(123, int))
print(isinstance('123', int))
print(isinstance('123', Iterable))

for i in "abc":
    print(i)
# 2. 迭代器Iterator
# 是一个可以记住遍历位置的对象：在上次停留的位置，继续去做一些事
li = [1,2,3,4,5]
for i in li:
    print(i)
# iter():获取可迭代对象的迭代器
# next():一个个去取元素，取完元素后，会引起一个一场异常
# 1. 创建迭代器对象
li2 = iter(li)
print(li2)
# 2. 获取下一条数据
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))
print(next(li2))
print(dir(li))
# 3.取完元素后，再使用next()会引发StopIteration异常

# 步骤：
# 1.iter()调用对象的__iter__()，并把__iter__()方法的返回结果作为自己的返回值
# 2.next()调用对象的__next__()，一个个取元素
# 3.所有元素都取完了，__next__()将引发StopIteration异常

# 2.2 可迭代对象Iterable与迭代器Iterator的区别
# 凡是可以作用于for循环的都属于可迭代对象
# 凡是可以作用于next()的都是迭代器
from collections.abc import Iterable, Iterator
name = "bingbing"
print(isinstance(name, Iterable))
print(isinstance(name, Iterator))
name2 = iter(name)
print(isinstance(name2, Iterable))
print(isinstance(name2, Iterator))
# 总结：
# 可迭代对象可以通过iter()转换成迭代器对象
# 如果一个对象拥有__iter__()，是可迭代对象，
# 如果一个对象拥有__iter__()和__next__()是迭代器对象
# 迭代器对象一定是可迭代对象

# 2.3 迭代器协议
# 对象必须提供一个next方法，执行该方法要么就返回迭代中的下一项
# 要么引发StopIteration异常，来终止迭代

# 2.4 自定义迭代器类
# 两个特性：__iter__()和__next__()
# class Test(object):
#     # 初始值是1， 逐步递增1
#     def __init__(self):
#         self.num = 1
#     def funa(self):
#         print(self.num)
#         self.num += 1
# te = Test()
# print(te)
# te.funa()
# for i in range(5):
#     te.funa()

# class MyIterator(object):
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num == 10:
#             raise StopIteration("终止当前迭代，数据已经被取完")
#         self.num += 1
#         return self.num
# mi = MyIterator()
# print(mi)
# print(next(mi))
# for i in mi:
#     print(i)

# 3.生成器
# Python中，一边循环，一边计算的机制，叫做生成器
# 生成器需要程序员自己实现
# 3.1 生成器表达式
# 列表推导式
li = [i*5 for i in range(5)]
gen = (i*5 for i in range(5))       # 列表推导式的[]改为()就成了生成器表达式
print(li)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

# 3.2 生成器函数
# Python中，使用了yield关键字的函数，就称之为生成器函数
# yield的作用：
# 1.类似于return，将指定值或者多个值返回给调用者
# 2.yield语句一次返回一个结果，在每个结果中间，
#   挂起函数，执行next(),再重新从挂起点执行
#   是函数中断，并保存中断的状态
# def test():
#     li = []
#     li.append("a")
#     li.append("b")
#     print("li:", li)
#
# # 生成器函数
# def gen():
#     print("开始了")
#     yield 'a'           # 返回一个‘a',并暂停函数，在此处挂起，下一次再从此处执行
#     yield 'b'
#     yield 'c'
#
# gen01 = gen()
# print(gen01)
# print(next(gen01))
# print(next(gen01))
# print(next(gen01))

def gen2(n):
    li = []
    a = 0
    while a < n:
        li.append(a)
        yield a
        a += 1
    print("li", li)
for i in gen2(5):
    print(i)

# 使用了yield关键字，就是生成器函数
def test_a():
    yield 1
    yield 2
    yield 3
print(test_a())
ta = test_a()
print(next(ta))     # 从对象中取值
print(next(ta))
print(next(ta))
print(next(test_a()))       # 加括号是调用函数，每一次都从头开始
print(next(test_a()))

# 4. 三者关系
# 可迭代对象：指实现了Python迭代协议，可以通过for .. in .. 循环遍历的对象
# 比如list、dict、str、set、tuple，
# 甚至还包含了迭代器和生成器
# 迭代器：可以记住自己遍历位置的对象，直观体现就是可以使用next()函数返回值，
# 迭代器只能往前，不能往后，当遍历完毕后，next()会抛出异常
# 生成器：本质上就是一个迭代器，是特殊的迭代器
#   是Python提供的通过简便的方法，写出迭代器的一种手段
# 包含关系：可迭代对象 > 迭代器 > 生成器