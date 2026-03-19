# 2. WAP to create a dictionary and input keys and values. Then create another dictionary which collects the values of 1st dictionary as keys and keys of dictionary as values and then display both dictionarys

d1 = {}
n = int(input("Enter number of elements: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

d2 = {}
for k, v in d1.items():
    d2[v] = k

print("original Dictionary", d1)
print("Reversed Dictionary", d2)