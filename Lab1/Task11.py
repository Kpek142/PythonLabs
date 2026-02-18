n = int(input())

for i in range(1, n + 1):
    spaces_count = n - i
    stars_count = 2 * i - 1

    print(' ' * spaces_count + '*' * stars_count)