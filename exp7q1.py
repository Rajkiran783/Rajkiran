# 1) WAP to create a list containing natural numbers from m to n where m and n given input (create using for loop). Find the sum, average, largest, smallest in the list. Create another list which contains all the numbers of list except no disble by 3.

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
lst = []
for i in range(m, n + 1):
    lst.append(i)

print("List:", lst)

sum = 0
for x in lst:
    sum = sum + x

avg = sum / len(lst)
print("sum :", sum)
print("Average :", avg)
print("Largest :", max(lst))
print("smallest :", min(lst))

new_lst = []
for x in lst:
    if x % 3 != 0:
        new_lst.append(x)

print("List without numbers divisible by 3 :", new_lst)