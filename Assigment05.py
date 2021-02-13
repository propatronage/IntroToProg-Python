# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#   RRoot,1.1.2030,Created started script
#   Tyler Tidd,02/11/21,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
import os

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

if os.path.isfile(objFile):
    file = open(objFile, "r")
    for i in file:
        lstRow = i.split(",")  # Returns a list!
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    file.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if lstTable:
            for i in lstTable:
                print(i["Task"] + " | " + i["Priority"])
            continue
        else:
            input("There is no data yet. Press enter to continue")
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input('What is the new task name?: ')
        priority = input('What is the new task priority?: ')
        newitem = [task, priority]
        dicRow = {"Task": newitem[0], "Priority": newitem[1]}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        item = input("Which item do you want to remove?: ")
        for i in lstTable:
            if i['Task'] == item:
                lstTable.remove(i)
                print(item, "deleted")
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        file = open(objFile, "w")
        for i in lstTable:
            file.write(i["Task"] + ',' + i["Priority"] + '\n')
        print("Data saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Bye, Felica!")
        break  # and Exit the program
