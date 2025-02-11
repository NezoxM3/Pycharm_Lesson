#Завдання 1
total = 0

def add_to_cart(price):
    global total
    total += price
    print(f"Сума всіх товарів: {total} грн.")

add_to_cart(40)
add_to_cart(20)
add_to_cart(70)

print(f"Cума всіх покупок: {total}")

#Завдання 2
print()

glasses_drunk = 0


def drink_water():
    global glasses_drunk
    glasses_drunk += 1
    print(f"За сьогодні ви вже випили {glasses_drunk} бутилку води")

    if glasses_drunk == 4:
        print("Ви досягли денного мінімуму!")

drink_water()
drink_water()
drink_water()
drink_water()

#Завдання 3
print()

steps_count = 0

def add_steps(count):
    global steps_count
    steps_count += count

    print(f"Кількість кроків зараз: {steps_count}")

    if steps_count >= 10000:
        print("Ви досягли своєї мети на сьогодні!")

add_steps(1000)
add_steps(4000)
add_steps(5000)

#Завдання 4
print()

budget = 5000

def spend_money(amount):
    global budget
    budget -= amount
    print(f"Ви потратили ще {amount} грн, залигилося: {budget} грн.")

    if budget < 0:
        print("Ви перевищили бюджет!")


spend_money(300)
spend_money(1120)
spend_money(2000)
spend_money(50)
spend_money(1540)