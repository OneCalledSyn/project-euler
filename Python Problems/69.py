def rel_primes(n):
    rels = set()
    rels.add(1)
    factors = set()
    limit = int(n ** 0.5) + 1
    for i in range(1, limit):
        if n % i == 0:
            factors.add(i)
            factors.add(n / i)
    #print(factors)
    for i in range(2, n):
        flag = True
        for num in factors:
            if num % i == 0:
                flag = False
                break
        if flag:
            rels.add(i)
    #print(rels)
    totient = len(rels)
    print(factors, rels, n/totient)
    return (n / totient)

current, best = 0,0
for i in range (2, 11):
    current = rel_primes(i)
    if current > best:
        best = current
print(best)

# Paper and pencil
# Just multiply primes until it would overflow past one million
# 2*3*5*7*11*13*17 = 510510
# https://www.mathblog.dk/project-euler-69-find-the-value-of-n-≤-1000000-for-which-nφn-is-a-maximum/