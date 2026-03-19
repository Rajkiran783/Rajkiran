# 7- WRITE A PROGRAM TO FIND THE AREA AND PERIMITER OF A TRINGLE 

x = float(input("Enter side a : "))
y = float(input("Enter side b : "))
z = float(input("Enter side c : "))
perimiter = x + y + z
s = perimiter / 2
area = (s*(s-x)*(s-y)*(s-z))**0.5
print("Area of the triangle:", area)
print("Perimiter of the triangle:", perimiter)