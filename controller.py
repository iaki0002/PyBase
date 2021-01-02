# PyBase
# Author: Dmitrii Iakimchuk

# The 'Controller' part of the MVC structure. This part contains the 'engine' of the program: all logic and functions

from model import *

# Function to print all rows from the database. The 'Read' part of CRUD
def dbprint():
    mycursor.execute("select * from mytable")
    for i in mycursor:
        print(i)

# Function to print a specific record based on the user input. The 'Read' part of CRUD
def dbChooseRecord():
    print("Select how you would like to choose a record: "
          "\n1. Choose a single record by its row number"
          "\n2. Choose all records with a specific attribute")
    choiceRecord1 = int(input())

# Print a record by ID
    if choiceRecord1 == 1:
        # Printing instructions
        print("Enter the number of the record you would like to choose: ")
        # Taking user's input
        choiceRecord2 = int(input())
        # Sending the request with the user input to the database
        mycursor.execute(f"select * from mytable where N= '{choiceRecord2}'")
        # Printing the result received from the database
        print(f"Record number {choiceRecord2}:")
        for i in mycursor:
            print(i)

# Print a record by a specific attribute
    elif choiceRecord1 == 2:
        print("Select the attribute to choose: "
              "\n1. id"
              "\n2. date"
              "\n3. cases"
              "\n4. deaths"
              "\n5. name in French"
              "\n6. name in English")
        choiceRecord3 = int(input())
        if choiceRecord3 == 1:
            print("Enter the id: ")
            choiceRecordId = input()
            mycursor.execute(f"select * from mytable where id= '{choiceRecordId}'")
            print(f"Records with the ID of {choiceRecordId}: ")
            for i in mycursor:
                print(i)
        elif choiceRecord3 == 2:
            print("Enter the date in format YYYY-MM-DD: ")
            choiceRecordDate = input()
            mycursor.execute(f"select * from mytable where date= '{choiceRecordDate}'")
            print(f"Records with the date of {choiceRecordDate}: ")
            for i in mycursor:
                print(i)
        elif choiceRecord3 == 3:
            print("Enter the N of cases: ")
            choiceRecordCases = input()
            mycursor.execute(f"select * from mytable where cases= '{choiceRecordCases}'")
            print(f"Records with {choiceRecordCases} cases: ")
            for i in mycursor:
                print(i)
        elif choiceRecord3 == 4:
            print("Enter the N of deaths: ")
            choiceRecordDeaths = input()
            mycursor.execute(f"select * from mytable where deaths= '{choiceRecordDeaths}'")
            print(f"Records with {choiceRecordDeaths} deaths: ")
            for i in mycursor:
                print(i)
        elif choiceRecord3 == 5:
            print("Enter the name in French: ")
            choiceRecordNameFrench = input()
            mycursor.execute(f"select * from mytable where name_fr= '{choiceRecordNameFrench}'")
            print(f"Records with the French name of {choiceRecordNameFrench}: ")
            for i in mycursor:
                print(i)
        elif choiceRecord3 == 6:
            print("Enter the name in English: ")
            choiceRecordNameEnglish = input()
            mycursor.execute(f"select * from mytable where name_en= '{choiceRecordNameEnglish}'")
            print(f"Records with the English name of {choiceRecordNameEnglish}: ")
            for i in mycursor:
                print(i)

# Function to update a record in the database based on the input, choosing the record ID first and then updating
# the specific fields based on the input. The 'Update' part of CRUD
def dbUpdateRecord():
    print("Select the N of the record to update: ")
    choiceUpdateN = int(input())
    print("You are updating the record: ")
    mycursor.execute(f"select * from mytable where N= '{choiceUpdateN}'")
    for i in mycursor:
        print(i)

    print("Select the attribute to update: "
          "\n1. id"
          "\n2. date"
          "\n3. cases"
          "\n4. deaths"
          "\n5. name in French"
          "\n6. name in English")
    choiceUpdateRecord = int(input())
    if choiceUpdateRecord == 1:
        print("Enter the new id in the format XX: ")
        choiceRecordId = input()
        mycursor.execute(f"update mytable set id= '{choiceRecordId}' where N='{choiceUpdateN}'")
        print("Success. The updated record: ")
        mycursor.execute(f"select * from mytable where N= '{choiceUpdateN}'")
        for i in mycursor:
            print(i)
        # Committing the change to the database
        mydb.commit()

    elif choiceUpdateRecord == 2:
        print("Enter the new date in format YYYY-MM-DD: ")
        choiceRecordDate = input()
        mycursor.execute(f"update mytable set date= '{choiceRecordDate}' where N= '{choiceUpdateN}'")
        print("Success. The updated record: ")
        mycursor.execute(f"select * from mytable where n= '{choiceUpdateN}'")
        for i in mycursor:
            print(i)
        mydb.commit()

    elif choiceUpdateRecord == 3:
        print("Enter the new number of cases: ")
        choiceRecordCases = int(input())
        mycursor.execute(f"update mytable set cases= '{choiceRecordCases}' where N= '{choiceUpdateN}'")
        print("Success. The updated record: ")
        mycursor.execute(f"select * from mytable where n= '{choiceUpdateN}'")
        for i in mycursor:
            print(i)
        mydb.commit()

    elif choiceUpdateRecord == 4:
        print("Enter the new number of deaths: ")
        choiceRecordDeaths = int(input())
        mycursor.execute(f"update mytable set deaths= '{choiceRecordDeaths}' where N= '{choiceUpdateN}'")
        print("Success. The updated record: ")
        mycursor.execute(f"select * from mytable where n= '{choiceUpdateN}'")
        for i in mycursor:
            print(i)
        mydb.commit()

    elif choiceUpdateRecord == 5:
        print("Enter the new name in French: ")
        choiceRecordNameFr = input()
        mycursor.execute(f"update mytable set name_fr= '{choiceRecordNameFr}' where N= '{choiceUpdateN}'")
        print("Success. The updated record: ")
        mycursor.execute(f"select * from mytable where n= '{choiceUpdateN}'")
        for i in mycursor:
            print(i)
        mydb.commit()

    elif choiceUpdateRecord == 6:
        print("Enter the new name in English: ")
        choiceRecordNameEn = input()
        mycursor.execute(f"update mytable set name_en= '{choiceRecordNameEn}' where N= '{choiceUpdateN}'")
        print("Success. The updated record: ")
        mycursor.execute(f"select * from mytable where n= '{choiceUpdateN}'")
        for i in mycursor:
            print(i)
        mydb.commit()

# Function to delete a record from the database. The 'Delete' part of CRUD
def dbDeleteRecord():
    print("Select how you would like to delete a record from the database: "
          "\n1. Delete a single record by N"
          "\n2. Delete all records with a specific attribute")
    choiceDelete1 = int(input())

# Option to delete a record based on its ID
    if choiceDelete1 == 1:
        print("Enter the id of the record you'd like to delete: ")
        choiceDeleteN = int(input())
        mycursor.execute(f"delete from mytable where N= '{choiceDeleteN}'")
        mydb.commit()
        print(f"Record {choiceDeleteN} has been deleted")

# Option to delete a record or records with a specified attribute
    elif choiceDelete1 == 2:
        print("select the condition to delete by: "
              "\n1. id"
              "\n2. date"
              "\n3. cases"
              "\n4. deaths"
              "\n5. name in French"
              "\n6. name in English")
        choiceDeleteRecord = int(input())
        if choiceDeleteRecord == 1:
            print("Enter the ID of the record to delete in the format XX: ")
            choiceRecordId = input()
            mycursor.execute(f"delete from mytable where id='{choiceRecordId}'")
            print(f"All records with the ID of {choiceRecordId} have been deleted")
            mydb.commit()

        elif choiceDeleteRecord == 2:
            print("Enter the date to delete records with in the format YYYY-MM-DD: ")
            choiceRecordDate = input()
            mycursor.execute(f"delete from mytable where date= '{choiceRecordDate}'")
            print(f"All records with the date of {choiceRecordDate} have been deleted")
            mydb.commit()

        elif choiceDeleteRecord == 3:
            print("Enter the number of cases to delete records with: ")
            choiceRecordCases = int(input())
            mycursor.execute(f"delete from mytable where cases= '{choiceRecordCases}'")
            print(f"All records with {choiceRecordCases} cases have been deleted")
            mydb.commit()

        elif choiceDeleteRecord == 4:
            print("Enter the number of deaths to delete records with: ")
            choiceRecordDeaths = int(input())
            mycursor.execute(f"delete from mytable where deaths= '{choiceRecordDeaths}'")
            print(f"All records with {choiceRecordDeaths} deaths have been deleted")
            mydb.commit()

        elif choiceDeleteRecord == 5:
            print("Enter the name in French to delete records with: ")
            choiceRecordNameFr = input()
            mycursor.execute(f"delete from mytable where name_fr= '{choiceRecordNameFr}'")
            print(f"All records with the French name of {choiceRecordNameFr} have been deleted")
            mydb.commit()

        elif choiceDeleteRecord == 6:
            print("Enter the name in English to delete records with: ")
            choiceRecordNameEn = input()
            mycursor.execute(f"delete from mytable where name_en= '{choiceRecordNameEn}'")
            print(f"All records with the English name of {choiceRecordNameEn} have been deleted")
            mydb.commit()

# Function to add a new record to the database. The 'Create' part of CRUD
def dbAddRecord():
    print("Enter the ID in the format XX: ")
    dbAddId = input()
    print("Enter the date in the format YYYY-MM-DD: ")
    dbAddDate = input()
    print("Enter the N of cases: ")
    dbAddCases = int(input())
    print("Enter the number of deaths: ")
    dbAddDeaths = int(input())
    print("Enter the name in French: ")
    dbAddNameFr = input()
    print("Enter the name in English: ")
    dbAddNameEn = input()

    mycursor.execute(f"insert into mytable(id, date, cases, deaths, name_fr, name_en)"
                     f"values ('{dbAddId}', '{dbAddDate}', '{dbAddCases}', '{dbAddDeaths}',"
                     f"'{dbAddNameFr}', '{dbAddNameEn}')")
    mydb.commit()
    print(f"A new record with the values of:"
          f"\nID: {dbAddId} \nDate: {dbAddDate} \nCases: {dbAddCases} \nDeaths: {dbAddDeaths} "
          f"\nFR name: {dbAddNameFr} \nEN name: {dbAddNameEn} \nhas been added")

def dbMultipleChoice():
    # Search records based on multiple columns at same time
    print("Enter the amount of columns to base the search on (2, 3, 4): ")
    columnNChoice = int(input())

    # Validating the input
    if columnNChoice not in [2, 3, 4]:
        print("Invalid option. Try again")
        dbMultipleChoice()

    # function to take input for 2 columns and 2 values from the user and search the database for records based
    # on the input values. The function prints the result afterwards
    else:
        if columnNChoice == 2:
            print("Enter 2 columns to select values from: \nColumn 1: ")
            mcValue1 = input()
            print("Column 2: ")
            mcValue2 = input()
            print(f"Enter values: \nValue for {mcValue1}: ")
            mcValue3 = input()
            print(f"Value for {mcValue2}: ")
            mcValue4 = input()
            mycursor.execute(f"select * from mytable where {mcValue1} = '{mcValue3}' and {mcValue2} = '{mcValue4}'")
            for i in mycursor:
                print(i)

        elif columnNChoice == 3:
            print("Enter 3 columns to select values from: \nColumn 1: ")
            mcValue1 = input()
            print("Column 2: ")
            mcValue2 = input()
            print("Column 3: ")
            mcValue3 = input()
            print(f"Enter values: \nValue for {mcValue1}: ")
            mcValue4 = input()
            print(f"Value for {mcValue2}: ")
            mcValue5 = input()
            print(f"Value for {mcValue3}: ")
            mcValue6 = input()
            mycursor.execute(f"select * from mytable where {mcValue1} = '{mcValue4}' and {mcValue2} = '{mcValue5}' "
                             f"and {mcValue3} = '{mcValue6}'")
            for i in mycursor:
                print(i)

        elif columnNChoice == 4:
            print("Enter 4 columns to select values from: \nColumn 1: ")
            mcValue1 = input()
            print("Column 2: ")
            mcValue2 = input()
            print("Column 3: ")
            mcValue3 = input()
            print("Column 4: ")
            mcValue4 = input()
            print(f"Enter values: \nValue for {mcValue1}: ")
            mcValue5 = input()
            print(f"Value for {mcValue2}: ")
            mcValue6 = input()
            print(f"Value for {mcValue3}: ")
            mcValue7 = input()
            print(f"Value for {mcValue4}: ")
            mcValue8 = input()
            mycursor.execute(f"select * from mytable where {mcValue1} = '{mcValue5}' and {mcValue2} = '{mcValue6}' "
                             f"and {mcValue3} = '{mcValue7}' and {mcValue4} = '{mcValue8}'")
            for i in mycursor:
                print(i)

