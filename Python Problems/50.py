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
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

primes = sieve(1000000)

best, length = 0,0
limit = len(primes)

for i in range(len(primes)):
    for j in range(i + length, limit):
        current = sum(primes[i:j])
        if current < 1000000:
            if current in primes:
                length = j - i
                best = current
        else:
            limit = j + 1
            break
print(best)
# for num in candidates:
#     current += num
#     length += 1
#     if current >= 1000000:
#         break
#     if length > longest and current in candidates:
#         best,longest = current, length
        
# print(best)

# Too slow to be comprehensively used
# for i in range(5000, 5500):
#     current = 0
#     for num in candidates[i:]:
#         current += num
#         if current >= 1000000:
#             break
#         if current in candidates:
#             best = current
# print(best)