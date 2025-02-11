numbers = input("Введіть елементи списку цілих чисел через пробіл: ").split()

max_number = max(numbers)
min_number = min(numbers)
max_index = numbers.index(max_number)
min_index = numbers.index(min_number)

print(f"Найбільше значення: {max_number}, індекс: {max_index}")
print(f"Найменше значення: {min_number}, індекс: {min_index}")