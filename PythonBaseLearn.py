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
# 保留字
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

# Number（数字）-------------------------------------

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

# String（字符串）-------------------------------------------

# 从后面索引01234567
# 从前面索引-8-7-6-5-4-3-2-1
#         Good boy
# 从前面截取:123456:
# 从后面截取:-6-5-4-3-2-1:
# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行
# 用+运算符连接在一起，用*运算符重复
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

# List（列表）-------------------------------------------
# 列表中的元素是可以改变的
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

# Tuple（元组）---------------------------------
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改，但它可以包含可变的对象。元组写在小括号 () 里，元素之间用逗号隔开。
# string、list 和 tuple 都属于 sequence（序列）。
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# Set（集合）-----------------------------------
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
sites1 = {}
sites2 = ()
set()

print(sites)  # 输出集合，重复的元素被自动去掉

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

# Dictionary（字典）-------------------------------
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
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


