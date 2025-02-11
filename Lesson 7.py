import random

num = random.randint(1, 100)
attempts = 5

print("Вгадайте число від 1 до 100. У вас є 5 спроб.")

while attempts > 0:
    guess = int(input("Введіть ваше число: "))

    if guess < num:
        print("Число більше")
    elif guess > num:
        print("Число менше")
    else:
        print("Ви вгадали число!")
        break

    attempts -= 1
    print("Ви не вгадали число за 5 спроб")

