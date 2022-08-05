# First calculated by hand, then solved using math
# Notice that for x^n to have n digits, then 10^n-1 <= x^n < 10^n
# When does 10^n-1 'catch up' to x^n? Set them equal and solve for n
# n = 1 / 1 - log x

import math

total = 0

for i in range(1, 10):
    total += int(1 / (1 - math.log(i, 10)))

print(total)