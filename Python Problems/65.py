prev = 3
numer = 8
step = 4
factor = 4

while step < 101 :
    print(numer)
    if step % 3 == 0:
        numer, prev = prev + factor * numer, numer
        factor += 2
    else:
        numer, prev = numer + prev, numer
    
    step += 1

print(numer)

total = 0

for char in str(numer):
    total += int(char)

print(total)