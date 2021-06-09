"""
语法错误和异常
"""
# 语法错误 SyntaxError
# 异常  ZeroDivisionError，NameError 和 TypeError
# 异常处理
# ---try/except---
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
# except (RuntimeError, TypeError, NameError):
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
# ----try/except...else---else 子句将在 try 子句没有发生任何异常的时候执行
# ---try-finally----
# 抛出异常 raise [Exception [, args [, traceback]]]
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
# 用户自定义异常 通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
# with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")