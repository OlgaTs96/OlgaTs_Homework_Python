user_login = "adam"
user_pass = "Qwerty123456"

login = input("login: ")
password = input("password: ")

if (login == user_login) and (password == user_pass):
    print("Secret is open")
else:
    print("Locked")

crit1 = "red"
crit2 = "lock"

color = input("color: ")
feture = input("Feture: ")

if (color == crit1) or (feture == crit2):
    print("buy it!")
else:
    print("похожу еще посмотрю")