price_per_console = float(input("Введіть вартість однієї ігрової приставки: "))
quantity = int(input("Введіть кількість ігрових приставок: "))
discount_percentage = float(input("Введіть відсоток знижки (0-100): "))

choice = input("Оберіть операцію (замовлення або вартість однієї приставки зі знижкою")
if choice == "замовлення":
    total_price = price_per_console * quantity * (1 - discount_percentage / 100)
    print(f"Загальна сума замовлення: {total_price:.2f} грн")
elif choice == "вартість однієї приставки зі знижкою":
    discounted_price = price_per_console * (1 - discount_percentage / 100)
    print(f"Вартість однієї приставки зі знижкою: {discounted_price:.2f} грн")
else:
    print("Ви ввели некоректний вибір операції. Оберіть 'замовлення' або 'вартість однієї приставки зі знижкою'.")