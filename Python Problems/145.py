def odd_digits(n):
    while n > 0:
        if n % 2 == 0:
            return False
        n = n // 10
    return True

n = 1000000000
count = 0

for i in range(1, n):
    if i % 10 == 0:
        continue
    final = i + int(str(i)[::-1])
    print(final)
    if odd_digits(final):
        count += 1

print(count)