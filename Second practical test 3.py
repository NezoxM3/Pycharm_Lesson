#Гра «Вгадай число» (10-15 хв)
import random

num = random.randint(1, 100)
attempts = 10

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

    if attempts <= 0:
        print("Ви не вгадали число за 10 спроб")


