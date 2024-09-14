# 1.导包
import pymysql
try:
    # 2.创建数据库连接
    conn = pymysql.Connect(
        user="root",
        password="Test1234",
        host="192.168.220.128",
        port=3306,
        database="test_navicat")
    # 3.创建游标对象
    cursor = conn.cursor()
    # 4.编写sql语句
    sql = "select * from person_info;"
    # 5.使用游标对象调用sql语句
    cursor.execute(sql)
    # 6.获取查询结果
    result = cursor.fetchall()
    print(result)
    # 7.关闭资源
    cursor.close()
    conn.close()
except Exception as e:
    raise e
