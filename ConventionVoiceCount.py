#Функція
def vote():
   print('Voting System')

#Усі лічильники кандидатів ставимо на нуль
candidate1 = 0
candidate2 = 0
candidate3 = 0

#Повторення коду, поки його не зупинити
while True:
   voting=input('Vote for 1, 2, or 3 (or "stop" to end):')
   if voting=='stop':
     print("Voting has ended")
     break
   if voting=='1':
     candidate1 += 1
   elif voting=='2':
     candidate2 += 1
   elif voting=='3':
     candidate3 += 1
   else:
     print('Invalid vote!')
     print('Results:')
     print('1:',candidate1)
     print('2:',candidate2)
     print('3:',candidate1)

#Запуск функції
vote()
