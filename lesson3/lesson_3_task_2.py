from smartphone import Smartphone

# Создание списка объектов
catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79161234568"),
    Smartphone("Google", "Pixel 6", "+79161234569"),
    Smartphone("OnePlus", "9 Pro", "+79161234570"),
    Smartphone("Sony", "Xperia 5", "+79161234571")
]

# Печать каталога
for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.phone_number}")
