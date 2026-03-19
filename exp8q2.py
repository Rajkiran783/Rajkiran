# Question: WAP to generate all prime numbers within a given range from m to n.

M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))
print("Prime numbers between", M, "and", N, "are:")

for num in range(M, N+1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")