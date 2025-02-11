#Завдання 1
day = int(input("Введіть номер для дня тижня (1-7): "))

if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П'ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")
else:
    print("Введіть число від 1 до 7.")

#Завдання 2
month = int(input("Введіть номер для місяця року (1-12): "))

if month == 1:
    print("Січень")
elif month == 2:
    print("Лютий")
elif month == 3:
    print("Березень")
elif month == 4:
    print("Квітень")
elif month == 5:
    print("Травень")
elif month == 6:
    print("Червень")
elif month == 7:
    print("Липень")
elif month == 8:
    print("Серпень")
elif month == 9:
    print("Вересень")
elif month == 10:
    print("Жовтень")
elif month == 11:
    print("Листопад")
elif month == 12:
    print("Грудень")
else:
    print("Введіть число від 1 до 12.")

#Завдання 3
num = float(input("Введіть число:"))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

#Завдання 4
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if num1 == num2:
    print("Числа рівні.")
else:
    if num1 < num2:
        print(f"Числа в порядку зростання: {num1}, {num2}")
    else:
        print(f"Числа в порядку зростання: {num2}, {num1}")
