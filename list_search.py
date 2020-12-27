grades = [23, 45, 21, 67, 23, 9, 10, 11, 84, 45]

user_grade = int(input("Please enter your grade: "))

match = 0
no_match = 0

for i in range(len(grades)):
    if user_grade != grades[i]:
        no_match += 1
    else:
        match += 1

if no_match == len(grades):
    print("There is No match")
elif match == 1:
    print("There is a match")
else:
    print("There is are {} matches".format(match))

"""if user_grade in grades:
    print("there is a match")
else:
    print("there is NO match")"""
