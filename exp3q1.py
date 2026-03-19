# 1- Write a program to test a string is palindrome or not.

s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is a palindrome") 
else: 
    print("The string is Not a palindrome")