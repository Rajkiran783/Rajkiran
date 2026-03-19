# 5- Accept a digit within 0 to 6 and display the week day such as 0 for Sunday, 1 for monday etc..

n = int(input("Enter a digit (0 to 6): "))
if n == 0:
    print("Sunday")
elif n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
else:
    print("Invalid input!")