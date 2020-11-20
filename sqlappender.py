import mysql.connector as mscon

regular_alphabet = "abcdefghijklmnopqrstuvwxyz -"
DATABASE_NAME_NEVER_CHANGE = "cs_project_ns_ys_ma_2020_sqlDB"
SQL_TABLENAME_NEVER_CHANGE = {"places" : "PLACES","searches" : "SEARCHES", "saved" : "SAVED"}

class save:

    def __createDB(self):
        self.sql_cursor.execute("CREATE DATABASE IF NOT EXISTS "+DATABASE_NAME_NEVER_CHANGE)
    
    def __addAllPlacesToPLACES(self):
        cities = []
        with open(MAJOR_CITIES_FILENAME_NEVER_CHANGE, encoding = 'utf-8') as file:
            reader = csv.reader(file)
            firstRow = True
            cityTuple = ("first_nothing_no_city",)
            for row in reader:
                if(firstRow == True):
                    firstRow = False
                else:
                    cityTuple = (row[0].lower(),)
                    should_not_add = False
                    for char in cityTuple[0]:
                        if(char not in regular_alphabet):
                            should_not_add = True
                            break
                    if(should_not_add == True or cityTuple in cities):
                        continue
                    cities.append(cityTuple)
        
        self.sql_cursor.executemany("INSERT INTO PLACES(name) VALUES (%s)",cities)
        self.sql.commit()

    def __initializeAllTables(self):
        self.sql_cursor.execute("CREATE TABLE " + SQL_TABLENAME_NEVER_CHANGE["saved"] + " (name VARCHAR(255) PRIMARY KEY)")
        self.__addAllPlacesToPLACES()
    
    def __ensureTablesExist(self):
        tables_exist = False
        self.sql_cursor.execute("SHOW TABLES LIKE " + "'" + SQL_TABLENAME_NEVER_CHANGE["saved"] + "'")
        result = self.sql_cursor.fetchone()
        if result:
            tables_exist = True

        if(tables_exist == False):
            self.__initializeAllTables()

    def __init__(self):
        usernameIN = input("Enter your mysql username")
        passwordIN = input("Enter your password")

        self.username = usernameIN
        self.password = passwordIN
        self.sql = mscon.connect(host = "localhost",user = usernameIN, password = passwordIN)
        self.sql_cursor = self.sql.cursor()

        self.__createDB()

        self.sql = mscon.connect(host = "127.0.0.1", user = usernameIN, password= passwordIN,database=DATABASE_NAME_NEVER_CHANGE)
        self.sql_cursor = self.sql.cursor()

        self.__ensureTablesExist()