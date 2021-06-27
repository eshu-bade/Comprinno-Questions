# Question link: 

def BeautifulArr():
    # Iterating over every pair
    for each_pair in full_list:
        k = each_pair[0] * each_pair[1] # k gives the product value of both numbers of the pair
        if k == each_pair[0] or k == each_pair[1]: # If k is equal to either of them, it's a beautiful Array
            print("YES")
        else:
            print("NO")


# Input section of the code
testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    integers = int(input("number of values: "))
    pairs = list(map(int,input("Enter numbers by separating with space : ").strip().split(' ')))[:integers]
    full_list.append(pairs)

# Calling the function
BeautifulArr()
