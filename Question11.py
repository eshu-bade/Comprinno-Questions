# Question link: https://drive.google.com/file/d/1BREQ7XGQBES21xUknHvw2Oxn9cfivWzH/view?usp=sharing

# The main function
def IDandShip():
    for each in full_list:# Since I used lower() in input, we dont have to use capital letters in comparisons
        if each == 'b':
            print("BattleShip")
        elif each == 'c':
            print("Cruiser")
        elif each == 'd':
            print("Destroyer")


# Input section
testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    character = input("Char is: ").lower() # Converts all the letters to lower
    full_list.append(character)

# Calling the function
IDandShip()
