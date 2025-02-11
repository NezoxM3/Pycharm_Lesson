#1
age = "16"
print("Your age is  " + age + " SM")

#2
human = False
print("Monkeys are funny: " + str(human))

#3
M = N = A = R = "Letter"
print(M)
print(N)
print(A)
print(R)

#4
name = "Max"

print(len(name))
print(name.find("a"))
print(name.capitalize())   #?
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("x"))
print(name.replace("Max","Alex"))
print(name*3)

#5
x = 1 #int
y = 2.0 #float
z = "3" #str

x = float(x)
y = str(y)
z = int(z)

print(x)
print(y)
print(z*3)

#6
name = input("Name:")
age = int(input("Age:"))
height = float(input("Height:"))

print("Hi, " +
      str(name) +
      ". You're "+
      str(age) +
      " and your height is " +
      str(height))

#7
import math
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi)) #Як задалеко від 0
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x,y,z))
print(min(x,y,z))







