# 5- WRITE A PROGRAM TO INPUT TWO NUMBERS, SWAP THEM USING 3RD VARIABLE 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
