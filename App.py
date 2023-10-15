import sqlite3

def main():

    #Display the menu
    menu()

    
def salesAndInventory():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Join sales and inventory tables and get item and price where qty > 2
    cursor.execute("SELECT IDesc, IPrice FROM Inventory INNER JOIN Sales ON Sales.IID = Inventory.IID WHERE SQty >= 2")
    result = cursor.fetchall()
    print()
    #print items 
    for item in result:
        formatted = "{0},{1}".format(*item)
        formatMore = formatted.replace(',','   $')
        print(formatMore)
    print()

    #Close the connection
    conn.close()
    #Display the main menu
    menu()

    
def customers():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get customer names from customers table
    cursor.execute("SELECT CFName, CLName from Customers")
    result = cursor.fetchall()
    print()
    #Display the customers
    for item in result:
        formatted = "{0},{1}".format(*item).title()        
        formatMore = formatted.replace(',',' ')
        print(formatMore)
    print()

    #Close the connection
    conn.close()
    #Display the main menu
    menu()

    
def inventory():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get item desc from inventory table
    cursor.execute("SELECT IDesc from Inventory")
    result = cursor.fetchall()
    print()
    #display inv items
    for item in result:
        formatted = "{0}".format(*item)        
        formatMore = formatted.replace(',',' ')
        print(formatMore)
    print()  

    #Close the connection
    conn.close()
    #Display the main menu
    menu()

    
def employees():

    #create a connection to the database
    conn = sqlite3.connect('halldb.db')
    cursor = conn.cursor()

    #Get emp id and last name from emp table
    cursor.execute("SELECT EID, ELname from Employees")
    result = cursor.fetchall()
    print()
    #display employees
    for item in result:
        formatted = "{0}, {1}".format(*item).title()        
        formatMore = formatted.replace(',',' ')
        print(formatMore)
    print()  

    #Close the connection
    conn.close()
    #Display the main menu
    menu()


def menu():

    #Menu items.

    print("****Sales and Inventory****")
    print("1. View Inventory with sales > 2: ")
    print()
    print("****Customers****")
    print("2. View all customers: ")
    print()
    print("****Inventory****")
    print("3. View all inventory items: ")
    print()
    print("  **Employees**")
    print("4. View employee ID and last name: ")
    print()    
    print("5. Quit the program")

#Get the menu choice.
    menuChoice = int(input('Enter your choice: '))
    #while choice is valid...
    while menuChoice >= 1 or menuChoice <= 5:
          
        # choice 1   
        if menuChoice == 1:
            salesAndInventory()
            break
        # choice 2  
        elif menuChoice == 2:
            customers()
            break
        # choice 3     
        elif menuChoice == 3:
            inventory()
            break
        # choice 4
        elif menuChoice == 4:
            employees()
            break
        # choice 5
        elif menuChoice == 5:
            print("Exiting program.")
            exit()
        else:
            #Display error message if choice is out of range
            print("Invalid entry.")
            #Prompt again for the choice.
            menu()
            menuChoice = int(input('Enter your choice: '))

main()

