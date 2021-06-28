#Question link: https://drive.google.com/file/d/1tOWenG1HyknKIA1rygImrXkkuIAs1oT0/view?usp=sharing
def CatsDogs():
    for each in full_list:
        # Dividing the values and assigning them to variables for better understanding
        cat = each[0]
        dog = each[1]
        legs = each[-1]
        animalsCount = sum(each[:1]) # without the legs count
        if dog ==1 and cat <=3 and (legs in [i*4 for i in range(dog, animalsCount+1)] or legs == 8):
            print("YES")
        elif dog == 2 and cat>=4 and cat <= 6 and (legs in [i*4 for i in range(dog, animalsCount+1)]):
            print("YES")
        else:
            print("NO")


testCases = int(input("testCases are: "))
full_list = []
for i in range(testCases):
    pairs = list(map(int, input("Enter numbers by separating with space : ").strip().split(' ')))[:3]
    full_list.append(pairs)


# Calling the function
CatsDogs()
