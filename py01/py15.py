# 1.继承
# 就是让类和类之间转变为父子关系，子类默认继承父类的属性和方法
# 1.1 语法
# class 类名（父类名）：
#   代码块
# 1.2 单继承
class Person:
    def eat(self):
        print("我会吃饭")
    def sing(self):
        print("我是唱歌小能手")
class Girl(Person):
    pass            # 占位符，代码里面不写任何东西，会自动跳过
class Boy(Person):
    pass
girl = Girl()
girl.eat()
girl.sing()
boy = Boy()
boy.eat()
boy.sing()
# 总结： 子类可以继承父类的属性和方法，就算子类自己没有，也可以使用父类的
# 1.3 继承的传递性
# A/B/C C（子类）继承于B（父类），B类（子类）继承A类（父类）
# 子类拥有父类的父类的属性和方法
class Father:
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")
class Son(Father):
    pass
class Grandson(Son):
    pass
son = Son()
son.eat()
son.sleep()
grandson = Grandson()
grandson.eat()
grandson.sleep()

# 1.4 重写：指在子类中定义与父类相同名称的方法
# 1.4.1 覆盖父类的方法
class Person2:
    def money(self):
        print("一百万需要被继承")
class Man(Person2):
    def money(self):
        print("自己赚一千万")
man = Man()
man.money()
# 1.4.2 对父类方法进行扩展：
# 继承父类的方法，子类也可以增加自己的功能
# 1.父类名.方法名（self）
# 2.super().方法名（）   --推荐使用,懒人写法
# super在python里面是一个特殊的类，
# super（）实例化了一个匿名对象，可以调用父类方法
# 3.super(子类名, self).方法名()
# 推荐第二种
class Person3:
    def money(self):
        print("一百万需要被继承")
    def sleep(self):
        print("睡觉了")
class Man(Person3):
    def money(self):
        # Person3.money(self)
        # super().money()
        super(Man, self).money()
        print("自己赚一千万")
man = Man()
man.money()

# 2.新式类写法
class A:        # 经典类：不由任意内置类型派生出的类
    pass
class Animal:
    def walk(self):
        print("我会走路")
class Dog(Animal):
    name = "富贵"

# 2.3 class A(object)       新式类：继承了object或者该类的子类
# object --对象，python为所有对象提供的基类（顶级父类）
# 提供了一些内置的属性和方法，可以使用dir()查看
# print(dir(object))
# python3中，如果一个类没有继承任何类，则默认继承object类
# 因此，python3都是新式类

# 3.多继承
# 子类可以拥有多个父类，并且具有所有父类的属性和方法
class Father(object):
    def money(self):
        print("拥有一百万需要被继承")
class Mother(object):
    def money(self):
        print("拥有一百二十万需要被继承")
    def appearance(self):
        print("绝世容颜需要被继承")
class Son(Father, Mother):      # 子类
    def money(self):
        print("拥有十万")
son = Son()
son.money()
son.appearance()

# 3.2 不同的父类存在同名的方法
# 开发时，需要尽量避免这种情况
# 有多个父类的属性和方法，如果多个父类具有同名的方法的时候
# 调用就近原则，括号内哪个离得更近，优先调用哪一个类的方法

# 3.3 方法的搜索顺序（了解）、
# python中的内置属性__mro__可以查看方法搜索顺序
print(Son.__mro__)
# 搜索方法时，会先按照__mro__的输出结果，从左往右的顺序查找
# 如果找到了就直接执行，不再搜索
# 如果找到最后一个类，也没找到这个方法，则程序就会报错
# 3.4 多继承的弊端
# 容易引发冲突
# 会导致代码的设计的复杂度增加

# 4.6 多态
# 指同一种行为，具有不同的表现形式
# 前提：继承，重写
print(10 + 10)      # 算数运算符：可以实现整型之间的相加操作
print('10'+'10')    # 字符串拼接：实现字符串之间的拼接操作
class Animal(object):
    def shout(self):
        print("动物会叫")
class Cat(Animal):
    def shout(self):
        print("小猫喵喵喵")
class Dog(Animal):
    def shout(self):
        print("小狗汪汪汪")
cat = Cat()
cat.shout()
dog = Dog()
dog.shout()
# 4.2 多态性：一种调用方式，不同的执行结果
class Animal(object):
    def eat(self):
        print("我会干饭")
class Pig(Animal):
    def eat(self):
        print("猪吃猪饲料")
class Dog(Animal):
    def eat(self):
        print("狗吃狗粮")
# 多态性:定义一个统一的接口，一个接口多种实现
def test(obj):
    obj.eat()
animal = Animal()
pig = Pig()
dog = Dog()
test(animal)
test(pig)
test(dog)
# test函数传入不同的对象，执行不同的eat方法

# 5. 静态方法
# 使用@staticmethod 来进行修饰，静态方法没有self，cls的参数限制
# 静态方法与类无关，可以被转换为函数使用
class Person(object):
    @staticmethod   # 静态方法
    def study(name):
        print(f"{name}会学习")
# 静态方法即可用对象访问，也可以使用类访问
# 取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗

# 6. 类方法
# 使用 装饰器@classmethod来标识类方法
# 对于类方法，第一个参数，必须是类对象
# 一般是以cls作为第一个参数
# class 类名：
#   @classmethod
#       def 方法名（cls，形参）：
#           方法体
# 类方法内部可以访问类属性，或者调用其他的类方法
class Person(object):
    name = "bingbing"
    @classmethod
    def sleep(cls):
        print("cls", cls)
        print("人类在睡觉")
        print(cls.name)
print(Person)
Person.sleep()
# 当方法中需要使用到类对象(如访问到私有类属性等），定义类方法
# 类方法一般是配合类属性使用

