best = 0
for num in range (1, 10000):
    current = ""
    multiplier = 1

    while len(current) < 9:
        current += str(num * multiplier)
        multiplier += 1
        print(current)
    if len(current) == 9 and '0' not in current and len(set(current)) == 9:
        if int(current) > best:
            best = int(current)

print(best)