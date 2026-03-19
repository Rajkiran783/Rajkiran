# 2. WAP to enter three sides of a tringle. Find out the area of the tringle. 

import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
s=float((a+b+c)/2)
z=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of tringle is :",z)