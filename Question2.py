# Question link: https://drive.google.com/file/d/1xjiXgD_CKjO28M4o80Uzr_59Q3zB18oX/view?usp=sharing
def OrderingTeams():
    
    """I will compare the sum values of each person's skill and if the sum values are distinct, those are YES, else NO"""
    for each3x3 in allSkills:
        eachSum= [] # To take the sum values of each matrix
        for matrix in each3x3:
            eachSum.append(sum(matrix))
        if len(eachSum) == len(list(set(eachSum))): # Compares the lengths of the actual sum values to 
            # the list converted set. Set removes the duplicate items and thus, finding out if they are in order or not
            print("Yes")
        else:
            print("No")
        eachSum.clear() # Clears the list after iteration is over.


# Input section
testCases = int(input("testCases are: "))
allSkills = []

for i in range(testCases):
    cases = []
    for _ in range(3):
        person = list(map(int,input("Enter 3 skills for separating with space : ").strip().split(' ')))
        cases.append(person)
    allSkills.append(cases)

# Calling the function
OrderingTeams()
