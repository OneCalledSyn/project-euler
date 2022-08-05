def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
truncatable = []
naughty = {0, 2, 4, 6, 8, 5}
num = 11

while count < 11 and num <1000000:
    print(count, num, len(truncatable))
    if is_prime(num):
        l = len(str(num))
        temp = str(num)
        for i in range(l - 1):
            #print(temp[i+1:], temp[:(l - 1 - i)])
            if not is_prime(int(temp[i+1:])) or not is_prime(int(temp[:l - 1 - i])):
                break
            if i == l - 2:
                count += 1
                truncatable.append(num)
    num += 2

print(truncatable, sum(truncatable))