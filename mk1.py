while True:
    n1 = float(input('Введите первое число: '))
    action = input('Введите действие - ')
    n2 = float(input('Введите второе число: '))

    if action == "+":
        ans = n1 + n2
        print(ans)

    elif action == "-":
        ans = n1 - n2
        print(ans)

    elif action == "*":
        ans = n1 * n2
        print(ans)

    elif action == "/" and n2 == 0:
        print("на ноль делить нельзя !!!")

    elif action == "/":
        ans = n1 // n2
        print(ans)
    else:
        print("неопознанная операция")
