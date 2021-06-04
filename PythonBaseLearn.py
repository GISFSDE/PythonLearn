'''
=============基本语法=============
'''
import keyword

# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
print("Hello word!")

''' 
注释 
'''
"""
注释
注释
"""
# 保留字  关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符print(b, end=',')
print("保留字", keyword.kwlist)

# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
if True:
    print("ture")
else:
    print('false')

# 多行语句，语句很长，我们可以使用反斜杠(\)来实现多行语句，在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
total = 'item_one' + \
        'item_two' + \
        'item_three'
total1 = ['item_one', 'item_two', 'item_three',
          'item_four', 'item_five']
print(total)
print(total1)

''' 
================基本数据类型===================
Python3 中有六个标准的数据类型：
Number（数字）：int、float、bool、complex（复数）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
 type()查看数据类型，isinstance(a, int)进行判断
'''

# Number（数字）------------------------------------------------------------------------
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
# ==数学函数==
# 函数	    返回值 ( 描述 )
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y) 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
# sqrt(x)	返回数字x的平方根。
# ==随机数函数==
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random()	随机生成下一个实数，它在[0,1)范围内。
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内
# ==三角函数==
# Python包括以下三角函数：
# 函数	        描述
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度
# ==数学常量==
# 常量	描述
# pi	数学常量 pi（圆周率，一般以π来表示）
# e	    数学常量 e，e即自然常数（自然常数）。
a = b = c = counter = 100  # 同时为多个变量赋值整型变量
d, e, f = 1, 2, "runoob"  # 同时为多个变量赋值不同的值
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

# del语句删除一些对象引用
del a

# 数值运算

Division = 2 / 4  # 除法，得到一个浮点数
Division2 = 2 // 4  # 除法，得到一个整数
remainder = 17 % 3  # 取余
involution = 2 ** 5  # 乘方
print(Division, 'Division')
print(Division2, 'Division2')

# String（字符串）------------------------------------------------------------------------------

# 从后面索引01234567
# 从前面索引-8-7-6-5-4-3-2-1
#         Good boy
# 从前面截取:123456:
# 从后面截取:-6-5-4-3-2-1:
# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行
# 用+运算符连接在一起，用*运算符重复

# ==转义字符==
# \(在行尾时)	续行符
# >>> print("line1 \
# ... line2 \
# ... line3")
# line1 line2 line3
# \\	反斜杠符号
# >>> print("\\")
# \
# \'	单引号
# >>> print('\'')
# '
# \"	双引号
# >>> print("\"")
# "
# \a	响铃
# >>> print("\a")执行后电脑有响声。
# \b	退格(Backspace)
# >>> print("Hello \b World!")
# Hello World!
# \000	空
# >>> print("\000")
#
# >>>
# \n	换行
# >>> print("\n")
#
# >>>
# \v	纵向制表符
# >>> print("Hello \v World!")
# Hello
#        World!
# >>>
# \t	横向制表符
# >>> print("Hello \t World!")
# Hello      World!
# >>>
# \r	回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
# >>> print("Hello\rWorld!")
# World!
# >>> print('google runoob taobao\r123456')
# 123456 runoob taobao
# \f	换页
# >>> print("Hello \f World!")
# Hello
#        World!
# >>>
# \yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
# >>> print("\110\145\154\154\157\40\127\157\162\154\144\41")
# Hello World!
# \xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
# >>> print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
# Hello World!
# \other	其它的字符以普通格式输出
# ==字符串运算符==
# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。  print( r'\n' ) print( R'\n' )
# %	格式字符串
# ==字符串格式化==
# % c 格式化字符及其ASCII码
# % s 格式化字符串
# % d 格式化整数
# % u 格式化无符号整型
# % o 格式化无符号八进制数
# % x 格式化无符号十六进制数
# % X 格式化无符号十六进制数（大写）
# % f 格式化浮点数字，可指定小数点后的精度
# % e 用科学计数法格式化浮点数
# % E 作用同 % e，用科学计数法格式化浮点数
# % g % f和 % e的简写
# % G % f 和 % E 的简写
# % p 用十六进制数格式化变量的地址
# 格式化操作符辅助指令:
# 符号	功能
# *	定义宽度或者小数点精度
# -	用做左对齐
# +	在正数前面显示加号( + )
# <sp>	在正数前面显示空格
# #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	显示的数字前面填充'0'而不是默认的空格
# %	'%%'输出一个单一的'%'
# (var)	映射变量(字典参数)
# m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

# ==f-string==
name = 'Runoob'
f'Hello {name}'  # 替换变量
'Hello Runoob'
f'{1 + 2}'  # 使用表达式
'3'

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
# ==字符串内建函数==

# capitalize()
# 将字符串的第一个字符转换为大写

# center(width, fillchar)
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

# count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

# bytes.decode(encoding="utf-8", errors="strict")
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

# encode(encoding='UTF-8',errors='strict')
# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

# expandtabs(tabsize=8)
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

# find(str, beg=0, end=len(string))
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

# index(str, beg=0, end=len(string))
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常。

# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False

# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False

# isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False..

# islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

# isnumeric()
# 如果字符串中只包含数字字符，则返回 True，否则返回 False

# isspace()
# 如果字符串中只包含空白，则返回 True，否则返回 False.

# istitle()
# 如果字符串是标题化的(见 title())则返回 True，否则返回 False

# isupper()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

# join(seq)
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

# len(string)
# 返回字符串长度

# ljust(width[, fillchar])
# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

# lower()
# 转换字符串中所有大写字符为小写.

# lstrip()
# 截掉字符串左边的空格或指定字符。

# maketrans()
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

# max(str)
# 返回字符串 str 中最大的字母。

# min(str)
# 返回字符串 str 中最小的字母。

# replace(old, new [, max])
# 把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。

# rfind(str, beg=0,end=len(string))
# 类似于 find()函数，不过是从右边开始查找.

# rindex( str, beg=0, end=len(string))
# 类似于 index()，不过是从右边开始.

# rjust(width,[, fillchar])
# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

# rstrip()
# 删除字符串末尾的空格或指定字符。

# split(str="", num=string.count(str))
# 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串

# splitlines([keepends])
# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

# startswith(substr, beg=0,end=len(string))
# 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

# strip([chars])
# 在字符串上执行 lstrip()和 rstrip()

# swapcase()
#  将字符串中大写转换为小写，小写转换为大写

# title()
# 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

# translate(table, deletechars="")
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

# upper()
# 转换字符串中的小写字母为大写

# zfill (width)
# 返回长度为 width 的字符串，原字符串右对齐，前面填充0

# isdecimal()
# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
str = 'Lxl is a good boy'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TEST")  # 连接字符串
# 转义
print('Ru\noob')
# 不转义字符串前加r
print(2 * r'Ru\noob')


# List（列表）------------------------------------------------------------------------------
# 创建列表只需要方括号括起来，里面数据类型可不一致，索引正0反-1，
# 列表中的元素是可以改变的
# append() 追加  del 删除
# ==列表脚本操作符==
# Python 表达式	                              结果	             描述
# len([1, 2, 3])	                        3	                 长度
# [1, 2, 3] + [4, 5, 6]	                    [1, 2, 3, 4, 5, 6]	    组合
# ['Hi!'] * 4	                             ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	                        True	        元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")	    1 2 3	迭代
# ==函数&方法==
# len(list) 列表元素个数
# max(list) 返回列表元素最大值
# min(list) 返回列表元素最小值
# list(seq) 将元组转换为列表
# 1	list.append(obj) 在列表末尾添加新的对象
# 2	list.count(obj) 统计某个元素在列表中出现的次数
# 3	list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj) 将对象插入列表
# 6	list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj) 移除列表中某个值的第一个匹配项
# 8	list.reverse() 反向列表中元素
# 9	list.sort( key=None, reverse=False) 对原列表进行排序
# 10 list.clear() 清空列表
# 11 list.copy() 复制列表
lists = ['1', '2', '3', '4', '5']
print(lists[:])
print(lists[:3])
print(lists[1:3])
print(lists[4:])
print(lists[-1:])
print(lists[:-2])
print(lists * 3)  # 输出多次列表
print(lists + lists)  # 连接列表


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

# Tuple（元组）--------------------------------------------------------------------
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改，其使用小括号（）或不要括号，
# 但它可以包含可变的对象，可以连接组合成新元祖，元素不允许删除但可以使用del删除整个元祖。
# string、list 和 tuple 都属于 sequence（序列）。
# 当元祖只有一个元素时，后面添加逗号，否则括号会被当做运算符使用，tup1 = (50)为整型，tup1 = (50，)为元祖
# ==元祖运算符==
# Python 表达式	        结果	                     描述
# len((1, 2, 3))	        3	                 计算元素个数
# (1, 2, 3) + (4, 5, 6)	    (1, 2, 3, 4, 5, 6)	    连接
# ('Hi!',) * 4  	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	        True	            元素是否存在
# for x in (1, 2, 3): print (x,)	1 2 3	        迭代
# ==内置函数==
# len(tuple) 计算元组元素个数。
# max(tuple) 返回元组中元素最大值。
# min(tuple) 返回元组中元素最小值。
# tuple(iterable) 将可迭代系列转换为元组。
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# Set（集合）----------------------------------------------------------------------
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
sites1 = {}
sites2 = ()
set()
# # 添加元素，重复不操作
# sites1.add("1")
# # 可以添加列表，元祖字典等
# sites1.update("1")
# print(sites)  # 输出集合，重复的元素被自动去掉
# # 移除，不存在报错
# sites1.remove( x )
# # 移除，不存在不报错
# sites1.discard( x )
# # 随机删除
# sites1.pop()
# # 长度
# len(sites1)
# # 清空
# sites1.clear()
# # 判断是否存在
# x in s
# ==内置方法完整列表==
# add()	为集合添加元素
# clear()	移除集合中的所有元素
# copy()	拷贝一个集合
# difference()	返回多个集合的差集
# difference_update()	移除集合中的元素，该元素在指定的集合也存在。
# discard()	删除集合中指定的元素
# intersection()	返回集合的交集
# intersection_update()	返回集合的交集。
# isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# issubset()	判断指定集合是否为该方法参数集合的子集。
# issuperset()	判断该方法的参数集合是否为指定集合的子集
# pop()	随机移除元素
# remove()	移除指定元素
# symmetric_difference()	返回两个集合中不重复的元素集合。
# symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# union()	返回两个集合的并集
# update()	给集合添加元素

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

# Dictionary（字典）------------------------------------------------------------------
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)可以是任意类型，但必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
# ==内置函数==
# len(dict) 计算字典元素个数，即键的总数。
# str(dict) 输出字典，以可打印的字符串表示。
# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。
# ==内置方法==
# 1	radiansdict.clear() 删除字典内所有元素
# 2	radiansdict.copy()  返回一个字典的浅复制
# 3	radiansdict.fromkeys()  创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 4	radiansdict.get(key, default=None)  返回指定键的值，如果键不在字典中返回 default 设置的默认值
# 5	key in dict 如果键在字典dict里返回true，否则返回false
# 6	radiansdict.items() 以列表返回一个视图对象
# 7	radiansdict.keys() 返回一个视图对象
# 8	radiansdict.setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9	radiansdict.update(dict2) 把字典dict2的键/值对更新到dict里
# 10 radiansdict.values() 返回一个视图对象
# 11 pop(key[,default])  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# 12 popitem()  随机返回并删除字典中的最后一对键和值
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
del tinydict['name'] # 删除键 'name'
dict.clear()     # 清空字典
del tinydict         # 删除字典
# 构造函数 dict() 可以直接从键值对序列中构建字典如下


'''
============数据类型转换===============
'''
# int(x [,base]) 将x转换为一个整数
# float(x)将x转换到一个浮点数
# complex(real [,imag])创建一个复数
# str(x)将对象 x 转换为字符串
# repr(x)将对象 x 转换为表达式字符串
# eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)将序列 s 转换为一个元组
# list(s)将序列 s 转换为一个列表
# set(s)转换为可变集合
# dict(d)创建一个字典。d 必须是一个 (key, value)元组序列。
# frozenset(s)转换为不可变集合
# chr(x)将一个整数转换为一个字符
# ord(x)将一个字符转换为它的整数值
# hex(x)将一个整数转换为一个十六进制字符串
# oct(x)将一个整数转换为一个八进制字符串

'''
============Python3运算符===============
'''
# 算术运算符【a为10，b为21】----------------------------------
# +	加 - 两个对象相加	                        a + b 输出结果 31
# -	减 - 得到负数或是一个数减去另一个数	        a - b 输出结果 -11
# *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
# /	除 - x 除以 y	                        b / a 输出结果 2.1
# %	取模 - 返回除法的余数	                    b % a 输出结果 1
# **	幂 - 返回x的y次幂	                    a**b 为10的21次方
# //	取整除 - 向下取接近商的整数，除后取小      9//2=4   -9//2=-5

# 比较（关系）运算符【a为10，b为20】-----------------------------
# ==	等于 - 比较对象是否相等	        (a == b) 返回 False。
# !=	不等于 - 比较两个对象是否不相等	(a != b) 返回 True。
# >	    大于 - 返回x是否大于y	        (a > b) 返回 False。
# <	    小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
# >=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
# <=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。

# 赋值运算符【a为10，b为20】----------------------------------
# =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
# +=	加法赋值运算符	c += a 等效于 c = c + a
# -=	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a
# :=    海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
# 在这个示例中，赋值表达式可以避免调用 len() 两次:
# if (n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expected <= 10)")

# 逻辑运算符-----------------------------------------------------
# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

# 位运算符-------------------------------------------------------
# &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
# |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
# ^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
# ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
# <<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111

# 成员运算符----------------------------------------------------------
# in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

# 身份运算符------------------------------------------------------------
# is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

# 运算符优先级
# **	指数 (最高优先级)
# ~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //	乘，除，求余数和取整除
# + -	加法减法
# >> <<	右移，左移运算符
# &	位 'AND'
# ^ |	位运算符
# <= < > >=	比较运算符
# == !=	等于运算符
# = %= /= //= -= += *= **=	赋值运算符
# is is not	身份运算符
# in not in	成员运算符
# not and or	逻辑运算符
