# 2- Find the greatest among three unequal numbers.

a = int(input("Enter first numbers: "))
b = int(input("Enter second numbers: "))
c = int(input("Enter third numbers: "))
if (a > b and a > c):
    print("Greater number is: ", a)
elif (b > a and b > c):
    print("Greater number is: ", b)
else:
    print("Greater number is: ", c)