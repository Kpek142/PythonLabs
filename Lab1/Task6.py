number = input()

d1 = int(number[0])
d2 = int(number[1])
d3 = int(number[2])

high = max(d1, d2, d3)
low = min(d1, d2, d3)

if d1 != high and d1 != low:
    middle = d1
elif d2 != high and d2 != low:
    middle = d2
else:
    middle = d3

if high + low == middle * 2:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")