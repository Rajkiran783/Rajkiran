# 8. WAP to enter two numbers nd swap them using bitwise operators. 

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
a=a^b
b=a^b
a=a^b
print("after convesion the value of a:",a)
print("after convesion the value of b:",b) 