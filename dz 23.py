import tkinter as tk

root = tk.Tk()
root.title("Вгадай число")
root.geometry("400x300")

title = tk.Label(text="Вгадай число",
                       font=("Arial", 16))
title.pack()

guess_number = tk.Label(text="Введіть число від 1 до 100:")
guess_number.pack()

enter = tk.Entry(font=("Arial", 14))
enter.pack()

check_button = tk.Button(text="Перевірити",
                         font=("Arial", 12))
check_button.pack()

root.mainloop()