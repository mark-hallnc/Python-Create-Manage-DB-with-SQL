#This program demonstrates the ability to add and remove transactions from a database for a 
#sales tracking system.

import sqlite3


def main():

    #Display the menu
    menu()


def voidSalesTransaction():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the transaction ID to remove.
    transID = input("Enter the transaction # to void: ")

    #Query the database to see if trans exists.
    cursor.execute("DELETE FROM Sales WHERE SID = ?", [transID])
    conn.commit()
    results = cursor.fetchall()
    #Check if any rows are returned.
    rowCount = cursor.rowcount
    #If query returns a row, transaction was found. If it does not, transaction does not exist.
    if rowCount == 0:
        print("Transaction not found")
        print()
    else:
        print()
        print("Transaction " + transID + " succesfully removed")
        print()
    
    cursor.execute("SELECT * from Sales")
    trans = cursor.fetchall()
    for x in trans:
        print(x)

    #Close the connection
    conn.close()
    #Return to the menu
    menu()
    

def addSalesTransaction():


    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the sales data to add to the database.
    quantity = int(input("Qty sold: "))
    unitPrice = int(input("Unit price: "))
    total = quantity * unitPrice
    employeeID = input("Employee ID: ")
    itemID = input("Item ID: ")
    customerID = input("Customer ID: ")
    
    #Add transaction to database. 
    cursor.execute("INSERT INTO Sales (SQty, STotal, EID, IID, CID) VALUES (?,?,?,?,?)",
                   (quantity, total, employeeID, itemID, customerID))
    conn.commit()

    cursor.execute("SELECT SID from Sales order by SID desc limit 1")
    sale = cursor.fetchone()
    formattedtransID = "{}".format(*sale)
    print()
    print("Transaction # " + formattedtransID + " complete. ")
    print()

          
    cursor.execute("SELECT * from Sales")
    trans = cursor.fetchall()
    for x in trans:
        print(x)

        
    #Close the connection
    conn.close()
    #Display the main menu
    menu()


def menu():

    #Menu items
    print()
    print("1. New Sales Transaction")
    print("2. Void Sales Transaction")
    print()

    print("3. Quit the program")

    #Get the menu choice.
    menuChoice = int(input('Enter your choice: '))
    #while choice is valid...
    while menuChoice >= 1 or menuChoice <= 3:
          
        # choice 1   
        if menuChoice == 1:
            addSalesTransaction()
            break
        # choice 2  
        elif menuChoice == 2:
            voidSalesTransaction()
            break
        # choice 3     
        elif menuChoice == 3:
            print("Exiting program.")
            exit()
        else:
            #Display error message if choice is out of range
            print("Invalid entry.")
            #Prompt again for the choice.
            menu()
            menuChoice = int(input('Enter your choice: '))



main()

