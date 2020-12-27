grades_A = [23, 45, 21, 67, 23, 41, 10, 11, 84, 45, 59, 100]

grades_B = [100, 32, 84, 94, 20, 41, 66, 38, 3, 59, 23, 10, 100]

inter = []

for i in range(len(grades_A)):
    for j in range(len(grades_B)):
        if grades_B[j] == grades_A[i] and grades_A[i] not in inter:
            inter.append(grades_A[i])

print(inter)

#print(inter.append(grades_A.intersection(grades_B)))

"""
#intersection_set = set(grades_A).intersection(set(grades_B))
intersection_set = set.intersection(set(grades_A), set(grades_B))
intersection_list = list(intersection_set)
print(intersection_list)"""
