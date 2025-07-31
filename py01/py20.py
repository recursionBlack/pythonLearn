# 20. 进程
# 1.1 含义
# 是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
#   一个正在运行的程序或者软件，就是一个进程
#   程序跑起来，就成了进程
# 注意：进程里面可以创建多个线程，多进程也可以完成多任务
# 1.2 进程的状态
# 1.就绪状态：运行的条件，都已经满足，正在等待cpu执行
# 2. 执行状态：cpu正在执行其功能
# 3. 等待（阻塞）状态：等待某些条件满足，如一个程序sleep了，此时就处于等待状态
import time
# print("我是冰冰")   # 程序开始，处于执行状态
# sex = input("输入性别：")   # 光标闪动，等待用户输入，处于等待状态
# print(sex)
# time.sleep(1)       # 延迟1秒，等待（阻塞）状态

# 2. 进程语法结构
# multiprocessing模块提供了Process类代表进程对象
# 2.1 Process 类参数
# 1.target:执行的目标任务名，即子进程要执行的任务
# 2.args：以元组的形式传参
# 3.kwargs：以字典的形式传参
# 2.2 方法
#   1.start():开启子进程
#   2.is_alive()：判断子进程是否还活着，存活返回True，死亡返回False
#   3.join():主进程等待子进程执行结束
# 2.3 常用的属性
# name: 当前进程的别名，默认Process-N
# pid:  当前进程的进程编号
from multiprocessing import Process, Queue
import os
# def sing():
#     # os.getpid():获取当前进程编号
#     # os.getppid():获取当前父进程编号
#     # 父进程的id，就是py文件主进程的pid
#     print(f"sing子进程编号：{os.getpid()}，父进程id：{os.getppid()}")
#     print("唱歌")
# def dance():
#     print(f"dance子进程编号：{os.getpid()}，父进程id：{os.getppid()}")
#     print("跳舞")
# if __name__ == "__main__":
#     # 创建子进程
#     # 修改子进程名，创建时，就复制
#     p1 = Process(target=sing, name="子进程一")
#     p2 = Process(target=dance, name="子进程二")
#     p1.start()
#     p2.start()
#     # 修改子进程名，创建后再修改
#     p1.name = "子进程1"
#     p2.name = "子进程2"
#     # 访问name属性
#     print("p1:", p1.name)
#     print("p2:", p2.name)
#     # 查看子进程的进程编号
#     print("p1.pid", p1.pid)
#     print("p2.pid", p2.pid)
#     print(f"主进程Pid：{os.getpid()},主进程的父进程pid：{os.getppid()}", )
#     # 主进程的父进程，就是pycharm64软件的进程
#     # 可以在cmd中输入tasklist查看电脑的所有进程
# def eat(name):
#     print(f"{name}在干饭")
# def sleep(name):
#     print(f"{name}在睡觉")
# if __name__ == "__main__":
#     p1 = Process(target=eat, args=("bingbing",))
#     p2 = Process(target=sleep, args=("ziyi",))
#     p1.start()
#     p1.join()   # 主进程处于等待的状态，p1是运行状态
#     p2.start()
#     p2.join()
#     print("p1存活状态：", p1.is_alive())
#     print("p2存活状态：", p2.is_alive())
# 写在主进程中判断存活状态的时候需要加入join阻塞一下

# 2.4 进程间，不共享全局变量
# 读取一直为空，进程不共享全局变量

# 3.进程间的通信
# Queue(队列）
# q.put(): 放入数据
# q.get(): 取出数据
# q.empty(): 判断队列是否为空
# q.qsize(): 返回当前队列包含的消息数量
# q.full():  判断队列是否满了
# from queue import Queue
# 初始化一个队列对象
# q = Queue(3)        # 最多可以接受三条消息，没写或者是负值，就是没有上限
# q.put("爱你到老")
# q.put("你在做梦")
# print("是否满了：", q.full())
# q.put("年轻人不讲武德")
# print(q.qsize())
# print(q.get())      # 获取队列的一条消息，并将其从队列中移除
# print(q.get())
# print(q.empty())
# print(q.get())
# print(q.empty())
# print(q.qsize())

li = ["张三", "李四", "王麻子", "赵六"]
def wdata(q1):
    for i in range(5):
        print(f"{i}已经被放入")
        q1.put(i)
        time.sleep(0.2)
    print("写入的数据是：", li)
# 读取数据
def rdata(q2):
    while True:
        # 判断是否为空，队列为空就退出循环
        if q2.empty():
            break
        else:
            print("取出数据", q2.get())
    print("读取的数据是：", li)
# 1. 防止别人导入文件的时候，执行main里面的方法
# 2. 防止window系统递归创建子进程
if __name__ == "__main__":
    # 创建队列对象
    q = Queue()
    p1 = Process(target=wdata, args=(q,))
    p2 = Process(target=rdata, args=(q,))
    p1.start()
    p1.join()       # 阻塞等待队列中的数据放入完成
    p2.start()
