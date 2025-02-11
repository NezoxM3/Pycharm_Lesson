#Функція
def sal():
  print('Salary Tax Calculator')

#Вводемо зарплату і підраховуємо податки
salary=float(input('Enter gross salary:'))
tax = 0.18 if salary < 20000 else 0.22
net=salary-salary*tax
print('Net salary:',net)

#Запуск функції
sal()
