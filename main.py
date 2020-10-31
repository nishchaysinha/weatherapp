import pymysql
import time

connection=pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='weather')

with connection.cursor() as cursor:
    base-cmd='INSERT INTO TABLE weather VALUES '
    cursor.execute(base-cmd + "()")