# 7. Generate a Fibonacci series

n = int(input("Enter number of terms: "))
a = 0
b = 1
count = 0
print("Fibonacci series:")
while count < n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
    count += 1