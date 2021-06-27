# Question link: https://drive.google.com/file/d/1YyMzLed3RZEWcYIjSQ5Ze1hJqFWyWmYt/view?usp=sharing

def MilkCookies():
    validities = [] # Taking a list to see if all the strings follow the pattern
    for each_case in full_list:
        """Iterating over the complete input section """
        
        if (len(each_case) ==1 or each_case[-1] =='cookie') and  'cookie' in each_case:
            # Prints NO if a single input or the last parameter of the input and cookie in the list
            print("NO")
        # Prints YES if a single input or the if just milk in the input
        elif ('milk'in each_case or len(each_case) ==1) and 'cookie' not in each_case:
            print("YES")
        elif len(each_case)>1:
            for i in range(len(each_case)): # eat = ['c', 'm', 'm', 'c', 'm', 'c', 'm']

                if each_case[i] == 'cookie':
                    if each_case[i+1] == 'milk':
                        validity = 'True'
                        validities.append(validity)
                    else:
                        validity = 'False'
                        validities.append(validity)
            if 'False' in validities:
                print("NO")
            else:
                print("YES")
    validities.clear()


# Input section of the code
testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    integers = int(input("number of values: "))
    inputStrings = list(map(str,input("Enter either milk or cookie by separating with space : ").strip().split(' ')))[:integers]
    full_list.append(inputStrings)

# Calling the function
MilkCookies()
