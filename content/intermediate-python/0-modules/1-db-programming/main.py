import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password ="159357",
    database = "testdb" # added after create db
)

my_cursor = mydb.cursor()

# -----

# my_cursor.execute("CREATE DATABASE testdb")

# -----
# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db)

# -----

# my_cursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# my_cursor.execute("SHOW TABLES")

# for tb in my_cursor:
#     print(tb)

# -----

# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

## Single data
# student1 = ("Rachel", 22)

# my_cursor.execute(sqlFormula, student1)

# mydb.commit()

## Plural datas
# students = [("Rachel", 22),
#             ("Mike", 24),
#             ("Victoria", 21),
#             ("Eddy", 20),
#             ("Mai", 22)]

# my_cursor.executemany(sqlFormula, students)

# mydb.commit()

# -----

# my_cursor.execute("SELECT * FROM students")
# my_cursor.execute("SELECT age FROM students")
# my_cursor.execute("SELECT age FROM students ORDER BY age DESC;")

# result = my_cursor.fetchall()
# # result = my_cursor.fetchone()

# for row in result:
#     print(row)

# -----

# sql = "SELECT * FROM students WHERE age=22"
# sql = "SELECT * FROM students WHERE name='Rachel'"
# sql = "SELECT * FROM students WHERE name LIKE '%O%'"
# sql = "SELECT * FROM students WHERE name= %s"

# my_cursor.execute(sql)
# my_cursor.execute(sql, ("Levo",)) # used for formatted sql params
# result = my_cursor.fetchall() 

# for row in result:
#     print(row)

# -----

# sql = "UPDATE students SET age = 13 WHERE name = 'Levo'"

# my_cursor.execute(sql) # used for formatted sql params
# mydb.commit()

# sql = "SELECT * FROM students LIMIT 4"
# sql = "SELECT * FROM students ORDER BY age DESC LIMIT 4"
# sql = "SELECT * FROM students ORDER BY age DESC LIMIT 4 OFFSET 2"
# my_cursor.execute(sql)
# result = my_cursor.fetchall()

# for row in result:
#     print(row)

# -----

# sql = "DELETE FROM students WHERE name = 'Levo'"
# sql = "DELETE FROM students WHERE age = 21"

# sql = "DROP TABLE students"
# sql = "DROP TABLE IF EXISTS students"

# my_cursor.execute(sql)
# mydb.commit()
