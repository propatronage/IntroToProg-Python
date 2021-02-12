# Character creator program

attributes = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
points = 40

print('''
Welcome to the character creator program
You get to add 40 points to your character's attributes
The attibutes are: Strength, Health, Wisdom, Dexterity''')

while True:
    print(
"""
Which Attribute do you want to update?
1 - Strength
2 - Health
3 - Wisdom
4 - Dexterity
5 - View point totals
"""
    )
    attribute = input("Choice: ")
    if attribute == "5":
        for myKey, myValue in attributes.items():
            print(myKey, myValue)
        input("Press any key to continue")
        continue
    print(
"""
What do you want to do with that attribute?
1 - add points
2 - remove points
"""
    )
    addrm = input('Choice: ')
    if addrm == "1":
        new = int(input("how many points do you want to add? "))
        attributes[attribute] += new
        points -= new
        print("You now have:", attributes[attribute], "points in ",attribute,"!")
        print("And", points, "points left to use")
    elif addrm == "2":
        new = int(input("how many points do you want to subtract? "))
        attributes[attribute] -= new
        points += new
        print("You now have:", attributes[attribute], "points in ",attribute,"!")
        print("And", points, "points left to use")
    else: print("That's not an option")
