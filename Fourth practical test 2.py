#Регулярні вирази (15 хв)
import re


def validate_phone(phone):
    pattern = re.compile(r"^\+\d{12}$")

    if re.match(pattern, phone):
        print("Валідний номер")
    else:
        print("Помилка")


phone_number = input("Введіть номер телефону:")
validate_phone(phone_number)