# 7) WAP to reverse a string

def reverse_string(s):
	return s[::-1]

text = input("Enter a string: ")
result = reverse_string(text)
print("Reversed string is: ", result)