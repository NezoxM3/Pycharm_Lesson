#Task 1
def text():
    text1 = "Don't let the noise of others opinions \n drown out your own inner voice.\n\t\t\t\t\t\t\t\tSteve Jobs\n"
    print(text1)

text()

#Task 2
def odd(num1, num2):

    print(f"Непарні числа між {num1} і {num2}:", end=" ")
    for num in range(num1 + 1, num2):
        if num % 2 != 0:
            print(num, end=" ")

odd(1, 20)

#Task 3
#Task 4
def max_number(first, second, third, fourth):
    return max(first, second, third, fourth)

max_numbers = max_number(3, 9, 7, 2)
print(f"\n\nМаксимальне число між 3, 9, 7, 2 є число {max_numbers}\n")

#Task 1(1)
def temp(celsius):
    fahrenheit = (celsius * (9/5) + 32)
    return fahrenheit

celsius = -5
fahrenheit = temp(celsius)
print(f"{celsius}C дорівнює {fahrenheit}F\n")

#Task 2(1)
def work_hour(hour):
    if 9 <= hour < 18:
        return True
    return False

hour = 15
if work_hour(hour):
    print(f"Зараз робочий час({hour}:00)\n")
else:
    print(f"Зараз не робочий час({hour}:00)\n")
#Task 3(1)
def minute_hour(minutes):

    if minutes < 0:
        return "Кількість хвилин не може бути від'ємною!\n"

    hours = minutes // 60
    minutes_ = minutes % 60
    return f"{minutes} хвилин = {hours} годин(и) і {minutes_} хвилин."

print(minute_hour(254))
