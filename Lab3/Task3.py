list1 = [1, 2, 3, 4, 5, 10, 50]
list2 = [4, 5, 6, 7, 8, 10, 50, 1]

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)

print(sorted(intersection))