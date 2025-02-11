#Завдання 1
num1 = float(input("Введіть перше число:"))
num2 = float(input("Введіть друге число:"))
num3 = float(input("Введіть третє число:"))

choice = input("Введіть дію")

if choice == 'сума':
    print(num1 + num2 + num3)
elif choice == 'добуток':
    print(num1 * num2 * num3)
else:
    print("Error")
#Завдання 2
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

choice = input("Введіть максимальне, мінімальне або середнє значення чисел")

if choice == 'максимальне':
    print(max(num1, num2, num3))
elif choice == 'мінімальне':
    print (min(num1, num2, num3))
elif choice == 'середнє':
    print ((num1 + num2 + num3) / 3)
else:
    print("Error")
#Завдання 3
meters = float(input("Введіть кількість метрів: "))

choice = input("Переведіть метри в милі, дюйми або ярди")

if choice == 'милі':
    print (meters * 0.000621371192)
elif choice == 'дюйми':
    print (meters * 39.3700787)
elif choice == 'ярди':
    print (meters * 1.0936133 )
else:
    print("Error")