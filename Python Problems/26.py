# def cycle(denom,num=1):
#     digit = None
#     decimals=[]
#     while digit not in decimals:
#         decimals += [digit]
#         digit = num * 10 // denom
#         remainder = num * 10 - digit * denom
#         num = remainder
#         print(digit)
#     return len(decimals) - decimals.index(digit)

# for i in range(1000, 1, -1):
#     if longest >= i:
#         break



# def sieve(n):
#     sieve = [True] * n // 2
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if sieve[i // 2]:
#             sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (i * 2) + 1)
#     return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

# def longestCycle(n):
#     if n <= 7:
#         return 3
#     for i in sieve(n)[::-1]:
#         k = i // 2
#         while pow(10, k, i) != 1:
#             k += 1
#         if i - 1 == k:
#             return i

# print(longestCycle(1000))


def cycle_count(n):
    digits = []
    cycle_not_found = True
    remainder = 1
    
    while cycle_not_found  and remainder != 0:
        digits.append(remainder)
        remainder = (remainder * 10) % n
        if remainder in digits: 
            cycle_not_found = False
    
    if remainder == 0:
        return 0
    
    else:
        return len(digits[digits.index(remainder):])

longest = 0
for i in range(2, 1000): 
    if longest < cycle_count(i): 
        longest = i
print(longest)

# Full reptend prime: A prime p is full reptend iff 10 is a primitive root modulo p (10^k congruent to 1 mod p for
# k = p - 1 and no lesser k)

# Suffix tree
# Long division