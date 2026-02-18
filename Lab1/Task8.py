count = 0
min_height = 191
max_height = 149

while True:
    data = input()

    if data == "!":
        break

    height = int(data)

    if 150 <= height <= 190:
        count = count + 1

        if height < min_height:
            min_height = height

        if height > max_height:
            max_height = height

print(count)

if count > 0:
    print(min_height, max_height)