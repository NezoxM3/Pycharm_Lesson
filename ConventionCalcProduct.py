#Функція
def calculate_products():
  print('Shopping Calculator')

#Список
shopping_list = []

#Повторення коду, поки його не зупинити
while True:
  product=input('Enter product name or "done":')
  if product=='done':
   break
  cost=float(input('Enter price:'))
  shopping_list.append((product,cost))
  total = 0
  print('Your products:')
  for i in shopping_list: print(i[0],' - ',i[1]);
  total += i[1]
  print('Total:',total)

#Запуск функції
calculate_products()
