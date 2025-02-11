import tkinter as tk

spending_list = []
day_counter = 1

def add_expenses():
    global day_counter
    try:
        food = float(food_entry.get()) if food_entry.get() else 0
        transport = float(transport_entry.get()) if transport_entry.get() else 0
        other = float(other_entry.get()) if other_entry.get() else 0
        total = food + transport + other
        spending_list.append(total)
        day_counter += 1
        food_entry.delete(0, tk.END)
        transport_entry.delete(0, tk.END)
        other_entry.delete(0, tk.END)
        update_results()
    except ValueError:
        result_label.config(text="Error, Будь ласка, введіть числові значення!")

def show_results():
    if not spending_list:
        result_label.config(text="Немає збережених витрат.")
        return
    total_spending = sum(spending_list)
    result_text = "\n".join([f"День {i+1}: {exp:.2f} грн" for i, exp in enumerate(spending_list)])
    result_text += f"\nЗагальні витрати: {total_spending:.2f} грн"
    result_label.config(text=result_text)

def update_results():
    result_label.config(text="Витрати додано! Натисніть 'Результати', щоб переглянути.")

root = tk.Tk()
root.title("Облік витрат")
root.geometry("400x300")

tk.Label(root, text="Витрати на їжу:").pack()
food_entry = tk.Entry(root)
food_entry.pack()

tk.Label(root, text="Витрати на транспорт:").pack()
transport_entry = tk.Entry(root)
transport_entry.pack()

tk.Label(root, text="Витрати на інше:").pack()
other_entry = tk.Entry(root)
other_entry.pack()

tk.Button(root, text="Додати день", command=add_expenses).pack(pady=5)
tk.Button(root, text="Результати", command=show_results).pack(pady=5)

result_label = tk.Label(root, text="Витрати не додано.", justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()




