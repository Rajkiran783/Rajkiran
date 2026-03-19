# 2. write a program that loops over a sequence of elements of a list, tuple, dictionary and set.

lst = [1, 2]
tup = (3, 4)
dic = {'a': 5, 'b': 6}
st = {7, 8}

for i in lst:
    print(i)
for i in tup:
    print(i)
for k, v in dic.items():
    print(k, v)
for i in st:
    print(i)