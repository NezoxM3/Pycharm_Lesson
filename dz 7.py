#Завдання 1
#start = int(input("Введіть перше число:"))
#end = int(input("Введіть друге число:"))
#
#for i in range(start, end+1):
#    if i % 7 == 0:
#        print("Кратне семи")
#    else:
#        print(i)

#Завдання 2
#start = int(input("Введіть перше число:"))
#end = int(input("Введіть друге число:"))

#five_counter = 0

#print("Всі числа діапазону:")
#for i in range(start, end + 1):
#    print(i)

#    if i % 7 == 0:
#       print("Кратне семи")
#    elif i % 5 == 0:
#        five_counter += 1

#for i in range(end, start - 1, -1):
#    print(i)
#print("Кратних 5 є",five_counter)

#Завдання 3
start = int(input("Введіть перше число:"))
end = int(input("Введіть друге число:"))

for i in range(start, end+1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)






