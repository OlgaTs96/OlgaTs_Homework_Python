from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "IPhone_12", "+79000000000"),
    Smartphone("Sumsung", "Galaxy_A35", "+79123456789"),
    Smartphone("Xiomi", "Redme9", "+79631234567"),
    Smartphone("Techno", "Nova", "+79991112233"),
    Smartphone("Nokia", "3310", "+7998887766")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
