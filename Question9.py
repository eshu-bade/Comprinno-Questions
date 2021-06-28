# Question link: https://drive.google.com/file/d/1IGAqccBmckjnEmTcXmkELeSyAvpl6nvP/view?usp=sharing
def MinMax():
    sumValues = []
    for eachValue in full_list:
        new = eachValue.copy() # Copying the same list to remove the items
        for i in range(len(new)-1):
            a, b = new[i], new[i+1]
            if a>b:# If a is greater than b, a is removed and b is added to the list
                eachValue.remove(a)
                sumValues.append(b)
            else:# If b is greater than a, b is removed and a is added to the list
                eachValue.remove(b)
                sumValues.append(a)
        print(sum(sumValues))# This will print the sum of all the sumvalues
        sumValues.clear()# Clears the list everytime for each loop


# Input section of the code
testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    integer = int(input("Give the number of integers: "))
    pairs = list(map(int,input("Enter numbers by separating with space : ").strip().split(' ')))
    full_list.append(pairs)

# Calling the main function
MinMax()
