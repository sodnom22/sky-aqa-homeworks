def is_year_leap(year):
    return year % 4 == 0

# Вызов функции и передача ей года
year = 2024
result = is_year_leap(year)

# Вывод результата
print(f"год {year}: {result}")


# Пример с годом 2023
year = 2023
result = is_year_leap(year)
print(f"год {year}: {result}")

def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Вызов функции и передача ей года
year = 2024
result = is_year_leap(year)

# Вывод результата
print(f"год {year}: {result}")

# Пример с годом 2023
year = 2023
result = is_year_leap(year)
print(f"год {year}: {result}")

