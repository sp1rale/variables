total_seconds = int(input("Введіть час у секундах: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"До опівночі залишилося {hours} годин, {minutes} хвилин і {seconds} секунд.")