# If both a and b are even, c will also be even and P (the perimeter) will be even.
# If both a and b are odd, c will be even and P will be even.
# If one is even and the other is odd, c will be odd and P will again be even.
# Therefore, only even values of P need to be checked.

best, value = 0, 0

for perimeter in range (4, 1001, 2):
    current = 0
    a_max = perimeter - 2
    for a in range(1, a_max):
        b_max = perimeter - a - 2
        a_squared = a ** 2
        for b in range(a, perimeter - a - 2):
            print(a, b, perimeter)
            if (a_squared) + (b ** 2) == (perimeter - a - b) ** 2:
                current += 1
    if current > best:
        best = current
        value = perimeter

print(best, value)
