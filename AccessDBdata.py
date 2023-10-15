#This program demonstrates the ability to access and display records from a database.

import sqlite3

conn = sqlite3.connect('halldb.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM Customers")
result = cursor.fetchall()

for row in result:
    print(row)
print("----------------------------")

cursor.execute("SELECT * FROM Employees")
result = cursor.fetchall()

for row in result:
    print(row)
print("----------------------------")

cursor.execute("SELECT * FROM Inventory")
result = cursor.fetchall()

for row in result:
    print(row)
print("----------------------------")

cursor.execute("SELECT * FROM Sales")
result = cursor.fetchall()

for row in result:
    print(row)
print("----------------------------")


conn.close()
