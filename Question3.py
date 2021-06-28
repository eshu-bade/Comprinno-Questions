# Question link: https://drive.google.com/file/d/1d5TKLBymv4Gu9c13I5UgXXMhknjYDr0B/view?usp=sharing

def templeLand():
    # Creating an even list to check the lenght of the given values
    evens = [i * 2 for i in range(1, 100)]

    # iterating over all the strings one by one
    for each_list in full_list:
        if len(each_list) in evens:
            print("No")
        elif each_list[0] != 1 and each_list[-1] != 1: # If the first and last parameters are non-zero, prints NO
            print("No")
        else:
            middle = len(each_list) // 2
            if sum(each_list[:middle]) == sum(each_list[middle + 1:]): # Using the slicing method
                print("Yes")
            else:
                print("No")
                

# Input section of the code

strips = int(input("strips: "))
full_list = []
for i in range(strips):
    integers = int(input("number of values: "))
    # Using list and map function to take multiple inputs at once.
    values = list(map(int, input("Enter the numbers by separating with space : ").strip().split(' ')))[:integers]
    full_list.append(values)# List of the lists.

# Calling the function
templeLand()
