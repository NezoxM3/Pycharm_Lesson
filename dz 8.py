#Завдання 1

start = int(input("Введіть перше число:"))
end = int(input("Введіть друге число:"))

even = 0
odd = 0
nine = 0

for number in range(start, end + 1):
    if number % 2 == 0:
        even += number
    else:
        odd += number

    if number % 9 == 0:
        nine += number

print(f"Сума парних чисел:{even}")
print(f"Сума непарних чисел:{odd}")
print(f"Сума чисел, кратних 9:{nine}")

#Завдання 2
length = int(input("Введіть довжину лінії:"))
symbol = input("Введіть символ для заповнення лінії:")

for line in range(length):
    print(symbol)

#Завдання 4

numbers = []

while True:
    number = input("Введіть число:")

    if number == "7":
        print("Good bye!")
        break
    elif number:
        number = float(number)
        numbers.append(number)

        total_sum = sum(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

        print(f"Сума чисел:{total_sum}")
        print(f"Максимальне число:{maximum}")
        print(f"Мінімальне число:{minimum}")
    else:
        print("Введіть число")

#Завдання 3

while True:
    number = float(input("Введіть число:"))

    if number == "7":
        print("Good bye!")
        break

    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

