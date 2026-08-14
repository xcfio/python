# SQ2
a = 1
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print("Cant devide with 0")

# Q1
age = int(input("Enter your age: "))
if age < 18:
    raise Exception("You are not allowed here")
