def is_snumber(x, y):
    if x == y:
        return True

    t = 10
    while t < y:
        q, r = divmod(y, t)
        if r < x and is_snumber(x - r, q):
            return True
        t *= 10
    
    return False

total = 0
for i in range(4, 10**6 + 1):
    if is_snumber(i, i*i):
        total += i*i

print(total)