import math

print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Power of number \n")

amal = int(input("Which mathematic action do you want?: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if amal == 1:
  print(a, "+" ,b, "=", (a+b))

elif amal == 2:
  print(a, "-", b, "=", (a - b) )

elif amal == 3:
  print(a, "X", b, "=", (a*b))

elif amal == 4:
  print(a, "÷", b, "=", (a/b))

elif amal == 5:
  print(a, "^", b, "=", math.pow(a,b))

else:
  print("Enter number 1 to 5!")