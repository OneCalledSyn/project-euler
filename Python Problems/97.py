import timeit

# Stupid brute force only takes about 2 minutes in Python
# String conversion is the bulk of the computational time
# Time: 122.16862309999851 sec

# print(timeit.timeit('print(str(((2**7830457) * 28433) + 1)[-10:])', number = 1))

# Much better brute force
# Time: 0.07002359999751206 sec

print(timeit.timeit('print((((2**7830457) * 28433) + 1) % 10000000000)', number = 1))

# https://www.exploringbinary.com/patterns-in-the-last-digits-of-the-positive-powers-of-two/
# Idea: For k trailing digits, there is a cycle with period 4 * (5 ^ (k - 1))
# For k = 10, the period is 4 * 5**9 = 7812500
# Time: 0.0002223999981652014 sec

print(timeit.timeit('print((2**(7830457 % 7812500) * 28433 + 1) % 10000000000)', number = 1))

def PE97(a, b, c, m):
    return (c * pow(a, b, m) + 1) % m

# Time: 1.400003384333104e-06 sec
print(timeit.timeit('def PE97(a, b, c, m): return (c * pow(a, b, m) + 1) % m; print(PE97(2, 7830457, 28433, 10**10))', number = 1))