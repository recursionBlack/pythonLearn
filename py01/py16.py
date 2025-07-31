# 上节课总结
# 实例指的是具体的对象
# 1.实例方法:方法内部访问实例属性，方法内部可以通过类名，类属性名，来访问类属性
# 2.静态方法@staticmethod:方法内部，不需要访问实例属性和类属性
# 如果要访问类属性，通过类名.类属性名访问，不能访问实例属性
# 3.类方法@classmethod: 方法内部只需要访问类属性，可以通过cls.类属性名访问，不能访问实例属性
class Person(object):
    name = "小明"           # 类属性：类所拥有的属性
    def __init__(self):
        self.age = 18       # 实例属性：对象私有的
    def play(self):         # 实例方法
        # 在实例方法中访问类属性
        print(f"{Person.name}在玩游戏")
        print(self.age)
    @staticmethod           # 静态方法：类中函数，形参没有限制
    def introduce():
        print(f"我是{Person.name}") # 静态方法能够访问到类属性，但没有意义
    @classmethod            # 类方法：针对类存在的方法
    def introduce2(cls):    # 代表类对象本身
        print(Person.name)
        print(cls.name)
        # print(self.age)   # 不能访问到实例属性
pe = Person()
pe.play()

# 总结：类属性是公共的，所有方法内部都能访问到，静态方法不需要访问类属性
# 因为静态方法，和类，对象，都没有关联
# 实例属性是私有的，只有实例方法内部能够访问到（self作为传参），

# 本节课
# 1. __init__()和__new__()
# 1.1 __init__():初始化对象
class Test(object):
    def __init__(self):
        print("这是__init__()")
te = Test()
# 1.2 __new__():object基类提供的内置的静态方法
# 作用：1.在内存中为对象分配空间，2.返回对象的引用
class Test2(object):
    def __init__(self):
        print("这是__init__()")
    def __new__(cls, *args, **kwargs):
        print("我是__new__()")
        print(cls)
        # 对父类方法尽心扩展： super().方法名()
        res = super().__new__(cls)      # 方法重写，res里面保存的是实例对象的引用
        # __new__()是静态方法，形参里面有cls，实参就必须传cls
        return res
        # 注意：重写__new__()一定要return super().__new__(cls)
        # 否则python解释器，就得不到分配空间的对象引用，就不会调用__init__()
te = Test2()
print("te:", te)

# 执行步骤：
# 一个对象的实例化过程：首先执行__new__(),如果没有写，则会调用父类里面的__new__()
# 返回一个实例对象的引用，然后再去调用__init__(),对对象进行初始化
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("这是new方法")
        print("返回值：", super().__new__(cls))
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name
        print("名字是：", self.name)
pe = Person("bingbing")
print(pe)
pe2 = Person("susu")
print(pe2)

# 总结一下：
# 1.__new__()是创建对象，__init__()是初始化对象
# 2.__new__()是返回对象引用，__init__()是定义实例属性
# 3.__new__()是类级别的方法，__init__()是实例级别的方法
# 没有前者，就没有后者


# 2. 单例模式
# 可以理解成一个特殊的类，这个类只存在一个对象
# 优点：可以节省内存空间，减少了不必要的资源浪费
# 弊端：多线程访问时，容易引发线程安全的问题
# 2.2 方式
# 1.通过@classmethod
# 2.通过装饰器实现
# 3.通过重写__new__()实现     （重点）
# 4.通过导入模块实现

class A(object):
    pass
a1 = A()
print(a1)
a2 = A()
print(a2)
# 内存地址发生变化说明是不同的对象
# 实现单例模式    对象的内存地址都是一样的，只有一个对象
# 2.3 通过重写__new__()实现单例模式
# 设计流程
# 1.定义一个类属性，初始值为None，用来记录单例对象的引用
# 2.重写__new__()方法
# 3.进行判断，如果类属性是None，把__new__()返回对象的引用保存进去
# 4. 返回类属性中记录的对象引用
class Singleton(object):
    # 记录第一个被创建的对象的引用
    obj = None      # 类属性
    def __new__(cls, *args, **kwargs):
        print("这是__new__()方法")
        # 判断类属性是否为空
        if cls.obj == None:
            cls.obj = super().__new__(cls)
        return cls.obj
    def __init__(self):
        print("我是__init__()")
s = Singleton()
print("s:", s)
s2 = Singleton()
print("s2:", s2)
s3 = Singleton()
print("s3:", s3)
# 单例模式：每一次实例化所创建的对象都是同一个，内存地址都一样

# 2.4 通过导入模块实现单例模式
# 模块就是天然的单例模式
from pytest02 import te as te01
from pytest02 import te as te02
print(te01, id(te01))
print(te02, id(te02))

# 2.5 应用场景
# 1. 回收战对象
# 2. 音乐播放器， 一个音乐播放软件，负责音乐播放的对象
# 3. 开发游戏软件     场景管理器
# 4. 数据库配置、数据库连接池的设计

# 3. 魔法方法
# 3.1 __doc__()：类、函数的描述信息
class Person(object):
    """人类---类的描述信息"""       # 只能使用多行注释，单行注释无效
    pass
print(Person.__doc__)
def sing():
    """唱歌"""
    pass
print(sing.__doc__)
# 3.2 __module__()：表示当前操作对象所在的模块
# 3.3 __class__()：表示当前操作对象所在的类
class B:
    def funa(self):
        print("哈哈哈")
# 3.4 __str__():对象的描述信息
# 如果类中定义了此方法，那么在打印对象时，默认输出该方法的返回值
# 也就是打印方法中的return数据
# 注意：__str__()必须返回一个字符串
class C:
    def __str__(self):
        return "这里是str的返回值"     # 必须要返回值，并且一定是字符串类型
c = C()
print(c)
# 3.5 __del__(): 析构函数，在程序结束时被调用，
# 或者删除某个对象时也会被调用
# 3.6 __call__()： 使一个实例对象成为一个可调用对象，就像函数那样可以 调用
# 可调用对象：函数，内置函数，和类都是可调用对象
# 凡是可以把一()应用到某个对象身上，都可以被称作可调用对象
# callable():判断一个对象，是否是可调用对象
def func():
    print("呵呵呵")
func()
print(callable(func))   # True
name = "bingbing"
print(callable(name))   # False

class A:
    def __call__(self, *args, **kwargs):
        print("这是一个__call__()")
a = A()
a()         # 调用一个可调用的实例对象，其实就是在调用它的__call__()方法
print(callable(a))