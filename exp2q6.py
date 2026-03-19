# 6- WRITE A PROGRAM TO CREATE A DISCTIONARY , STORE SIMPLE DATA AND MEDIXPLAY THE KEY, VALUE OF IT.

student = {"name": "Subrat", "age": 19, "branch": "CSEAIML", "city": "Gunupur"}
print("disconary :", student)
print("\nKeys :")
for key in student.keys():
    print(key)
print("\nValues :")
for value in student.values():
    print(value)
print("\nItems :")
for item in student.items():
    print(item)