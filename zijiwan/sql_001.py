# -*- coding: utf-8 -*-

import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
        host = '120.26.90.177',
        port = 3306,
        user = 'test_admin',
        passwd = 'bdwork.com!@#',
        db = 'bdwork_test',
        charset = 'utf8'
)
# 获取游标
cursor = connect.cursor()

# 查询数据
sql = "SELECT * from bdwork_test.T_LOT_FOOT_MATCH_RESULT"
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
print('共查找出', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
connect.close()