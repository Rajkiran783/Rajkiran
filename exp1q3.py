# 3- WRITE A PROGRAM TO IFND AREA AND PERIMITER OF A CIRCLE

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)
print("radius of the circle:", radius)