# 1479 is the first number to produce a chain of length 60. 
# Since 0 and 1 have the same factorial value of 1, 4079 also has a chain of length 60. 
# There are no other four digit combinations that result in a chain of length 60. 
# There are no five digit results. The first six digit result is 223479. 
# Thus all permutations of this number have a chain of length 60. 
# There are no other six digit results. 
# Doing the math we get: 4! + 3*3! + 6!/2 = 402

#Brute force below

import math

total = 0 

for i in range(1, 1000000):
    chain = set()
    start = i
    counter = 1
    curr = str(i)
    
    while counter < 62:
        
        value = 0
        
        for char in curr:
            value += math.factorial(int(char))
        
        if value not in chain:
            chain.add(value)
            counter += 1
            
            if counter == 60:
                total += 1
                #print(i, value, counter)
        
        else:
            #print(i, value,counter)
            break
        
        curr = str(value)

print(total)