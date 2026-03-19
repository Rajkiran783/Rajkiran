# 10- WRITE A PROGRAM TO INPUT A STRING "GOOD MORNING FRIENDS HOW ARE YOU ALL" AND TO THE OPERATION : DISPLAY IN NEARER ORDER OF CHERATERS, SPLIT WHOLE SENTANCE INTO INDIVIDUAL WORDX AND STORE AS A LIST.

u = input("enter a sentence:")
new = u[::-1]
print("reversed string:", new)
words = u.split()
print("list of words:", words)
