# 1. 协程：单线程下的开发，又称为微线程
# 注意：线程和进程的操作是由程序触发系统接口，
# 最后的执行者是系统，协程的操作则是程序员
# 1.1 简单实现协程
# import time
# def task1():
#     while True:
#         yield "哈哈哈"
#         time.sleep(1)
# def task2():
#     while True:
#         yield "嘿嘿嘿"
#         time.sleep(1)
#
# if __name__ == "__main__":
#     t1 = task1()
#     t2 = task2()
#     # print(next(t1))
#     # print(next(t1))
#     # print(next(t2))
#     while True:
#         print(next(t2))
#         print(next(t1))
# 1.2 应用场景
#   1.如果线程里有io操作比较多的情况，可以用协程
#       Input/Output
#       常见io操作：文件操作，网络请求
#   2.适合高并发处理

# 2.greenlet：是一个由c语言实现的协程模块，通过设置switch()来实现任意函数之间的切换
# 2.1 安装
# 安装： pip install 模块名
# 卸载： pip uninstall 模块名
# 查看已安装的模块：pip list
# 2.2 注意：greenlet属于手动切换，当遇到IO操作，程序会阻塞，而不能自动切换
# 2.3 通过greenlet实现任务的切换
# 导入模块
# from greenlet import greenlet
# def sing():
#     print("在唱歌")
#     g2.switch()
#     print("唱完歌了")
# def dance():
#     print("在跳舞")
#     print("跳完舞了")
#
# if __name__ == "__main__":
#     # 创建协程对象    greenlet（任务名）
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#     g1.switch()     # 切换到g1中去运行
#     g2.switch()

# 3.gevent: 遇到IO操作是，会进行自动切换，属于主动式切换
# 注意：文件命名不要和第三方模块或内置模块重名

# 3.1 使用
import gevent
import time
# gevent.spawn(函数名):创建协程对象
# gevent.sleep():    耗时操作
# gevent.join():     阻塞，等待某个协程执行结束
# gevent.joinall():  等待所有协程对象都执行结束再退出，参数是一个协程对象列表
# 3.2 gevent自带耗时操作
# def sing():
#     print("在唱歌")
#     gevent.sleep(2)
#     print("唱完歌了")
# def dance():
#     print("在跳舞")
#     gevent.sleep(3)
#     print("跳完舞了")
#
# if __name__ == "__main__":
#     # 1. 创建协程对象
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     # 2. 阻塞，等待协程执行完成
#     g1.join()       # 等待g1执行结束
#     g2.join()
# 3.3 joinall()
# def sing(name):
#     for i in range(3):
#         gevent.sleep(1)
#         print(f"{name}在唱歌，被送走的第{i}次")
# if __name__ == "__main__":
#     gevent.joinall([
#         gevent.spawn(sing, "bingbing"),
#         gevent.spawn(sing, "susu")
#     ])

# joinall(): 等待所有的协程任务都执行结束后，再退出

# 3.4 monkey补丁：拥有在模块运行时替换的作用
# 导入模块
from gevent import monkey
monkey.patch_all()      # 将用到的time.sleep()代码替换成gevent里面自己实现耗时操作的gevent.sleep()代码
# 注意：monkey.patch_all()这句话，必须放在，被打补丁的前面
def sing(name):
    for i in range(3):
        time.sleep(1)
        print(f"{name}在唱歌，被送走的第{i}次")
if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(sing, "bingbing"),
        gevent.spawn(sing, "susu")
    ])

# 4.总结：
# 4.1 线程是cpu调度的基本单位，进程是资源分配的基本单位
# 进程、线程、协程的对比
#       进程：切换需要的资源最大，效率最低
#       线程：切换需要的资源一般，效率一般
#       协程：切换需要的资源最小，并且效率高
# 4.3 多线程适合IO密集型操作（文件操作，爬虫）
#       多进程适合CPU密集型操作（科学计算，对视频进行高清解码，计算圆周率）
# 4.4 进程、线程、协程都是可以完成多任务的，可以根据自己的实际开发需要选择使用

