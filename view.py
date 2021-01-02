# PyBase
# Author: Dmitrii Iakimchuk

# The 'View' part of the MVC structure. This part is responsible for user interface

from controller import *

# Creating a menu to greet the user and show the options
def welcomeMenu():
    print("\nChoose an option:"
          "\n1 - Print all rows of the database"
          "\n2 - Choose a specific record from the file"
          "\n3 - Update a record"
          "\n4 - Remove a record"
          "\n5 - Add a new record"
          "\n6 - Select records based on multiple input"
          "\n7 - Exit the program")

# Taking input from the user, validating it, and executing a respective function
    option = int(input())
    if option not in [1, 2, 3, 4, 5, 6, 7]:
        print("Invalid option. Try again")
        welcomeMenu()
    else:
        if option == 1:
            dbprint()
        elif option == 2:
            dbChooseRecord()
        elif option == 3:
            dbUpdateRecord()
        elif option == 4:
            dbDeleteRecord()
        elif option == 5:
            dbAddRecord()
        elif option == 6:
            dbMultipleChoice()
        elif option == 7:
            print("Goodbye!")
            exit(1)
    welcomeMenu()


welcomeMenu()
