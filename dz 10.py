#Завдання 1
text = input("Введіть вираз:")

operator = ""

num1, operator, num2 = text.split()

num1 = float(num1)
num2 = float(num2)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль"
else:
    result = "Невідомий оператор"

print(f"Результат: {result}")

#Завдання 2
number = input("Enter the list of numbers with space: ")

numbers = number.split()

num = [int(num) for num in numbers]

list_even = []
list_odd = []
list_positive = []
list_negative = []

for num in num:
    if num % 2 == 0:
        list_even.append(num)

    if num % 2 != 0:
        list_odd.append(num)

    if num < 0:
        list_negative.append(num)

    if num > 0:
        list_positive.append(num)

print("Even numbers:", list_even)
print("Odd numbers:", list_odd)
print("Negative numbers:", list_negative)
print("Positive numbers:", list_positive)
