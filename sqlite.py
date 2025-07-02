import sqlite3

## connect to sqlite 
connection= sqlite3.connect('student.db')

##create a cursor object to insert record,create table
cursor=connection.cursor()

##create the table
table_info="""
CREATE TABLE STUDENT(NAME VARCAR(25),CLASS VARCAR(25),
SECTION VARCAR(25),MARKS INT)
"""
cursor.execute(table_info)

## insert some more records
cursor.execute('''Insert Into Student values('Shishir','Data Science','A',90)''')
cursor.execute('''Insert Into Student values('Rohit','Data Science','B',85)''')
cursor.execute('''Insert Into Student values('Anjali','Data Science','A',95)''')
cursor.execute('''Insert Into Student values('Priya','Data Science','B',80)''')
cursor.execute('''Insert Into Student values('Rahul','Data Science','A',88)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from Student''')
for row in data:
    print(row)
