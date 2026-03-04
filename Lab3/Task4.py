numbers = [1, 2, 4, 4, 4, 5, 6, 6, 10, 45, 45]

seen = set() #пустое множество для хранения встреченных чисел

for i in numbers:
    if i in seen:
        print("YES")
    else:
        print("NO")
        seen.add(i)