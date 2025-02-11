import re


login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}")
login_pattern_hard = re.compile(r"[a-zA-Z0-9._%+-]{2,6}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,8}$")


login = input("Введи свій Email: ")


if login_pattern.search(login):
    print("Логін правильний")

else:
    print("Не корректний логін")


password_pattern = re.compile(r"^(?=.[A-Za-z])(?=.*\d){6,}")

password = input("Введи свій пароль: ")

if password_pattern.search(password):
    print("Пароль правильний")

else:
    print("Не корректний пароль")


    #?????????????????????????????

password_pat = re.compile(r"\w(nazar)@[a-z]{2,10}\.[a-z]{2,6}")

password = input("Введи свій пароль: ")

if password_pat.search(password):
    print("Пароль правильний")

else:
    print("Не корректний пароль")