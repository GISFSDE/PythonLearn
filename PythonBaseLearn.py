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
基本数据类型 
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
a = b = c = counter = 100  # 同时为多个变量赋值整型变量
d, e, f = 1, 2, "runoob"  # 同时为多个变量赋值不同的值
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串
