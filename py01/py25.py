# 导入模块
import os
import sys
import time
import logging
import random
# 1.os模块
# 作用：用于和操作系统进行交互
# 1.os.name     # 指示正在使用的工作平台（windows或linux）
# print(os.name)
# 对于windows 返回nt，对于Linux，返回posix
# 2. os.getenv(环境变量名称)      # 读取环境变量
# print(os.getenv("path"))
# 3.os.path.split()     # 把目录名和文件名分离，以元组形式接收，第一个元素是目录路径，第二个是文件名
# print(os.path.split(r"C:\Users\Admin\Desktop\工件焊缝\CB06S.stl"))
# 4.os.path.dirname:    # 显示split分割的第一个元素，即目录
# 5.os.path.basename:   # 显示split分割的第二个元素，即文件名
# print(os.path.dirname(r"C:\Users\Admin\Desktop\工件焊缝\CB06S.stl"))
# print(os.path.basename(r"C:\Users\Admin\Desktop\工件焊缝\CB06S.stl"))
# print(os.path.basename(r"C:\Users\Admin\Desktop\工件焊缝/"))    # 如果以反斜杠结尾，会报错，以斜杠结尾，则为空的
# 6.os.path.exists()    # 判断路径（文件或目录）是否存在，存在的话，就返回True，不存在返回False
# print(os.path.exists(r"C:\Users\Admin\Desktop\工件焊缝\CB06S.stl"))
# 7.os.path.isfile()    # 判断文件是否存在
# print(os.path.isfile(r"C:\Users\Admin\Desktop\工件焊缝\CB06S.stl"))
# print(os.path.isfile(r"C:\Users\Admin\Desktop\工件焊缝"))
# 8.os.path.isdir()     # 判断目录是否存在
# print(os.path.isdir(r"C:\Users\Admin\Desktop\工件焊缝\CB06S.stl"))
# print(os.path.isdir(r"C:\Users\Admin\Desktop\工件焊缝"))
# 9.os.path.abspath()   # 获取当前路径下的绝对路径
# 10. os.path.isabs()   # 判断是否是绝对路径
# print(os.path.abspath("py25"))

# 2.sys模块
# 作用：负责程序跟python解释器的交互
# 1.sys.getdefaultencoding()    # 获取系统默认编码格式
# print(sys.getdefaultencoding())
# 2.sys.path:   获取环境变量的路径，跟解释器相关
# print(sys.path)     # 以列表形式返回，第一项为当前所在的工作目录
# 3.sys.platform      # 获取操作系统平台名称
# print(sys.platform)
# 4.sys.version       # 获取python解释器的版本信息
# print(sys.version)


# 3.time模块
# 三种时间表示：
# 时间戳（timestamp）
# 格式化的时间字符串（format time）
# 时间元组（struct_time）
# 1.time.sleep()    # 延时操作，以秒为单位
# print(12)
# time.sleep(3)
# print(123)
# 2.time.time()     # 获取到当前的时间戳，以秒计算，从1970年1月1日00：00：00，到现在的时间差
# print(time.time())      # 返回的是浮点型
# 3.time.localtime()        # 将一个时间戳转换为当前时区的localtime
# t = time.localtime()
# print(t.tm_year)
# 4.time.asctime()  # 获取系统当前时间,把时间元组换成固定的字符串
# print(time.asctime())
# 5.time.ctime()    # 获取系统当前时间，把时间戳转换成固定的字符串表达式
# print(time.ctime())
# 6.time.strftime（格式化字符串，struct_time）   # 将struct_time转换成时间字符串
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 7.time.strptime(时间字符串，格式化字符串)     # 将时间字符串转换为struct_time
# print(time.strptime("2025-07-14","%Y-%m-%d"))

# 4.logging模块
# 1.作用：用于记录日志信息
# 2.日志的作用
#   1.程序调试
#   2.了解软件程序运行情况是否正常
#   3.软件程序运行故障分析与问题定位
# 3.级别排行，从高到低
# CRITICAL > ERROR > WARNNING > INFO > DEBUG > NOTEST
# logging.debug("我是debug")
# logging.info("我是info")
# logging.warning("我是warning")
# logging.error("我是error")
# logging.critical("我是critical")
# logging默认的level就是warnning，也就是logging只会显示级别大于等于warnning的日志信息
# 4. logging.basicConfig()  # 配饰root logger的参数
#   1.filename：指定日志文件的文件名，所有会显示的日志，都会存放到这个文件中
# logging.basicConfig(filename="log.log")
#   2.filemode: 文件的打开方式，默认是a，追加模式
# logging.basicConfig(filename="log.log", filemode="a")
# 3.level: 指定日志显示级别，默认是警告信息warnning
# logging.basicConfig(filename="log.log", filemode="a", level=logging.NOTSET)
# 4.format: 指定日志信息的格式
# logging.basicConfig(filename="log.log", filemode="a",
#                     level=logging.NOTSET, format="%(levelname)s:%(asctime)s\t%(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# 5.    random模块
# 作用：用于实现各种分布的伪随机数生成器，可以根据不同的实数分布，来随机生成值
# 1.random.random()     # 产生大于0且小于1之间的小数
# print(random.random())
# 2.random.uniform()    # 产生指定范围的随机小数
# print(random.uniform(1,3))
# 3.random.randint()    # 产生指定范围内的随机整数，包含开头和结尾
# print(random.randint(1,3))
# 4.random.randrange(start,stop, [step])    # 产生start到stop的随机整数，左开右闭
#   step ：步长，指定产生随机的步长，随机选择一个数据
# print(random.randrange(2,7,2))