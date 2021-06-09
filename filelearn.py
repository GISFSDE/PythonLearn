"""
文件
"""
# 打开文件返回文件对象
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# mode 参数有：
# 模式	描述
# t	文本模式 (默认)。
# x	写模式，新建一个文件，如果该文件已存在则会报错。
# b	二进制模式。
# +	打开一个文件进行更新(可读可写)。
# U	通用换行模式（Python 3 不支持）。
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
file = open('filetest.txt', mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#  file 对象常用的函数：
# file.close() 关闭文件。关闭后文件不能再进行读写操作。
# file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty() 如果文件连接到一个终端设备返回 True，否则返回 False。
# file.next() Python 3 中的 File 对象不支持 next() 方法。 返回文件下一行。
# file.read([size]) 从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readline([size]) 读取整行，包括 "\n" 字符。
# file.readlines([sizeint]) 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
# file.seek(offset[, whence]) 移动文件读取指针到指定位置
# file.tell() 返回文件当前位置。
# file.truncate([size]) 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
# file.write(str) 将字符串写入文件，返回的是写入的字符长度。
# file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

"""
文件和目录
"""
# os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
#
# 序号	方法及描述
# os.access(path, mode) 检验权限模式
# os.chdir(path) 改变当前工作目录
# os.chflags(path, flags) 设置路径的标记为数字标记。
# os.chmod(path, mode) 更改权限
# os.chown(path, uid, gid) 更改文件所有者
# os.chroot(path) 改变当前进程的根目录
# os.close(fd) 关闭文件描述符 fd
# os.closerange(fd_low, fd_high) 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
# os.dup(fd) 复制文件描述符 fd
# os.dup2(fd, fd2) 将一个文件描述符 fd 复制到另一个 fd2
# os.fchdir(fd) 通过文件描述符改变当前工作目录
# os.fchmod(fd, mode) 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
# os.fchown(fd, uid, gid) 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
# os.fdatasync(fd) 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
# os.fdopen(fd[, mode[, bufsize]]) 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
# os.fpathconf(fd, name) 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
# os.fstat(fd) 返回文件描述符fd的状态，像stat()。
# os.fstatvfs(fd) 返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。
# os.fsync(fd)  强制将文件描述符为fd的文件写入硬盘。
# os.ftruncate(fd, length) 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
# os.getcwd() 返回当前工作目录
# os.getcwdb() 返回一个当前工作目录的Unicode对象
# os.isatty(fd) 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
# os.lchflags(path, flags) 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
# os.lchmod(path, mode) 修改连接文件权限
# os.lchown(path, uid, gid) 更改文件所有者，类似 chown，但是不追踪链接。
# os.link(src, dst) 创建硬链接，名为参数 dst，指向参数 src
# os.listdir(path) 返回path指定的文件夹包含的文件或文件夹的名字的列表。
# os.lseek(fd, pos, how) 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
# os.lstat(path) 像stat(),但是没有软链接
# os.major(device) 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
# os.makedev(major, minor) 以major和minor设备号组成一个原始设备号
# os.makedirs(path[, mode]) 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
# os.minor(device) 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
# os.mkdir(path[, mode]) 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
# os.mkfifo(path[, mode]) 创建命名管道，mode 为数字，默认为 0666 (八进制)
# os.mknod(filename[, mode=0600, device]) 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
# os.open(file, flags[, mode]) 打开一个文件，并且设置需要的打开选项，mode参数是可选的
# os.openpty() 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
# os.pathconf(path, name) 返回相关文件的系统配置信息。
# os.pipe() 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
# os.popen(command[, mode[, bufsize]]) 从一个 command 打开一个管道
# os.read(fd, n) 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
# os.readlink(path) 返回软链接所指向的文件
# os.remove(path) 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
# os.removedirs(path) 递归删除目录。
# os.rename(src, dst) 重命名文件或目录，从 src 到 dst
# os.renames(old, new) 递归地对目录进行更名，也可以对文件进行更名。
# os.rmdir(path) 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
# os.stat(path) 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
# os.stat_float_times([newvalue]) 决定stat_result是否以float对象显示时间戳
# os.statvfs(path) 获取指定路径的文件系统统计信息
# os.symlink(src, dst) 创建一个软链接
# os.tcgetpgrp(fd) 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
# os.tcsetpgrp(fd, pg) 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
# os.tempnam([dir[, prefix]]) Python3 中已删除。返回唯一的路径名用于创建临时文件。
# os.tmpfile() Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
# os.tmpnam() Python3 中已删除。为创建一个临时文件返回一个唯一的路径
# os.ttyname(fd) 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
# os.unlink(path) 删除文件路径
# os.utime(path, times) 返回指定的path文件的访问和修改的时间。
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) 输出在文件夹中的文件名通过在树中游走，向上或者向下。
# os.write(fd, str) 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
# os.path 模块 获取文件的属性信息。
# os.pardir() 获取当前目录的父目录，以字符串形式显示目录名。
