'''
import mysql.connector as sql
import time as t

sql = sql.connect(host = "localhost",user = "root", password = "")
cursor = sql.cursor()
cursor.execute('use cs_project_ns_ys_ma_2020_sqlDB')
#loop for continually giving suggestions ;)
def autocompletepoopoo():
    i=""
    while i!='!':
        i+=str(input("Search fuckface:  "))
        print(cursor.execute('SeLeCt * FrOm PLACES WhErE name like '+'"'+i+'%";'))


autocompletepoopoo()
'''
