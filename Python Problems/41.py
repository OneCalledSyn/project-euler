import itertools

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

# Notice that there cannot be a 9-digit or 8-digit pandigital number
# The sum 1+2+3+4+5+6+7+8+9 = 45 and the sum 1+2+3+4+5+6+7+8 = 36 are both divisible by 9
perms = sorted(itertools.permutations([1,2,3,4,5,6,7]), reverse=True)

for item in perms:
    temp = ""
    for elt in item:
        temp += str(elt)
    if is_prime(int(temp)):
        print(temp)
        break
