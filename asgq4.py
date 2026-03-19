# 4.WAP to enter the coefficients of a quadratic equation and findout the roots of the equivalent

import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=math.sqrt(b*b)-(4*c*a)
x=(-b+d)/(2*a)
y=(-b-d)/(2*a)
print("the roots are:",x,"&",y)
