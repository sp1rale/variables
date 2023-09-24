import math

diameter = float(input("Введіть діаметр кола: "))

choice = input("Оберіть операцію (площа або периметр): ")

radius = diameter / 2

if choice == "площа":
    area = math.pi * radius ** 2
    print(f"Площа кола з діаметром {diameter} дорівнює {area:.2f} квадратних одиниць.")
elif choice == "периметр":
    perimeter = 2 * math.pi * radius
    print(f"Периметр кола з діаметром {diameter} дорівнює {perimeter:.2f} одиниць довжини.")
else:
    print("Ви ввели некоректний вибір операції. Оберіть 'площа' або 'периметр'.")