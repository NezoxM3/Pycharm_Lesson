#Функція
def avg():
   print('Average Grade Calculator')

#Список в який ми будемо добавляти оцінки
grades = []

#Повторення коду, поки його не зупинити
while True:
   grade=input('Enter grade (or "stop"):')
   if grade=='stop':
     break
   grades.append(float(grade))
   avg=sum(grades)/len(grades)
   print('Average grade:',avg)
   if avg >= 90:
     print('Excellent')
   elif avg >= 75:
     print('Good')
   else:
     print('Needs Improvement')

#Запуск функції
avg()
