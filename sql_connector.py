import mysql.connector as mscon
import csv

regular_alphabet = "abcdefghijklmnopqrstuvwxyz -"

DATABASE_NAME_NEVER_CHANGE = "cs_project_ns_ys_ma_2020_sqlDB"

#as of 6th november, search history and saved places are not implemented, they should only be implemented after everything is complete si-nishchay
SQL_TABLENAME_NEVER_CHANGE = {"places" : "PLACES","searches" : "SEARCHES", "saved" : "SAVED"}

MAJOR_CITIES_FILENAME_NEVER_CHANGE = "major_cities.csv"

class simple_sql:

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
        self.sql_cursor.execute("CREATE TABLE " + SQL_TABLENAME_NEVER_CHANGE["places"] + " (name VARCHAR(255) PRIMARY KEY)")
        self.__addAllPlacesToPLACES()
        self.sql_cursor.execute("CREATE TABLE " +  SQL_TABLENAME_NEVER_CHANGE["searches"] + "(search_name VARCHAR(255) NOT NULL, order_val INT NOT NULL)")
        self.sql_cursor.execute("CREATE TABLE " +  SQL_TABLENAME_NEVER_CHANGE["saved"] + "(search_name VARCHAR(255) NOT NULL, order_val INT NOT NULL, FOREIGN KEY (search_name) REFERENCES PLACES(name))")

    
    def __ensureTablesExist(self):
        tables_exist = False
        self.sql_cursor.execute("SHOW TABLES LIKE " + "'" + SQL_TABLENAME_NEVER_CHANGE["places"] + "'")
        result = self.sql_cursor.fetchone()
        if result:
            tables_exist = True
            self.sql_cursor.execute("SELECT MAX(order_val) as last_search_val FROM " + SQL_TABLENAME_NEVER_CHANGE["searches"])
            self.searchesOrderLast = self.sql_cursor.fetchone()[0]
            if(self.searchesOrderLast == None):
                self.searchesOrderLast = 0

            self.sql_cursor.execute("SELECT MAX(order_val) as last_search_val FROM " + SQL_TABLENAME_NEVER_CHANGE["saved"])
            self.savedOrderLast = self.sql_cursor.fetchone()[0]

            if(self.savedOrderLast == None):
                self.savedOrderLast = 0

        if(tables_exist == False):
            self.__initializeAllTables()
        
    
    def addToSearches(self,searchname):
        self.searchesOrderLast  +=1
        self.sql_cursor.execute("INSERT INTO " + SQL_TABLENAME_NEVER_CHANGE["searches"] + " values(" + '"' + searchname + '",' + str(self.searchesOrderLast) + ")" )
        self.sql.commit()
    
    def addToSaved(self,placename):
        self.savedOrderLast += 1
        self.sql_cursor.execute("INSERT INTO " + SQL_TABLENAME_NEVER_CHANGE["saved"] + " values(" + '"' + placename + '",'  + str(self.savedOrderLast) + ")" )
        self.sql.commit()

    def __init__(self):
        usernameIN = input("Enter your mysql username")
        passwordIN = input("Enter your password")

        self.username = usernameIN
        self.password = passwordIN
        self.sql = mscon.connect(host = "localhost",user = usernameIN, password = passwordIN)
        self.sql_cursor = self.sql.cursor()

        self.searchesOrderLast = 0  #these will be updated to actual values in the ensure tables exist function (they are for ordering)
        self.savedOrderLast = 0

        self.__createDB()

        self.sql = mscon.connect(host = "127.0.0.1", user = usernameIN, password= passwordIN,database=DATABASE_NAME_NEVER_CHANGE)
        self.sql_cursor = self.sql.cursor()

        self.__ensureTablesExist()

        """
        alright so a not so quick explanation of whats going on:
            Obviously you'll need the username and password to access sql, we also store it just in case we need it again
            the sql_cursor is what you will need to execute commands (basically writes whatever you give as arg to execute() in sql)
            in the __createDB() function, we use create if not exists to only create the database if it does not exists,
            this makes it safe to use it. (it would give an error if it did not exist)
            then we just reset our sql and sql cursor to use our database.
        """

#db = simple_sql()