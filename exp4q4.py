# 4. Write a program to find the sum of digits of a positive integer

num = int(input("Enter a positive integer: "))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print("Sum of digits:", sum)