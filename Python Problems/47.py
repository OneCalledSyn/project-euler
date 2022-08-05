def factor_finder(n):
    divisor = 2
    factors = set()

    while divisor < n ** 0.5 or n == 1:
        #print(divisor)
        if n % divisor == 0:
            n /= divisor
            factors.add(divisor)
            divisor -= 1
        divisor += 1
    return len(factors) + 1

current = 2 * 3 * 5 * 7

while current < 200000  :
    #print(current)
    if factor_finder(current) == 4:
        current += 1
        if factor_finder(current) == 4:
            current += 1
            if factor_finder(current) == 4:
                current += 1
                if factor_finder(current) == 4:
                    print (current - 3)
                    break
    current += 1
