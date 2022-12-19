import math

f = open('p099_base_exp.txt')
lines = f.read().splitlines()
base = [int(x.split(',')[0]) for x in lines]
exponent = [int(x.split(',')[1]) for x in lines]

#print(lines)
#print(base)
#print(exponent)

largest = 0
best_line = 0

for i in range(len(base)):
    curr = exponent[i] * math.log(base[i])
    if curr > largest:
        largest = curr
        best_line = i + 1

print(best_line)
