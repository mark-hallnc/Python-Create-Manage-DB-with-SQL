#The program creates a database and seeds it with tables and data for use in later projects.

import sqlite3

#Create the db file
connection = sqlite3.connect('halldb.db')

#Create cursor to interact with db
cursor = connection.cursor()

#Create the customers table
customersTable = """CREATE TABLE IF NOT EXISTS
Customers(CID INTEGER PRIMARY KEY AUTOINCREMENT, CFName TEXT, CLName TEXT)"""

cursor.execute(customersTable)

#Create the employees table
employeesTable = """CREATE TABLE IF NOT EXISTS
Employees(EID INTEGER PRIMARY KEY AUTOINCREMENT, EFName TEXT, ELName TEXT)"""

cursor.execute(employeesTable)

#Create the inventory table
inventoryTable = """CREATE TABLE IF NOT EXISTS
Inventory(IID INTEGER PRIMARY KEY AUTOINCREMENT, IDesc TEXT, IPrice TEXT)"""

cursor.execute(inventoryTable)

#Create the sales table
salesTable = """CREATE TABLE IF NOT EXISTS
Sales(SID INTEGER PRIMARY KEY AUTOINCREMENT, SQty INTEGER, STotal FLOAT, EID TEXT, IID TEXT, CID TEXT, FOREIGN KEY(EID)
REFERENCES Employees(EID), FOREIGN KEY(IID) REFERENCES Inventory(IID), FOREIGN KEY(CID) REFERENCES Customers(CID))"""

cursor.execute(salesTable)



#data to test that table creation executed succesfully.
#Customers table
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(1, 'larry', 'smith')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(2, 'terry', 'jones')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(3, 'curly', 'simpson')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(4, 'steve', 'harvey')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(5, 'sally', 'white')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(6, 'Jessica', 'hernandez')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(7, 'adam', 'abbott')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(8, 'petra', 'johnson')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(9, 'hillary', 'jones')")
cursor.execute("INSERT OR REPLACE INTO Customers VALUES(10, 'bob', 'simmons')")


#Employees table
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(11, 'marty', 'byrd')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(12, 'walter', 'white')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(13, 'justin', 'beiber')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(14, 'john', 'dutton')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(15, 'beth', 'dutton')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(16, 'kacey', 'dutton')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(17, 'monica', 'dutton')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(18, 'jesse', 'pinkman')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(19, 'jacob', 'hazelwood')")
cursor.execute("INSERT OR REPLACE INTO Employees VALUES(20, 'drew', 'pinsky')")


#Inventory table
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(21, 'iphone 1', 12.65)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(22, 'iphone 2', 14.87)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(23, 'iphone 3', 25.36)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(24, 'iphone 4', 30.00)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(25, 'iphone 5', 40.00)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(26, 'iphone 6', 52.00)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(27, 'iphone 7', 82.00)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(28, 'iphone 8', 128.00)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(29, 'iphone 9', 954.00)")
cursor.execute("INSERT OR REPLACE INTO Inventory VALUES(30, 'iphone 10', 2478.00)")


#Sales table
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1234, 12, 14.87, 11, 21, 3)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1235, 1, 23.90, 12, 30, 2)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1236, 1, 23.90, 12, 28, 1)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1237, 1, 23.90, 13, 27, 9)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1238, 1, 23.90, 15, 26, 7)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1239, 1, 23.90, 19, 25, 5)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1240, 1, 23.90, 16, 25, 6)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1241, 1, 23.90, 17, 25, 8)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1242, 1, 23.90, 12, 24, 9)")
cursor.execute("INSERT OR REPLACE INTO Sales VALUES(1243, 1, 23.90, 12, 28, 3)")


connection.commit()
connection.close()

print("Database created succesfully. You can close the program.")

