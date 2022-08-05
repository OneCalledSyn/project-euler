total = 0
numer = 1
denom = 2

for i in range(1000):
    numer, denom = denom, numer + (denom * 2) 

    if len(str(numer + denom)) > len(str(denom)):
        total += 1

print(total)
