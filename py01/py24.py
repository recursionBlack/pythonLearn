import re
# 1. 匹配分组
# 1. |: 匹配左右任意一个表达式         --- 常用
# res = re.match("abc|def", "abc")
# print(res.group())
# 2. (ab):将括号中字符作为一个分组     --- 常用
# res = re.match("\w*@(163|qq|126).com", "abc@163.com")
# print(res.group())
# 3. \num: 匹配分组num匹配到的字符串   --- 经常在匹配标签时被使用
# res = re.match("<(\w*)>\w*</\\1>", "<html>login</html>")
# res = re.match("<(\w*)><(\w*)>\w*</\\2></\\1>", "<html><body>login</body></html>")
# print(res.group())
# 注意：从外到内排序，编号从1开始
# 4. (?P<name>)：分组起别名
# 5. (?P=name)： 引用别名为name分组匹配到的字符串
# res = re.match("<(?P<L1>\w*)><(?P<L2>\w*)>\w*</(?P=L2)></(?P=L1)>", "<html><body>login</body></html>")
# print(res.group())

# 匹配网址：前缀一般是www,后缀：.com、.cn
# li = ["www.baidu.com", "www.python.org", "http.jd.cn","www.py.en", "www.abc.cn"]
# res = re.match("www\.\w*\.(com|cn|org)","www.baidu.com")
# print(res.group())
# for i in li:
#     res = re.match("www\.\w*\.(com|cn|org)", i)
#     if res:
#         print(res.group())
#     else:
#         print(f"{i}这个网址有错误")

# 2. 高级用法
# 1.search(): 扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败，就返回None
# res = re.search("th", 'pythonth')
# print(res.group())
# 2.findall(): 从头到尾匹配，找到所有匹配成功的数据，并返回一个列表
# res = re.findall("th", 'pythonth')
# print(res)

# 总结：
# match()：从头开始匹配，匹配成功返回match对象，通过groups对象进行提取，匹配失败返回None
# search(): 从头开始匹配，匹配成功返回第一个成功匹配的对象，通过groups对象进行提取
# findall(): 从头到尾匹配，匹配成功返回一个列表，匹配所有成功的数据，不需要通过groups提取

# 3.sub(pattern, repl, string, count)
# pattern: 正则表达式（代表需要被替换的，也就是字符串里面的内容）
# repl: 新内容
# string： 字符串
# count: 指定替换的次数
# res = re.sub("ptyhon", "bingbing", "hellopython")
# print(res)
# 4. split(pattern, string, maxsplit)
# pattern: 正则表达式（代表需要被分割的，
# string： 字符串
# maxsplit：最大分割次数
# res = re.split(",", "hello,python, 123, hahah")     # 没有设置次数，就默认全部分割
# print(res)

# 3.贪婪与非贪婪
# 1.贪婪匹配（默认）：在满足匹配时，匹配尽可能长的字符串
# res = re.match("em*", "emmmmmm.....")
# print(res.group())

# 2.非贪婪匹配：在满足匹配时，匹配尽可能短的字符串，使用？来表示非贪婪匹配
# res = re.match("em*?", "emmmmmm.....")
# print(res.group())

# res = re.match("m{2,5}?", "mmmmmm.....")
# print(res.group())

# 4. 原生字符串
print(r"sixs\tar")      # r取消转义
res = re.match(r"\\\\", r"\\\name")
print(res.group())
# 正则表达式中，匹配字符串中的字符\需要\\\\,加入原生字符串，\\代表\
