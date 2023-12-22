import pymysql

conn = pymysql.Connect(
        user="root",
        password="Test1234",
        host="192.168.220.128",
        port=3306,
        database="test_navicat")

cursor = conn.cursor()

try:
    # 方法1：写死插入的数据
    # sql_add = "insert into person_info values(0, 'Python_Sam', 20,'男', 'LA', '1993-07-25 11:04:01'), " \
    #           "(10, 'Python_Tom', 20,'男', 'LA', '1993-07-25 11:04:01');"
    # 方法2：插入数据写入列表
    sql_add = "insert into person_info values(%s, %s, %s, %s, %s, %s)"
    add_data1 = [0, 'Python_Sam', 20, '男', 'LA', '1993-07-25 11:04:01']
    add_data2 = [10, 'Python_Tom', 20, '男', 'LA', '1993-07-25 11:04:01']
    # update和delete也可以用方法2
    sql_update = "update person_info set name='Python_Tom1' where name='Python_Tom';"
    sql_delete = "delete from person_info where name='Python_Tom1';"

    cursor.execute(sql_add, add_data1)
    cursor.execute(sql_add, add_data2)
    cursor.execute(sql_update)
    cursor.execute(sql_delete)

    # 提交操作!!!
    conn.commit()
except Exception as e:
    print(e)
    # 如果操作失败，回滚操作！！
    conn.rollback()
finally:
    cursor.close()
    conn.close()