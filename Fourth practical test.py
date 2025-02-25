#4. Регулярні вирази (15 хв) ?
import re

email_pattern = re.compile(r"[a-zA-Z0-9._-]{2,6}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,8}$")


email = input("Введи свій Email: ")


if re.match(email_pattern, email):
    print("Логін правильний")
else:
    print("Не корректний логін")