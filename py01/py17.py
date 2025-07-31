# 1. 文件
# 文件就是存储某种长期存储设备上的一段数据
# 1.2 文件操作
# 打开文件  --->读写文件---》关闭文件
# 1.3 文件对象的方法
# 1.open():创建一个file对象，默认是以只读模式打开
# 2.read(n)：n表示从文件中读取的数据的长度，没有传n值，就默认全部读取
# 3.write(): 将指定内容写入文件
# 4.close()：关闭文件
# 1.4 属性
# 文件名.name: 返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode：返回文件的访问模式
# 文件名.closed:检测文件是否关闭，关闭的话，就返回True
# 1.打开文件
f = open('test.txt')
print(f.name)   # 文件名
print(f.mode)   # 文件的访问模式
print(f.closed) # 判断文件是否关闭呢
# 2.关闭文件
f.close()
print(f.closed)

# 2.读写操作
# 2.1 read(n):n表示从文件中读取的数据的长度，
# 没有传n值或传的负值，就默认一次性读取全部
f = open("test.txt")
# print(f.read())
print(f.read(5))    # 最多读取5个数据
f.close()

# 2.2 readline()：逐行读取，方法执行完，会把文件指针，移到下一行
f = open("test.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# while True:
#     text = f.readline()  # 读取一行内容
#     # 读取不到内容，就退出循环
#     if not text:
#         break
#     print(text)
# for i in f:
#     text = f.readline()
#     if not text:
#         break
#     print(text)
# f.close()

# 2.3 readlines(): 按照行的方式把文件内容一次性读取，
# 返回的是一个列表，每一个元素就是一行的内容
# f = open("test.txt")
# text = f.readlines()
# print(text)             # 返回列表
# print(type(text))       # <class "list">
# f.close()

# 2.4 访问模式
# 2.4.1 r:只读模式（默认模式），文件必须存在，不存在就会报错
# 2.4.2 w:只写模式，文件存在就先清空文件内容，再写入添加内容，不存在就创建文件
file = open("test.txt", 'w')
# print(file.read())
file.write("zzkzkzkjib")    # 重新编辑文件内容，原有内容被覆盖
file.close()

# 2.4.3 +：表示可以同事读写某个文件
# 使用+会影响文件的读写效率。开发过程中，更多时候只会以只读、只写的方式操作文件
# r+: 可读写文件，文件不存在就会报错
# w+：先写再读，文件存在就重新编辑文件，不存在就创建文件
# f = open('test.txt', 'w+')
# print(f.read())
# f.close()

# 2.4.4 a:追加模式，不存在就创建新文件进行写入，存在就在原有文件的内容基础上添加内容
f = open("test.txt","a")
f.write("test is being written")
f.close()
# 文件指针：标记从哪个位置开始读取数据，类似于光标
f = open('text.txt', 'w+')
f.write("hello Python")
print(f.read())
f.close()
# 2.5 文件定位操作
# tell()和seek()
# tell(): 显示文件内当前位置，即文件指针当前位置
# seek(offset, whence): 移动文件读取指针到指定位置
# offset : 偏移量，表示要移动的字节数
# whence ： 起始位置，移动字节的参考位置，默认是0，
# 0 代表开头作为参考位置，1 代表当前位置作为参考位置，2 代表文件结尾代表参考位置
# seek(0,0) 会把文件指针移动到开头位置
f = open('test.txt', 'w+')
f.write("hello python!")
pos = f.tell()
print("当前文件指针所在的位置：", pos)
f.seek(0, 0)
pos2 = f.tell()
print("移动后所在位置：", pos2)
print(f.read())

f.close()

# 3.1 with open
# 作用：代码执行完，系统会自动调用f.close()，可以省略关闭步骤
with open("test.txt", "w") as f:    # f是文件对象
    f.write("emmmm....")
    print(f.closed)
print(f.closed)

# 编码格式
# with open("test.txt", "w", encoding = "utf-8") as f:
#     f.write("冰冰18岁")

# 案例：图片复制  ‘rb’
"""
1. 读取图片
图片是一个二进制文件，想要写入，必须先拿到
2. 写入图片
"""
with open(r"C:\Users\Admin\Desktop\新建文件夹\liuhua101.jpg", 'rb') as file:
    img = file.read()
    print(img)
# 读取到的内容，写入到当前文件中
with open(r"E:\PyProject\py01\图片.jpg", "wb") as f:
    f.write(img)

# 4. 目录常见操作
# 导入模块
import os
# 1. 文件的重命名 os.rename(旧名字，新名字)
# os.rename('test.txt', "bingbing.txt")
# 2. 删除文件
# os.remove("图片.jpg")
# 3. 创建文件夹  os.mkdir()
os.mkdir("bingbing")
# 4. 删除文件夹 os.rmdir()
# os.rmdir("bingbing")
# 5. 获取当前目录 os.getcwd()
# print(os.getcwd())
# 6. 获取目录列表
# print(os.listdir())       # 获取当前目录列表
# print(os.listdir("../"))    # 获取上一级目录列表