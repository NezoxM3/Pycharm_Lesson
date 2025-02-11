import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Вгадай число")
root.geometry("400x300")


def check_guess():
    guess = int(enter.get())
    if guess < random_number:
        result_label.config(text="Загадане число більше")
    elif guess > random_number:
        result_label.config(text="Загадане число менше")
    else:
        result_label.config(text="Ви вгадали число!")


def generate_new_number():
    global random_number
    random_number = randint(1, 100)
    result_label.config(text="Нове число уже загадане")



title = tk.Label(text="Вгадай число",
                       font=("Arial", 16))
title.pack()

guess_number = tk.Label(text="Введіть число від 1 до 100:")
guess_number.pack()

enter = tk.Entry(font=("Arial", 14))
enter.pack()

guees_button = tk.Button(text="Угадати",
                         bg="black",
                         fg = "white",
                         width=15,
                         font=("Comic Sans MS",20),
                         command = check_guess)
guees_button.pack()

random_button = tk.Button(text="Нове число",
                         bg="black",
                         fg = "white",
                         width=15,
                         font=("Comic Sans MS",20),
                         command = generate_new_number)
random_button.pack()

result_label = tk.Label(text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
