#Функція
def to_do():
  print('To-Do List')

#Список, в який будуть додавтися таски
tasks = []

#Повторення коду, поки його не зупинити
while True:
  action=input('Choose: "add", "done", "view", "exit":')
  if action=='exit':
    print("Closing your to do tasks")
    break
  if action=='add':
    task=input('Enter task:')
    tasks.append((task,False))
  elif action=='done':
    num=int(input('Task number to mark done:'))
    tasks[num]=(tasks[num][0],True)
  elif action=='view':print('Your tasks:')
  for i,t in enumerate(tasks):
    print(i,t[0],'- Done' if t[1] else '- Not Done')

#Запуск функції
to_do()
