import re
# 1. 正则表达式
# 字符串处理工具
# 注意：需要导入re模块
# 1.2 特点：
#   语法比较复杂，可读性较差
#   通用性强，适用于多种语言
# 1.3 步骤：
#   1.导入re模块
#   2.使用match方法进行匹配操作
#       re.match()能匹配褚以xxx开头的字符串
#       如果起始位置没有匹配成功，返回None
# re.match(pattern, string,flags)
# pattern 匹配的正则表达式
# string 要匹配的字符串
# res = re.match("冰", "冰冰永远18岁")
# print(res)
#   3.如果上一步数据匹配成功，使用group()提取数据
# print(res.group())
# 注意：match是从开始位置匹配，匹配不到就没有，且匹配的是表达式整理

# 2. 匹配单个字符
# 1. .:匹配任意一个字符，\n除外       -- 常用
# res = re.match('.','hello')
# print(res.group())
# 2. []:匹配[]中列举的字符          -- 常用
# res = re.match('[he]','hello')
# res = re.match('[1234]','5423')
# print(res.group())
# 3. \d: 匹配数字0-9             -- 常用
# res = re.match('\d', '7234')
# print(res.group())
# 4. \D: 匹配非数字              -- 常用
# res = re.match('\D', 's3er24')      # 只要不是数字，都能匹配
# print(res.group())
# 5. \s: 匹配空白，即空格和tab键
# res = re.match('\s', '  s3er24')
# print(res.group())      # \s\s = 一个tab
# 6. \S: 匹配非空白
# res = re.match('\S', 's3er24')
# print(res.group())
# 7. \w: 匹配单词字符，即a-z,A-A,0-9,_，汉字  -- 常用
# res = re.match('\w', 'Bingbing')
# print(res.group())
# 8. \W: 匹配非单词字符
# res = re.match('\W', '=Bingbing')
# print(res.group())

# 3. 匹配多个字符
# 1. * ：匹配前一个字符出现0次或无限次，即可有可无  -- 常用
# 2. + ：匹配前一个字符出现至少有1次或无限次        -- 常用
# 3. ？：匹配前一个字符出现1次或0次                -- 常用
# 4. {m}：匹配前一个字符出现m次
# 5. {m,n}: 匹配前一个字符出现从m次到n次

# 4. 匹配开头和结尾
# 1. ^: 表示以...开头;  或表示对...取反
# res = re.match('^py', 'python')
# print(res.group())
# 注意：^在[]中表示不匹配, 取反
# res = re.match('[^py]', 'python')       # [^py]表示匹配除了py之外的字符
# print(res.group())
# 2. $: 匹配以...字符串结尾
# res = re.match('.{3}g$', 'bing')
# print(res.group())

