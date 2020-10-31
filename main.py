import pymysql
import time
import requests
import json

connection=pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='weather')

with connection.cursor() as cursor:
    defcmd='INSERT INTO TABLE weather VALUES '
    cursor.execute(defcmd + "()")
    