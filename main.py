number1 = float(input("Введіть перше число: "))

number2 = float(input("Введіть друге число: "))

if number1 == number2:
    print("Числа рівні.")
else:

    if number1 < number2:
        print("Числа у порядку зростання:", number1, number2)
    else:
        print("Числа у порядку зростання:", number2, number1)