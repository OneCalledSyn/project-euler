import math

total = 0

for i in range(23, 101):
    for j in range(2, i - 1):
        if math.comb(i,j) > 1000000:
            if i % 2 == 1:
                total += ((i // 2) - j + 1) * 2
            else:
                total += (((i // 2) - j + 1) * 2) - 1
            break

print(total)