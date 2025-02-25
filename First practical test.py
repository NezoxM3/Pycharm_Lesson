#1. Змінні, типи даних, рядки (10 хв)

name = (input("Ваше і'мя:"))
salary_per_hour = (float(input("Ваша зарплата в годину:")))
hours_worked = (int(input("Скільки ви годину сьогодні відпрацювали:")))

earned_salary = salary_per_hour * hours_worked
taxes = earned_salary * 0.8

print(f"{name} сьогодні заробив {taxes} з урахуванням податків")