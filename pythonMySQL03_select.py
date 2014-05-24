#!/usr/bin/python
# SQL Query "SELECT" to read records from the EMPLOYEE table 


import MySQLdb

# Open database connection
#db = MySQLdb.connect("localhost","testuser","test123","TESTDB")
db = MySQLdb.connect("localhost","nurur","", "TESTDB")


# Reading Method 1 
print '          '
print 'Reading Method 1: Reading rows as tuple of tuples:'
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a tuple of tuples.
    results = cursor.fetchall()
    print results 

    for row in results:
        fname  = row[0]
        lname  = row[1]
        age    = row[2]
        sex    = row[3]
        income = row[4]
        # Now print fetched result
        print "fname= %s, lname= %s, age= %d, sex= %s, income= %f" \
            % (fname, lname, age, sex, income )

except:
    print "Error: unable to fecth data"




# Reading Method 2
print '          '
print 'Reading Method 2: Reading rows as a dictationary:'
# prepare a cursor object using cursor() method
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# Prepare SQL query to INSERT a record into the database.
sql = """SELECT * FROM EMPLOYEE 
         WHERE INCOME > '%d'""" % (1000)


try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print results 
    
    for row in results:
        print "%s %s %d %f" \
            % (row["FIRST_NAME"], row["LAST_NAME"],  \
                   row["AGE"], row["INCOME"])

except:
    print "Error: unable to fecth data"



# disconnect from server
db.close()
