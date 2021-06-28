# Question link: https://drive.google.com/file/d/1rtQCt1g9qAYzYQb9AUX0MRVJ5Z1Xa0tV/view?usp=sharing

from math import ceil
def AliceBob():
    for eachCase in full_list:
        alice,bob, N_turns = eachCase # Assigning each values to variables for better understanding
        a = ceil(N_turns / 2)# This will round the number to the next integer 2.5 becomes 3
        b = N_turns - a
        if N_turns == 1:
            alice*=2
            print(alice // bob)
        elif N_turns>1 and N_turns%2!=0:# Odd
            for i in range(a):
                alice*=2
            for i in range(b):
                bob*=2
        elif N_turns>1 and N_turns%2==0:
            for i in range(a):
                alice *= 2
                bob*=2
        if alice>bob: # Integere division after comaping the values
            print(alice//bob)
        elif bob>alice:
            print(bob//alice)


# Input section of the code
testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    pairs = list(map(int,input("Enter numbers by separating with space : ").strip().split(' ')))
    full_list.append(pairs)

# Calling the main function
AliceBob()
