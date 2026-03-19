# 3- Write a program to input 3 coefficient values and find the real roots.

import math
a = float(input("Enter Coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b*b - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Two distinct real roots ")
    print("Root 1 = ", r1)
    print("Root 2 = ", r2)
elif d == 0:
    r1 = -b / (2*a)
    print("Two equal real Roots")
    print("Root = ", r1)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex roots")