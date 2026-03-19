# 2. Write a program to test a number is prime or not

num = int(input("Enter a number: "))
if num == 1:
    print("Not a prime number")
else:
    i = 2
    prime = True
    while i <= num // 2:
        if num % i == 0:
            prime = False
            break
        i = i + 1
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")