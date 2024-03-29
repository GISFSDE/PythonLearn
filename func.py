'''
函数
'''


# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
#
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号 : 起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
def max(a, b):
    if a > b:
        return a
    else:
        return b


# python 函数的参数传递：
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
# 可通过id()函数查看对象内存地址

# 参数
# 以下是调用函数时可使用的正式参数类型：
# 必需参数【调用时的数量必须和声明时的一样】 def printme( str ):
# 关键字参数【允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值】def printinfo( name, age ):
# 默认参数【如果没有传递参数，则会使用默认参数】def printinfo( name, age = 35 ):
# 不定长参数 【加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数，没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量，加了两个星号 ** 的参数会以字典的形式导入，如果单独出现星号 * 后的参数必须用关键字传入】def functionname([formal_args,] *var_args_tuple ):

'''
匿名函数
'''
# lambda [arg1 [,arg2,.....argn]]:expression
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
'''
强制位置参数
'''


# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# 以下使用方法是正确的:

f(10, 20, 30, d=40, e=50, f=60)
# 以下使用方法会发生错误:

f(10, b=20, c=30, d=40, e=50, f=60)  # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)  # e 必须使用关键字参数的形式
