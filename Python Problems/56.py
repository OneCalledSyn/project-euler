import math

best = 0
num = ""
first = 0
second = 0

for a in range(50, 100):
    for b in range(50, 100):
        current = 0
        res = str(a ** b)
        #res = str(int(math.pow(a, b))) <- This causes some rounding error that causes an incorrect answer of 978
        #print(res)
        for char in res:
            current += int(char)
        if current > best:
            best = current
            num = res
            first = a
            second = b

print(best)
print(first,second)
print(num)
