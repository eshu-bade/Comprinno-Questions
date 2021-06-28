# Question link: https://drive.google.com/file/d/1_zO3vzgLV3s-BF2xVkj7vwWwXJ6hMO4V/view?usp=sharing
def chefSticks():
    all_areas = []
    rectPossibility = []

    for each in full_list:
        for i in range(len(each)):
            # Assigning length and width values for better understanding
            width = each[i]
            length= width+width
            if each.count(width) ==2 and each.count(length) ==2:# if width and length occurs twice, areas will be added
                all_areas.append(length*width)
                possibility = 'Yes'
                rectPossibility.append(possibility)
            else:
                possibility = 'No'
                rectPossibility.append(possibility)

        if 'Yes' not in rectPossibility:# Prints -1 if rectangle is not possible
            print(-1)
        else:
            print(max(all_areas)) # Prints max possible area
        rectPossibility.clear()# Clears the list for every new list


# Input section of the code
testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    integers = int(input("number of values: "))
    pairs = list(map(int,input("Enter numbers by separating with space : ").strip().split(' ')))[:integers]
    full_list.append(pairs)

# Calling the main function
chefSticks()
