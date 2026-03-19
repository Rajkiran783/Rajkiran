# 5) WAP to find the factorial of a no

def factorial(n):
	fact = 1
	for i in range(1, n + 1):
		fact = fact * i
	return fact

num = int(input("Enter a no "))
print("factorial =", factorial(num))