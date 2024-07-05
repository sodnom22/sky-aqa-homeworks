from address import Address
from mailing import Mailing

# Создание объектов адресов
to_address = Address("123456", "Улаанбаатор", "Арцат", "14", "33")
from_address = Address("654321", "Буэно-Айрес", "Палестина", "11", "43")

# Создание объекта почтового отправления
mailing = Mailing(to_address, from_address, 500, "TRACK123")

# Печать информации об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
