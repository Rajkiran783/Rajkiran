# 6. Write a program to test a number is palindrome or not

num = int(input("Enter a number: "))
original_num = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original_num == reverse:
    print(original_num, "is a palindrome")
else:
    print(original_num, "is not a palindrome")