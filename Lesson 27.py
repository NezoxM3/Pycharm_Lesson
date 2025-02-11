import tkinter as tk
import random
import time

def move_button():
    global start_time


    if time.time() - start_time < 30:
        new_x = random.randint(0,500)
        new_y = random.randint(0,400)
        button.place(x=new_x, y = new_y)
        root.after(500,move_button)

    else:
        end_game()

def click():
    global click_count
    click_count += 1
    click_label.config(text = f"Кількість кліків: {click_count}")

def restart_game():
    global click_count, start_time
    click_count = 0
    start_time = time.time()
    button.config(state="normal")
    button.place(x=250, y=250)
    click_label.config(text=f"Кількість кліків: {click_count}")
    restart_button.pack_forget()
    move_button()

def end_game():
    button.config(state="disabled")
    click_label.config(text=f"Гра завершена! Кількість кліків: {click_count}")
    restart_button.pack(pady=20)

click_count = 0
start_time = time.time()



root = tk.Tk()
root.title("Click the Button")
root.geometry("600x600+700+200")


click_label = tk.Label(root, text = f"Кількість кліків: {click_count}",
                       font = ("Arial", 14))

click_label.pack()

restart_button = tk.Button(root, text="Повторити спробу",
                           font=("Arial", 14),
                           command=restart_game)
restart_button.pack_forget()

button = tk.Button(root, text = f"Натисни мене!",
                       font = ("Arial", 14), command=click)

button.place(x=250,y=250)

move_button()

root.mainloop()