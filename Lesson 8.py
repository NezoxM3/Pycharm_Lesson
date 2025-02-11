
start = 1
end = 50

for i in range(start, end+1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)




















#start = 2
#end = 15
#sum = 0
#count = 0

#for i in range(start,end+1):

#    sum += i
#    count += 1
#    sered = sum / count

#    print(f"i = {i}")
#    print(f"sum = {sum}")
#    print(f"count = {count}")
#    print(f"середнє арифметичне = {sered}")