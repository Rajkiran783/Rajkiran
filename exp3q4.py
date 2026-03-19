# 4- Write a program to input an alphabet and check whether it is vowel or consonant.

ch = input("Enter an alphabet: ")
if ch in 'aeiou AEIOU':
    print("vowel")
else:
    print("Consonant")