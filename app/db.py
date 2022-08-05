import psycopg2

def create_db(db_name, db_user, db_passwd, db_host, db_port):
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database mydb''';

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    conn.close()

def create_table():

    #Establishing the connection
    conn = psycopg2.connect(
    database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Doping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    #Creating table as per requirement
    sql ='''CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
    )'''
    cursor.execute(sql)
    print("Table created successfully........")
    conn.commit()
    #Closing the connection
    conn.close()

def insert_to_table():

    #Establishing the connection
    conn = psycopg2.connect(
    database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
    cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
    cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
    cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
    cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")

    # Closing the connection
    conn.close()





def delete_from_table():
    #establishing the connection
    conn = psycopg2.connect(
    database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Retrieving contents of the table
    print("Contents of the table: ")
    cursor.execute('''SELECT * from EMPLOYEE''')
    print(cursor.fetchall())

    #Deleting records
    cursor.execute('''DELETE FROM EMPLOYEE WHERE AGE > 0''')

    #Retrieving data after delete
    print("Contents of the table after delete operation ")
    cursor.execute("SELECT * from EMPLOYEE")
    print(cursor.fetchall())

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()


def drop_table():

    #establishing the connection
    conn = psycopg2.connect(
    database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Doping EMPLOYEE table if already exists
    cursor.execute("DROP TABLE EMPLOYEE")
    print("Table dropped... ")

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

conn = psycopg2.connect(
    database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cursor.fetchall():
    print(table)