#3 WAP to check whether a no is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        print("The no is even")
    else:
        print("The no is odd")

n = int(input("enter a no "))
check_even_odd(n)