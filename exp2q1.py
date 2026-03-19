# 1- DISPLAY SIMPLE INTREST AND COMPOUND INTREST

p=float(input("enter the principal amount:"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the time period:"))
simple_intrest=(p*r*t)/100
ammount=p*pow((1+(r/100)),t)
compound_intrest=ammount-p
print("the simple intrest is:",simple_intrest)
print("the compound intrest is:",compound_intrest)