#Цикли + списки (15 хв)
numbers = []

for i in range(5):
    while True:
        try:
            num = float(input(f"Введіть число:"))
            numbers.append(num)
            break
        except ValueError:
            print("Error. Введіть число.")

print(f"\nВведені числа: {numbers}")
print(f"Найбільше число: {max(numbers)}")
print(f"Найменше число: {min(numbers)}")