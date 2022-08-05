import math

curious = []
# The factorion of an n-digit number cannot exceed n·9!
# Factorions could theoretically be 7 digits at most
# Allows supremum of 10,000,000
for i in range(10, 10000000):
    temp = [char for char in str(i)]
    total = 0
    for num in temp:
        total += math.factorial(int(num))
    if total == i:
        curious.append(i)

print(curious, sum(curious))

