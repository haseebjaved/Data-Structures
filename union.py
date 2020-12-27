grades_A = [23, 45, 21, 67, 23, 41, 10, 11, 84, 45, 59, 100]

s_a = sorted(grades_A)
print(s_a)

grades_B = [100, 32, 84, 94, 20, 41, 66, 38, 3, 59, 23, 10, 100]

for b in grades_B:
    if b not in grades_A:
        grades_A.append(b)

#to remove duplicates
new = list(set(grades_A))
print(new)

#print(list(set(grades_A+grades_B)))
