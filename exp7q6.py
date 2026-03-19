# 6) WAP to check whether a no is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("enter a no: "))
if is_prime(n):
    print("The no is prime")
else:
    print("The no is not prime")