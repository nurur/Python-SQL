#!/usr/bin/python
# SQL Query "INSERT" to add records to the EMPLOYEE table 


import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
#db = MySQLdb.connect("localhost","nurur","TESTDB")


# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE 
         (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
         VALUES 
         ('Marc', 'Pound', 55, 'M', 78000), 
         ('Peter', 'Teuben', 55, 'M', 78000)"""

'''
sql = "INSERT INTO EMPLOYEE \
       (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" \
       %( ('Marc', 'Pound', 55, 'M', 78000) '''

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
