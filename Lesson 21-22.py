import random

#Завдання 1
try:
    age = int(input("Введіть ваш вік: "))

    if 0 <= age <= 120:
        print("Ваш вік коректний.")
    else:
        print("Таке неможливо!")

except ValueError:
    print("Error. Вам не може бути не числове число років")

#Завдання 2
try:
    exchange_kurs = 41.88

    uah_amount = float(input("Введіть суму в гривнях: "))

    if uah_amount < 0:
        print("Error. потрібно додатнє число")

    exchange_kurs = 41.88

    usd_amount = uah_amount / exchange_kurs
    print(f"Сума у доларах: {usd_amount:} USD")

except ValueError:
    print("Error. Введіть числове значення.")

#Завдання 3
try:
    celsius = float(input("Введіть температуру в Цельсіях: "))

    fahrenheit = celsius * 9 / 5 + 32

    print(f"Температура {celsius} С у Фаренгейтах: {fahrenheit:} F")

except ValueError:
    print("Error. Введіть числове значення.")

#Завдання 4
guess_number = random.randint(1, 100)

while True:
    try:
        user_guess = int(input("Введіть ваше число: "))

        if user_guess < 1 or user_guess > 100:
            print("Error. Введіть число від 1 до 100.")

        if user_guess == guess_number:
            print("Ви вгадали число!")
            break
        elif user_guess < guess_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

    except ValueError:
        print("Error: введіть числове значення.")

#Завдання 5
try:
    hour = int(input("Введіть годину, від 0 до 23: "))

    if 0 <= hour <= 23:
        print("Година правильна")
    else:
        print("Error. Година має бути від 0 до 23.")

except ValueError:
    print("Error. Введіть числове значення")

#Завдання 6
try:
    length = float(input("Введіть довжину прямокутника:"))
    width = float(input("Введіть ширину прямокутника:"))

    if length <= 0 or width <= 0:
        print("Error. Довжина та ширина мають бути додатними числами.")

    area = length * width
    print(f"Площа прямокутника: {area}:")

except ValueError:
    print("Error. Введіть числове значення")

#Завдання 7
try:
    hours = float(input("Введіть кількість годин від 1 до 24: "))

    if 0 <= hours <= 24:
        minutes = hours * 60
        print(f"{hours} годин є {minutes:} хвилинами.")
    else:
        print("Error. Година має бути від 0 до 24.")

except ValueError:
    print("Error. Введіть числове значення.")

#Завдання 8 (Доробити з високосним роком)
try:
    day =int(input("Введіть день (1-31): "))
    month = int(input("Введіть місяць (1-12): "))
    year = int(input("Введіть рік: "))

    if month < 1 or month > 12:
        raise ValueError ("Місяць має бути в діапазоні від 1 до 12")

    if month == 2 and day > 29:
        raise ValueError ("У лютому може бути максимум 29 днів")

    if day < 1 or day > 31:
        raise ValueError("День має бути в діапазоні від 1 до 31")

    if day == 31 and month in [4,6,9,11]:
        raise ValueError ("У цьому місяці лише 30 днів")

except ValueError as e:
    print(f"Помилка: {e}")

else:
    print(f"Введена дата: {day}-{month}-{year}")
