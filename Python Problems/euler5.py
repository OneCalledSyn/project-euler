# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 5, 7, 2^3, 3^2 is the prime factorization for 1-10 


#Brute force
lcm = 1

while (lcm %  2 != 0 or lcm %  3 != 0 or lcm %  4 != 0 or lcm %  5 != 0 or
         lcm %  6 != 0 or lcm %  7 != 0 or lcm %  8 != 0 or lcm %  9 != 0 or
         lcm % 10 != 0 or lcm % 11 != 0 or lcm % 12 != 0 or lcm % 13 != 0 or
         lcm % 14 != 0 or lcm % 15 != 0 or lcm % 16 != 0 or lcm % 17 != 0 or
         lcm % 18 != 0 or lcm % 19 != 0 or lcm % 20 != 0 )
  lcm += 1       

print(lcm)

#Prime factorization approach

divisors =[2^4, 3^2, 5, 7, 11, 13, 17, 19]
