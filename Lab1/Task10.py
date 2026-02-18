while True:
    num1 = int(input())

    operation = input()

    if operation == 'x':
        print(num1)
        break

    elif operation == '!':
        if num1 >= 0:
            result = 1
            for i in range(1, num1 + 1):
                result = result * i
            print(result)

    else:
        num2 = int(input())

        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            if num2 != 0:
                print(num1 // num2)
        elif operation == '%':
            if num2 != 0:
                print(num1 % num2)