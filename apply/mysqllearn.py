import mysql.connector

# python -m pip install mysql-connector 安装连接驱动
# python -m pip install mysql-connector-python
# pip uninstall mysql-connector 卸载
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root"  # 数据库密码
    # auth_plugin='mysql_native_password'
    # database="runoob_db" #有则直接连接数据库
)

print(mydb)

# 创建数据库
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE runoob_db")
# 输出所有数据库列表
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# 创建表
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# mycursor.execute(sql语句)


# 增
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")

# 批量增
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]
mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功, ID:", mycursor.lastrowid)

# 查
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
myresult = mycursor.fetchone()  #获取一条
for x in myresult:
    print(x)

# 防sql注入
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)
mycursor.execute(sql, na)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#删
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")

# 改
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")