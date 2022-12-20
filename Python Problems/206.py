import math

num = 1000000000
lower = int(math.sqrt(1020304050607080900))
upper = int(math.sqrt(1929394959697989990))

for num in range(lower, upper, 10):
    print(num, str(num ** 2)[0:20:2])
    if str(num ** 2)[0:20:2] == "1234567890":
        break
    num += 100