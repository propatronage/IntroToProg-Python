# -------------------------------------------------- #
# Title: Listing 9
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Your Name Here>,<Date>,Changed rows from lists to dictionaries
# -------------------------------------------------- #

# Declare my variables
strChoice = '' # User input
lstRow = [] # list of data
dicRow = {} # Dictionary of data
strFile = 'HomeInventory.txt'  # data storage file
objFile = None  # file handle

# Get user Input
while(True):
    print("Write or Read file data, then type 'Exit' to quit!")
    strChoice = input("Choose to [W]rite or [R]ead data: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif (strChoice.lower() == 'w'):
        # List to File
        objFile = open(strFile, "w")
       # lstRow = ["Lamp", "$30"]
        dicRow = {"item": "lamp", "price": "$30"}
        objFile.write(dicRow["item"] + ',' + dicRow["price"] + '\n')
       # dicRow = ["End Table", "$60"]
        dicRow = {"item": "End Table", "price": "$60"}
        objFile.write(dicRow["item"] + ',' + dicRow["price"] + '\n')
        objFile.close()


    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            #dicRow = row.split(",") # Returns a list!
            dicRow = {"item": dicRow[0], "price": dicRow[1].strip()}
            print(dicRow["item"] + '|' + dicRow["price"].strip())
        objFile.close()
    else:
        print('Please choose either W or R!')
