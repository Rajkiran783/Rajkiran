# 3. Write a program to input a sentence. Store each word as element in into a list1. Now Display the element of list along with its index (using enumerate()). Create another list2 having elements as a series of numbers. Now use zip() to combine the elements of both lists to create a 3rd list and display it

sentence = input("Enter a sentence: ")
list_one = sentence.split()

print("List one with index: ")
for index, word in enumerate(list_one):
    print(index, word)

list_two = list(range(1, len(list_one) + 1))
list_three = list(zip(list_one, list_two))

print("combined list: ")
print(list_three)