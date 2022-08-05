def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]
current = 3

while True:
    if is_prime(current):
        primes.append(current)
        
    else:
        flag = True
        while flag == True:
            for p in primes:
                square, total = 1, 0
                while total <= current:
                    total = p + 2 * square ** 2
                    if total == current:
                        flag = False
                        break
                    square += 1
            print(current)
            
    current += 2