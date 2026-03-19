# 4. WAP to create an empty list and input a group of numbers into the list, remove the duplicate elements from it and then sort them in ascending order and then display.
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter numbers: ")))
numbers = list(set(numbers))
numbers.sort()
print("sorted list without duplicates:", numbers)