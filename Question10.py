# Question link: https://drive.google.com/file/d/1D04UW7BLtnc2Y5QDAcLP2vqpHifdFclX/view?usp=sharing
def GrossSalary():
    for eachSalary in allSalaries:
        # Iterating through all the loops
        if eachSalary<1500:
            HRA = 10*(eachSalary/100)
            DA = 90*(eachSalary/100)
            gross = HRA+DA+eachSalary
            strGross = str(gross)

        else:
            DA = 98*(eachSalary/100)
            gross = DA+500+eachSalary
            strGross = str(gross)
            
        if strGross[-2:] == '.0': # This will check if the gross has .00 and removes them
            print(int(gross))
        else:
            print(gross)


# Input section of the code
testCases = int(input("testCases are: "))
allSalaries = []
for i in range(testCases):
    salary = int(input("Give the salaries: "))
    allSalaries.append(salary)

# Calling the main function
GrossSalary()
