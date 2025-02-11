#Завдання 1
print("Завдання 1:")
def text():
    print ("\"Don't compare yourself with anyone in this world…\n"
             "if you do so, you are insulting yourself.\"\n"
             "Bill Gates")

text()

#Завдання 2
print("\nЗавдання 2:")
def even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(f"Число:{number}")

even_numbers(1, 10)

#Завдання 3
print("\nЗавдання 3:")
def min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)
print("Мінімальне з чиcло з: 6, 3, 7, 2, 5 є число: ")
print(min_of_five(6, 3, 7, 2, 5))

#Завдання 4
print("\nЗавдання 4:")
def product_seek(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for number in range(start, end + 1):
        product *= number
    return product
print("Добуток чисел у діапазоні від 5 до 3:")
print(product_seek(5, 3))

#Завдання 5
print("\nЗавдання 5:")
def count_numbers(number):

    return len(str(number))
print("Кількість цифр у 3456:")
print(count_numbers(3456))

#Завдання 6
print("\nЗавдання 6:")
def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]
print("Чи є число 123321 палідромом?")
print(is_palindrome(123321))


