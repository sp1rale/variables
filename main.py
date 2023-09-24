file_size_gb = float(input("Введіть розмір файлу в гігабайтах: "))
internet_speed_bps = float(input("Введіть швидкість інтернет-з'єднання в бітах на секунду: "))

choice = input("Оберіть одиницю вимірювання для часу (години, хвилини або секунди): ")

file_size_bits = file_size_gb * 8 * 1024 * 1024 * 1024
download_time_seconds = file_size_bits / internet_speed_bps

if choice == "години":
    download_time = download_time_seconds / 3600
    print(f"Час завантаження файлу: {download_time:.2f} годин")
elif choice == "хвилини":
    download_time = download_time_seconds / 60
    print(f"Час завантаження файлу: {download_time:.2f} хвилин")
elif choice == "секунди":
    download_time = download_time_seconds
    print(f"Час завантаження файлу: {download_time:.2f} секунд")
else:
    print("Ви ввели некоректну одиницю вимірювання. Оберіть 'години', 'хвилини' або 'секунди'.")