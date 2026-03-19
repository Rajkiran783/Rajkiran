# 1) generate fibonaci series between 0 to 1000. Then find the sum of even valued terms

a, b = 0, 1
even_sum = 0
while a <= 1000:
    if a % 2 == 0:
        even_sum += a
    a, b = b, a + b
print("sum of even-valued fibonaci terms", even_sum)