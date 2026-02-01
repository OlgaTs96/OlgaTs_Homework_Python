from address import Address
from mailing import Mailing

# Создаем адреса
to_addr = Address(index="123456",
                  city="Москва", street="Арбат", house="10", apartment="15")
from_addr = Address(index="654321", city="Санкт-Петербург",
                    street="Невский проспект", house="5", apartment="20")

# Создаем отправление
mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=250,
    track="AB123CD45678"
)

# Вывод информации
print(
    f"Отправление {mail.track} из {mail.from_address.index},"
    f"{mail.from_address.city}, {mail.from_address.street},"
    f"{mail.from_address.house} - {mail.from_address.apt} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street},{mail.to_address.house}"
    f"- {mail.to_address.apt}. "
    f"Стоимость {mail.cost} рублей."
)
