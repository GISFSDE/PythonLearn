"""
urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。
"""
# urllib.request - 打开和读取 URL。
# urllib.error - 包含 urllib.request 抛出的异常。
# urllib.parse - 解析 URL。
# urllib.robotparser - 解析 robots.txt 文件

# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# url：url 地址。
# data：发送到服务器的其他数据对象，默认为 None。
# timeout：设置访问超时时间。
# cafile 和 capath：cafile 为 CA 证书， capath 为 CA 证书的路径，使用 HTTPS 需要用到。
# cadefault：已经被弃用。
# context：ssl.SSLContext类型，用来指定 SSL 设置。

from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
print(myURL.read())
print(myURL.read(600))
print(myURL.readline())
lines = myURL.readlines()
for line in lines:
    print(line)
print(myURL.getcode())

f = open("runoob_urllib_test.html", "wb")
content = myURL.read()  # 读取网页内容
f.write(content)
f.close()

import urllib.request

encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
print(encode_url)

unencode_url = urllib.request.unquote(encode_url)    # 解码
print(unencode_url)


# 模拟头部信息
# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# url：url 地址。
# data：发送到服务器的其他数据对象，默认为 None。
# headers：HTTP 请求的头部信息，字典格式。
# origin_req_host：请求的主机地址，IP 或域名。
# unverifiable：很少用整个参数，用于设置网页是否需要验证，默认是False。。
# method：请求方法， 如 GET、POST、DELETE、PUT等。
import urllib.parse

url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
keyword = 'Python 教程'
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url+key_code
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request = urllib.request.Request(url_all,headers=header)
reponse = urllib.request.urlopen(request).read()

fh = open("./urllib_test_runoob_search.html","wb")    # 将文件写入到当前目录中
fh.write(reponse)
fh.close()