def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

diagonals = 0
primes = 0
l = 1
top_right = top_left = bot_left = 1

for _ in range(100000):
    diagonals += 4

    top_right += (l * 4) - 2
    if is_prime(top_right):
        primes += 1

    top_left += l * 4
    if is_prime(top_left):
        primes += 1
    
    bot_left += (l * 4) + 2
    if is_prime(bot_left):
        primes += 1
    
    #print(top_right, top_left, bot_left, primes, diagonals)
    if primes / diagonals < 0.1: 
        break

    l += 2
    #bot_right diagonal is always a perfect square, so never prime, and thus no need to calculate it
    #but it would be (l * 4) + 4

print(l)


