import math

def square(side_length):
    area = side_length * side_length
    return math.ceil(area)

# Пример вызова функции
side_length = 4.7
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")

# Пример с целым числом
side_length = 5
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")

# Пример с дробным числом
side_length = 4.7
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")

# Пример с маленьким числом
side_length = 1.2
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")

