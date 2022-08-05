# Slow naive way, works reasonably fast for 1000 but starts to blow up around 10,000

# total = 0

# for i in range(1, 10001):
#     total += i ** i

# print(str(total)[-10:])

# Faster way making use of modular division, instant at 100,000 and still very quick at 1,000,000

def self_power(n):
    mod = 10 ** 10
    total = sum(pow(i, i, mod) for i in range(1, n + 1))
    return total % mod

print(self_power(1000000))