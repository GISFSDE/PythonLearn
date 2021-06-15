"""
网络编程
"""

# 低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统 Socket 接口的全部方法。
# 高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

# socket()
# socket.socket([family[, type[, proto]]])
# family: 套接字家族可以使 AF_UNIX 或者 AF_INET。
# type:套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM。
# protocol: 一般不填默认为 0。
# Socket 对象(内建)方法


# 函数	                         描述
# 服务器端套接字-----------
# s.bind()	    绑定地址（host,port）到套接字， 在 AF_INET下，以元组（host,port）的形式表示地址。
# s.listen()	开始 TCP 监听。backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为 1，大部分应用程序设为 5 就可以了。
# s.accept()	被动接受TCP客户端连接,(阻塞式)等待连接的到来
# 客户端套接字-----------
# s.connect()	    主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
# s.connect_ex()	connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
# 公共用途的套接字函数----------
# s.recv()	接收 TCP 数据，数据以字符串形式返回，bufsize 指定要接收的最大数据量。flag 提供有关消息的其他信息，通常可以忽略。
# s.send()	发送 TCP 数据，将 string 中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于 string 的字节大小。
# s.sendall()	完整发送 TCP 数据。将 string 中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回 None，失败则抛出异常。
# s.recvfrom()	接收 UDP 数据，与 recv() 类似，但返回值是（data,address）。其中 data 是包含接收数据的字符串，address 是发送数据的套接字地址。
# s.sendto()	发送 UDP 数据，将数据发送到套接字，address 是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
# s.close()	关闭套接字
# s.getpeername()	返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
# s.getsockname()	返回套接字自己的地址。通常是一个元组(ipaddr,port)
# s.setsockopt(level,optname,value)	设置给定套接字选项的值。
# s.getsockopt(level,optname[.buflen])	返回套接字选项的值。
# s.settimeout(timeout)	设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
# s.gettimeout()	返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
# s.fileno()	返回套接字的文件描述符。
# s.setblocking(flag)	如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
# s.makefile()	创建一个与该套接字相关连的文件