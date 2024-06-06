import  pymysql

#1创建一个 链接对象:决定了要去访问链接哪一个数据库服务器下的哪一个数据仓库
conn = pymysql.connect(
    host='127.0.0.1',#数据库的ip地址
    port=3306,#mysql 端口
    user='root',
    password='boboadmin',
    db = 'new_spider', #数据库的名字
    charset='utf8'#中文编码
)

#2 创建一个油表对象：可以让python 直行sql语句
cursor = conn.cursor()

#3使用游标对象执行sql语句
#sql = 'delet from new_dep where id = 5'#删除
#sql = 'insert into new_dep values (66,"haha","xxx")'#增加

#查询
sql = 'select * from new_dep where id =66'
cursor.execute(sql)
ret = cursor.fetchall() #查询所有记录
ret  = cursor.fetchone() #查询返回第一条记录

#4提交事务:让游标执行的sql语句完全的映射到数据库中
conn.commit()

#5关闭资源:
cursor.close()
conn.close()


