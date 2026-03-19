# 1. WAP to create a list which contains some group of fruit names. Display the elements of the list from last index to 1st index and also show the length of each element. Create another list which collects the reverse of each element

foods = ["pizza", "burger", "pasta", "rice"]
for item in foods[::-1]:
    print(item, len(item))
keywords = [item[::-1] for item in foods]
print("keywords:", keywords)