class Preson:
    name = "bingbing"
    def run(self):
        print("人会走路")
        print("run方法的self", self)
    def introduce(self):
        print("我是实例方法")
        print(f"{Preson.name}的年龄：{self.age}")
# 实例化对象 变量名 = 类名+（）
pe = Preson()
print(pe)
pe.run()
pe.age = 18
pe.introduce()
# 类属性和实例属性的区别：
# 类属性属于所有的类对象，实例属性仅仅属于某个实例
# 实例属性只能由对象访问，不能由类名访问
pe.sex = "女"
# print(Preson.sex)
print(pe.sex)

# 构造函数__init__()
# 作用：通常用来做属性初始化或者赋值操作
# 注意：在类的实例化对象的时候，会被自动调用
class Test:
    def __init__(self):
        print("这是一个__init__()函数")

class Person:
    def __init__(self):
        self.name = "bingbing"
        self.age = 18
        self.height = 183
    def play(self):
        print(f"{self.name}在打王者荣耀")
    def introduce(self):
        print(f"{self.name}的年龄是{self.age}")
pe2 = Person()
pe2.play()
pe2.introduce()

# 析构函数 __del__()
# 删除对象时，解释器会默认调用__del__()方法
class Person2:
    def __init__(self):
        print("我是__init__()")
    def __del__(self):
        print("被销毁了")
p = Person2()
del p
print("这是最后一行代码")
# def __del__()主要是表示该程序块或者函数已经全部执行结束

# 封装：指的是隐藏对象中，一些不希望被外部访问到的属性或方法细节
class Person3():
    name = "bingbing"
pe = Person3()
print(pe.name)
Person.name = "ziyi"
print(Person.name)

# 隐藏属性（私有权限），只允许类内的方法访问，无法通过对象访问
# 在属性名或者方法名前面加上两个下划线
class Person4():
    name = "James"
    __age = 28  # 隐藏属性
    def introduce(self):
        print(f"{Person4.name}的年龄是{Person4.__age}")

pe = Person4()
print(pe.name)
# print(pe.__age) 不可访问隐藏属性
# 隐藏属性实际上是将名字修改为：_类名__隐藏属性名
# 了解，一般不使用
print(pe._Person4__age)

# 正规访问私有属性的方法：通过实例化方法,在类的内部访问
pe.introduce()

# 私有属性或方法
# 1.xxx: 普通属性或方法，如果是类中定义的，则类可以在任意地方使用
# 2._xxx:单下划线开头，声明私有属性方法，如果定义在类中，外部可以
# 使用，子类也可以继承
# 一般是为了避免与Python关键字冲突而采用的命名方法
# 3.__xxx：双下划线开头，隐藏属性，如果定义在类中，无法在外部直接访问
# 子类不会继承，要访问只能通过间接的方法。另一个文件通过from xxx import导入时，也无法导入
# 这种命名一般是python中的魔法方法或属性，都是有特殊含义或功能的
# 自己不要轻易定义
class Person5:
    name = "颂雪情雁"
    __age = 54          # 隐藏属性
    _sex = "不男不女"   # 私有属性

pe = Person5()
# print(pe.sex) # 报错
# 使用对象名._属性名调用
print(pe._sex)
# print(pe.__age) # 访问不到
print(pe._Person5__age) # 不正规手段强行访问

class Man:
    def __play(self):       # 隐藏方法
        print("玩手机")
    def funa(self):         # 平平无奇的实例方法
        print("平平无奇的实例方法")
        ma.__play()         # 在实例化方法中调用私有方法，不推荐

ma = Man()
ma.funa()
# ma.__paly()
ma._Man__play()

# 私有方法
class Girl:
    def _buy(self):
        print("整天买买买")
girl = Girl()
girl._buy()