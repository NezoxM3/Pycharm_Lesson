#Завдання 1
try:
    name = input("Введіть ваше ім'я:")
    age = int(input("Введіть ваш вік:"))


    if age < 0 or age > 130:
        raise ValueError("Вік потрібно написати в діапазоні від 0 до 130")

    print(f"Привіт, {name}! Твій вік — {age}")

except ValueError as e:
    print(f"Error: {e}")

#Завдання 2
print("`''`'``'`'`'`'`'`'`'`'`'`'`'`''``'`''`'``'`''`")
print()

def greetings(name1, age1):
    if age1 < 0 or age1 > 130:
        raise ValueError("Вік потрібно написати в діапазоні від 0 до 130")
    return f"Привіт, {name1}! Твій вік — {age1}"

try:
    result = greetings(name1="Max", age1=2)
    print(result)
except ValueError as e:
    print(f"Помилка: {e}")

#Завдання 3-4
print()
print("`''`'``'`'`'`'`'`'`'`'`'`'`'`''``'`''`'``'`''`")

def collect_positive_numbers():
    numbers = []
    print("Введіть додатні числа. Для завершення введіть 'stop'.")

    while True:
        try:
            user_input = input("Введіть число: ")
            if user_input.lower() == 'stop':
                break

            number = float(user_input)
            if number <= 0:
                raise ValueError("Введіть додатнє число ")

            numbers.append(number)
        except ValueError as e1:
            print(f"Помилка: {e1}. Спробуйте ще раз.")

    return numbers


def analyze_numbers(numbers):
    try:
        if any(num <= 0 for num in numbers):
            raise ValueError("У списку є недодатні числа.")
        return sum(numbers)
    except ValueError as e2:
        print(f"Помилка: {e2}")
        return None


def main():
    numbers = collect_positive_numbers()
    print("Список чисел:", numbers)

    result = analyze_numbers(numbers)
    if result is not None:
        print(f"Сума всіх чисел: {result}")

main()

print()
print("`''`'``'`'`'`'`'`'`'`'`'`'`'`''``'`''`'``'`''`")
