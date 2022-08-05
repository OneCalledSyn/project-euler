pentagonal = set()
best = 1000000000
for i in range(1, 5000):
    pentagonal.add(i * ((3 * i) - 1) // 2)
print(pentagonal)
for j in pentagonal:
    for k in pentagonal:
        print(j, k)
        distance = abs(j - k)
        if distance < best:
            if (j + k) in pentagonal and distance in pentagonal:
                best = distance
print(best)