#Question link: https://drive.google.com/file/d/1tOWenG1HyknKIA1rygImrXkkuIAs1oT0/view?usp=sharing
def CatsDogs():
    for each in full_list:
        # Dividing the values and assigning them to variables for better understanding
        cat = each[0]
        dog = each[1]
        legs = each[-1]
        if cat ==1 and (sum(each[:2])*4 == legs or sum(each[:2])*2 == legs):
            print("YES")
        elif (cat == 2 and dog == 1) and (legs ==4 or legs == 8 or legs == 12):
            print("YES")
        elif dog == 2 and (legs == 8 or legs == 12 or legs == 16 or legs == 20):
            print("YES")
        else:
            print("NO")


testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    pairs = list(map(int, input("Enter cats, dogs and legs counts by separating with space : ").strip().split(' ')))[:3]
    full_list.append(pairs)


# Calling the function
CatsDogs()
