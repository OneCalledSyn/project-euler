# n^2 + an + b must be prime for consecutive values of n, starting at n = 0
# a and b remain fixed for all the values of n

# n = 0: 0 + 0 + b must be prime, therefore b must always be prime
# n = 1: 1 + a + b must be prime, therefore b+1 is composite, so a must be odd unless b is 2
# This allows the search space of a to be halved and the search space of b to be decimated
# A less restrictive but easier approach for b would also be just searching positive odd numbers to avoid making a sieve

# construct list of primes to look through for b
#primes = [True] * 1000

def isPrime(n):
    if n == 2 or n == 3:
        return True
    for i in range(3, int(abs(n) ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

#search odd values of a and positive odd values of b
longest = 0
bestA = 0
bestB = 0

for a in range(-999, 1000, 2):
    for b in range(3, 1000, 2):
        current, n = 0, 0
        while True:
            #print(current, n)
            prod = (n ** 2) + (a * n) + b
            if not isPrime(prod):
                if current > longest:
                    longest = current
                    bestA, bestB = a, b
                break
            n += 1
            current += 1

print(longest, bestA, bestB, bestA * bestB)      
            
# Math note: If p(x) is prime-generating for 0 <= x <= n, then so is p(n - x)
# Thus we can transform Euler's formula of n^2 - n + 41 which produces primes for n = 0...40
# Into (n - 40) ^ 2 - (n - 40) + 41 which is equivalent to n^2 - 79n + 1601, which gives primes for 80 consecutive integers
# Thus for this problem, we can do (n - p) ^ 2 + (n - p) + 41, giving |2p - 1| < 1000 and |p^2 - p + 41| < 1000
# Second condition reduces to -30 <= p <= 31, p = 31 will generate the most primes
# We get a = -(2 * 31 - 1) = -61 and b = (31 ^ 2) - 31 + 41 = 971 for a product of -59231 and 71 primes from n = 0...70