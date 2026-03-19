# 6- WRITE A PROGRAM TO INPUT YOUR MARKS FOR SUBJECT THEN FIND SUM AND PARCENTAGE

mark_1 = float(input("Enter marks for subject 1: "))
mark_2 = float(input("Enter marks for subject 2: "))
mark_3 = float(input("Enter marks for subject 3: "))
total_marks = mark_1 + mark_2 + mark_3
percentage = (total_marks / 300) * 100
print("Total marks:", total_marks)
print("Percentage:", percentage)