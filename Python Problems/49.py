import itertools

def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index += i
    primes = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)
    return primes

candidates = sieve(10000)
candidates = [x for x in candidates if x > 1000]
#print(candidates)

def helper(candidate):
    length = len(candidate)
    for i in range(length):
        for j in range(i + 1, length):
            diff = candidate[j] - candidate[i]
            if candidate[j] + diff in candidate:
                return str(candidate[i]) + str(candidate[j]) + str(candidate[j] + diff)
    return False

for i in candidates:
    perms = itertools.permutations(str(i))
    perms_as_int = [int(''.join(x)) for x in perms]
    cleaned_perms = sorted(list(set([x for x in perms_as_int if x in candidates])))

    if len(cleaned_perms) >= 3:
        if helper(cleaned_perms) and helper(cleaned_perms) != "148748178147":
            print(helper(cleaned_perms))
            break
            