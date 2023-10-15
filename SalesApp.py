# This program demonstrates the ability to manipulate database data (add/remove/modify) based
# on user selection. 

import sqlite3

fname = ""
lname = ""
def main():


    #Display the menu
    menu()


def getName(fName, lName):

    fName = input("Customer first name: ")
    lName = input("Customer last name: ")

    return fName, lName

def removeCustomer(fName, lName):

    firstName = fName
    lastName = lName
    
    
    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the first and last name to remove.
    getName()

    #Query the database to see if name exists.
    cursor.execute("DELETE FROM Customers WHERE CFName = ? AND CLName = ?", (firstName.lower(), lastName.lower()))
    conn.commit()
    results = cursor.fetchall()
    #Check if any rows are returned.
    rowCount = cursor.rowcount
    #If query returns a row, name was found. If it does not, name does not exist.
    if rowCount == 0:
        print("Customer not found")
        print()
    else:
        print()
        print("Customer " + firstName + " " + lastName + " succesfully removed")
        print()
        
    #Close the connection
    conn.close()
    #Return to the menu
    menu()
    

def modifyCustomer():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Display sub menu
    print("What would you like to update?")
    print("1. First name")
    print("2. Last name")

    #Get menu choice
    menuChoice = int(input('Enter your choice: '))
    while menuChoice >= 1 or menuChoice <= 2:
          
        # choice 1   
        if menuChoice == 1:

            #Get first, last and new first name
            firstName = input("Customer first name: ")
            lastName = input("Customer last name: ")
            newFirstName = input("What is the new first name? ")

            #Query database to see is customer exists. If they do, replace.
            cursor.execute("UPDATE Customers SET CFName = ? WHERE CFName = ? AND CLName = ?", (newFirstName.lower(), firstName.lower(), lastName.lower()))
            conn.commit()
            results = cursor.fetchall()
            rowCount = cursor.rowcount

            #If no rows returned, name was not found. If a row is found, name exists.
            if rowCount == 0:
                print("Customer not found")
                print()
            else:
                print()
                print("Customer " + newFirstName + " " + lastName + " succesfully updated")
                print()
           
            #Close the connection
            conn.close()
            #Display the main menu
            menu()
          
        elif menuChoice == 2:

            #Get first, last and new last name
            firstName = input("Customer first name: ")
            lastName = input("Customer last name: ")
            newLastName = input("What is the new last name? ")
            
            #Query database to see is customer exists. If they do, replace.            
            cursor.execute("UPDATE Customers SET CLName = ? WHERE CFName = ? AND CLName = ?", (newLastName.lower(), firstName.lower(), lastName.lower()))
            conn.commit()
            results = cursor.fetchall()
            rowCount = cursor.rowcount
            
            #If no rows returned, name was not found. If a row is found, name exists.
            if rowCount == 0:
                print("Customer not found")
                print()
            else:
                print()
                print("Customer " + firstName + " " + newLastName + " succesfully updated")
                print()
            
            #Close the connection
            conn.close()
            #Display the main menu            
            menu()
            
        
def addCustomer():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the first and last name to add.
    firstName = input("Enter customer first name: ")
    lastName = input("Enter customer last name: ")

    #Add customer to database. 
    cursor.execute("INSERT INTO Customers (CFName, CLName) VALUES (?,?)", (firstName.lower(), lastName.lower()))
    conn.commit()
    print()
    print("Customer " + firstName, lastName + " sucessfully added")
    print()
        
    #Close the connection
    conn.close()
    #Display the main menu
    menu()


def removeEmployee():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the first and last name to remove.
    firstName = input("Customer first name: ")
    lastName = input("Customer last name: ")

    #Query the database to see if name exists.
    cursor.execute("DELETE FROM Employees WHERE EFName = ? AND ELName = ?", (firstName.lower(), lastName.lower()))
    conn.commit()
    results = cursor.fetchall()
    #Check if any rows are returned.
    rowCount = cursor.rowcount
    #If query returns a row, name was found. If it does not, name does not exist.
    if rowCount == 0:
        print("Employee not found")
        print()
    else:
        print()
        print("Employee " + firstName + " " + lastName + " succesfully removed")
        print()

    cursor.execute("SELECT * from Employees")
    lName = cursor.fetchall()
    for name in lName:
        print(name)
        
    #Close the connection
    conn.close()
    #Return to the menu
    menu()
    

def modifyEmployee():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Display sub menu
    print("What would you like to update?")
    print("1. First name")
    print("2. Last name")

    #Get menu choice
    menuChoice = int(input('Enter your choice: '))
    while menuChoice >= 1 or menuChoice <= 2:
          
        # choice 1   
        if menuChoice == 1:

            #Get first, last and new first name
            firstName = input("Employee first name: ")
            lastName = input("Employee last name: ")
            newFirstName = input("What is the new first name? ")

            #Query database to see is customer exists. If they do, replace.
            cursor.execute("UPDATE Employees SET EFName = ? WHERE EFName = ? AND ELName = ?", (newFirstName.lower(), firstName.lower(), lastName.lower()))
            conn.commit()
            results = cursor.fetchall()
            rowCount = cursor.rowcount

            #If no rows returned, name was not found. If a row is found, name exists.
            if rowCount == 0:
                print("Employee not found")
                print()
            else:
                print()
                print("Employee " + newFirstName + " " + lastName + " succesfully updated")
                print()

            cursor.execute("SELECT * from Employees")
            lName = cursor.fetchall()
            for name in lName:
                print(name)

            #Close the connection
            conn.close()
            #Display the main menu
            menu()
          
        elif menuChoice == 2:

            #Get first, last and new last name
            firstName = input("Employee first name: ")
            lastName = input("Employee last name: ")
            newLastName = input("What is the new last name? ")
            
            #Query database to see is customer exists. If they do, replace.            
            cursor.execute("UPDATE Employees SET ELName = ? WHERE EFName = ? AND ELName = ?", (newLastName.lower(), firstName.lower(), lastName.lower()))
            conn.commit()
            results = cursor.fetchall()
            rowCount = cursor.rowcount
            
            #If no rows returned, name was not found. If a row is found, name exists.
            if rowCount == 0:
                print("Employee not found")
                print()
            else:
                print()
                print("Employee " + firstName + " " + newLastName + " succesfully updated")
                print()
 
            cursor.execute("SELECT * from Employees")
            lName = cursor.fetchall()
            for name in lName:
                print(name)

            #Close the connection
            conn.close()
            #Display the main menu            
            menu()
            
        
def addEmployee():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the first and last name to add.
    firstName = input("Enter employee first name: ")
    lastName = input("Enter employee last name: ")

    #Add customer to database. 
    cursor.execute("INSERT INTO Employees (EFName, ELName) VALUES (?,?)", (firstName.lower(), lastName.lower()))
    conn.commit()
    print()
    print("Employee " + firstName, lastName + " sucessfully added")
    print()


    cursor.execute("SELECT * from Employees")
    lName = cursor.fetchall()
    for name in lName:
        print(name)

        
    #Close the connection
    conn.close()
    #Display the main menu
    menu()


def removeInventoryItem():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the first and last name to remove.
    desc = input("Enter item description: ")

    #Query the database to see if name exists.
    cursor.execute("DELETE FROM Inventory WHERE IDesc = ?", (desc.lower(),))
    conn.commit()
    results = cursor.fetchall()
    #Check if any rows are returned.
    rowCount = cursor.rowcount
    #If query returns a row, name was found. If it does not, name does not exist.
    if rowCount == 0:
        print("Item not found")
        print()
    else:
        print()
        print("Item " + desc + " succesfully removed")
        print()
         #           #for testing only
    cursor.execute("SELECT * from Inventory")
    lName = cursor.fetchall()
    for name in lName:
        print(name)

    #Close the connection
    conn.close()
    #Return to the menu
    menu()
    

def modifyInventoryItem():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Display sub menu
    print("What would you like to update?")
    print("1. Item description")
    print("2. Item price")

    #Get menu choice
    menuChoice = int(input('Enter your choice: '))
    while menuChoice >= 1 or menuChoice <= 2:
          
        # choice 1   
        if menuChoice == 1:

            #Get desc and new desc.
            desc = input("Item description: ")
            newDesc = input("What is the new description? ")

            #Query database to see is item exists. If it does, update desc.
            cursor.execute("UPDATE Inventory SET IDesc = ? WHERE IDesc = ?", (newDesc.lower(), desc.lower()))
            conn.commit()
            results = cursor.fetchall()
            rowCount = cursor.rowcount

            #If no rows returned, item was not found. If a row is found, item exists.
            if rowCount == 0:
                print("Item not found")
                print()
            else:
                print()
                print("Item " + desc + " succesfully updated")
                print()

            cursor.execute("SELECT * from Inventory")
            lName = cursor.fetchall()
            for name in lName:
                print(name)

            #Close the connection
            conn.close()
            #Display the main menu
            menu()
          
        elif menuChoice == 2:

            #Get desc and new price.
            desc = input("Enter item description: ")
            newPrice = int(input("What is the new price? "))
            
            #Query database to see is item exists. If it does, update price.            
            cursor.execute("UPDATE Inventory SET IPrice = ? WHERE IDesc = ?", (newPrice, desc.lower()))
            conn.commit()
            results = cursor.fetchall()
            rowCount = cursor.rowcount
            
            #If no rows returned, item was not found. If a row is found, item exists.
            if rowCount == 0:
                print("Item not found")
                print()
            else:
                print()
                print("Item " + desc + " succesfully updated")
                print()

            cursor.execute("SELECT * from Inventory")
            lName = cursor.fetchall()
            for name in lName:
                print(name)

            #Close the connection
            conn.close()
            #Display the main menu            
            menu()
            
        
def addInventoryItem():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get the item and price to add.
    desc = input("Enter item description: ")
    price = input("Enter item price: ")

    #Add item to database. 
    cursor.execute("INSERT INTO Inventory (IDesc, IPrice) VALUES (?,?)", (desc.lower(), price))
    conn.commit()
    print()
    print("Item " + desc + " sucessfully added")
    print()

    
    cursor.execute("SELECT * from Inventory")
    lName = cursor.fetchall()
    for name in lName:
        print(name)
        
    #Close the connection
    conn.close()
    #Display the main menu
    menu()
    

    
def menu():

    #Menu items.
    print()
    print("What would you like to do?")
    print("  **Customers**")
    print("1. Add a new customer ")
    print("2. Modify existing customer information")
    print("3. Delete a customer")
    print()
    print("  **Employees**")
    print("4. Add a new employee")
    print("5. Modify existing employee information")
    print("6. Delete an employee")
    print()
    print("  **Inventory**")
    print("7. Add a new item")
    print("8. Modify existing item information")
    print("9. Delete an item")
    print()    
    print("10. Quit the program")

    #Get the menu choice.
    menuChoice = int(input('Enter your choice: '))
    #while choice is valid...
    while menuChoice >= 1 or menuChoice <= 7:
          
        # choice 1   
        if menuChoice == 1:
            addCustomer()
            break
        # choice 2  
        elif menuChoice == 2:
            modifyCustomer()
            break
        # choice 3     
        elif menuChoice == 3:
            removeCustomer(fName, lName)
            break
        # choice 4
        elif menuChoice == 4:
            addEmployee()
            break
        # choice 5  
        elif menuChoice == 5:
            modifyEmployee()
            break
        # choice 6     
        elif menuChoice == 6:
            removeEmployee()
            break
        # choice 7        
        elif menuChoice == 7:
            addInventoryItem()
            break
        # choice 8 
        elif menuChoice == 8:
            modifyInventoryItem()
            break
        # choice 9     
        elif menuChoice == 9:
            removeInventoryItem()
            break
        # choice 10
        elif menuChoice == 10:
            print("Exiting program.")
            exit()
        else:
            #Display error message if choice is out of range
            print("Invalid entry.")
            #Prompt again for the choice.
            menu()
            menuChoice = int(input('Enter your choice: '))



main()

