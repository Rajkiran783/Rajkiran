# 8- WAP to count the vowels

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count += 1
    return count

text = input("Enter a string ")
print("no of vowels in the string: ", count_vowels(text))