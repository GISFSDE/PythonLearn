"""
JSON
"""
# json.dumps(): ==编码==
# dict	                                     object
# list, tuple	                             array
# str	                                     string
# int, float, int- & float-derived Enums	 number
# True	                                     true
# False	                                     false
# None	                                      null
# json.loads(): ==解码==
# object	    dict
# array     	list
# string	    str
# number (int)	int
# number (real)	float
# true	        True
# false	        False
# null	        None
import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 文件处理
# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)