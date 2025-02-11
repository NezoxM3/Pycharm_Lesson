#Завдання 1
user_input = input("Введіть рядок: ")

letters = 0
numbers = 0

for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        numbers += 1

print(f"Кількість букв: {letters}")
print(f"Кількість цифр: {numbers}")

#Завдання 2
text_1 = input("Введи речення:")
found = input("Що потрібно порахувати?:")
count_of_char = text_1.count(found)
print(count_of_char)

#Завдання 3
text_2 = input("Введи речення:")
found = input("Яке слово потрібно порахувати?:")
count_of_char = text_2.count(found)
print(count_of_char)

#Завдання 4
text = input("Введіть текст:")
search = input("Введіть слово яке хочете замінити:")
replace_word = input("Введіть слово на яке хочете замінити:")

modified_text = text.replace(search,replace_word)
print(modified_text)
