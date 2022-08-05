total = 0

for i in range(1, 10000001):
    curr = i
    while True:
        summand = 0
        for char in str(curr):
            summand += int(char) ** 2
        curr = summand #[sum(int(x)) for x in str(curr)]

        if curr == 89:
            total += 1
            break
        if curr == 1:
            break

print(total)