import math

def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        j = 2 * i
        while j < n:
            is_prime[j] = False
            j += i
    
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

#print(sieve(1000000))
primes = sieve(1000000)

total = 0

for i in primes:
    allowed = True
    trailing = i / 10
    while trailing:
        if (trailing % 10) % 2 == 0 or (trailing % 10) % 5 == 0:
            allowed = False
            break
        trailing //= 10
    
    if trailing:
        n = len(str(i))
        num = i
        total += 1
        for j in range(n):
            num = (num % 10) * 10 ** (n - 1) + (num // 10)
            if num not in primes:
                print(i)
                print(total)
                total -= 1
                print(total)
                break

print(total)

# def sieve(n):
# 	is_prime = [True]*n
# 	is_prime[0] = False
# 	is_prime[1] = False
# 	is_prime[2] = True
# 	#even numbers except 2 have been eliminated
# 	for i in range(3,int(n**0.5+1),2):
# 		index = i*2
# 		while index < n:
# 			is_prime[index] = False
# 			index = index+i
# 	prime = [2]
# 	for i in range(3,n,2):
# 		if is_prime[i]:
# 			prime.append(i)
# 	return prime

# #sieving prime numbers upto 1 million
# primes = sieve(1000000)

# #counter to count the instances
# counter = 0

# #looping through prime numbers
# for i in primes:
# 	#assuming that there is no 2,4,6,8,5,0 in digits
# 	flag = True
# 	#start with tens digit
# 	number = i/10
# 	#looping through digits
# 	while number:
# 		if (number%10) % 2 == 0 or (number%10)%5 == 0:
# 			flag = False
# 			break
# 		number //= 10
# 	#check if flag is true or false
# 	if flag:
# 		length = len(str(i))
# 		number = i
# 		#assume that the circular permutations are prime
# 		counter += 1
# 		#loop to create circular permutations
# 		for j in range(length):
# 			number = (number%10)*10**(length-1)+number//10
# 			#if any permutation is not prime
# 			if number not in primes:
# 				#subtract one from counter
# 				counter -= 1
# 				break

# #print the number of instances
# print(counter)


