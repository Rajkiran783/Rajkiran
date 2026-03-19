# 9) WAP to find the largest of the nos

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input("enter 1st no "))
y = int(input("enter 2nd no "))
z = int(input("enter 3rd no "))
largest = largest_of_three(x, y, z)