# Question: WAP to create a list containing natural numbers from m to n where m and n are given input. Create using for loop. Find the sum, average, largest and smallest in the list. Create another list which contains all the members of 1st list expect numbers divisible by 2.

M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))
list1 = []

for i in range(M, N+1):
    list1.append(i)

print("List 1:", list1)

total = sum(list1)
print("Sum:", total)

average = total / len(list1)
print("Average:", average)

largest = max(list1)
smallest = min(list1)
print("Largest number:", largest)
print("Smallest number:", smallest)

list2 = []
for num in list1:
    if num % 2 != 0:
        list2.append(num)
print("List 2 (excluding numbers divisible by 2):", list2)