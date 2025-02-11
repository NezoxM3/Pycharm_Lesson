#Завдання 1
word = input("Введіть слово:\n")
check = word[:: -1]

if check == word:
    print("Паліндром")
else:
    print("Не паліндром")

#Завдання 2
text = input("Введіть текст:")

reserve = input("Введіть зарезервовані слова, розділені комою: ")

for slovo in reserve:
    text = text.replace(slovo, slovo.upper())

print(f"Змінений текст:{text}\n")

#Завдання 3
text = "Hello, my name is Max. I'm 16 years old now. Today is my birthday!"

point = ['.', '!', '?']

sentence = 0

for char in text:
    if char in point:
        sentence += 1

print(f"Кількість речень у тексті:{sentence}")
