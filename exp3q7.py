# # 7- Write a program to input marks for 5 subjects, assume maximum marks for each subject is 50. Find percentage and then display grade as below:
# Percentage >= 90 and <= 100 grade is O.
# Percentage >= 80 and <= 90 grade is E.
# Percentage >= 70 and <= 80 grade is A.
# Percentage >= 60 and <= 70 grade is B.
# Percentage >= 50 and <= 60 grade is C.
# Percentage >= 0 and <= 50 grade is F.

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))
total = m1 + m2 + m3 + m4 + m5
Percentage = (total/500)*100
print("Total Marks: ", total)
print("Percentage: ", Percentage)

if Percentage >= 90 and Percentage <= 100:
    print("Grade: O")
elif Percentage >= 80 and Percentage <= 90:
    print("Grade: E")
elif Percentage >= 70 and Percentage <= 80:
    print("Grade: A")
elif Percentage >= 60 and Percentage <= 70:
    print("Grade: B")
elif Percentage >= 50 and Percentage <= 60:
    print("Grade: C")
else:
    print("Grade: F")