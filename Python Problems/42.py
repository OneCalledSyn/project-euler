triangular = set([((n * (n+1)) / 2) for n in range(1, 1000)])
#print(triangular)

total = 0

with open('words.txt', 'r') as f:
    content = f.read()

parsed = content.split(',')
print(parsed)

for word in parsed:
    score = 0
    for char in word:
        if char == '"':
            continue
        score += ord(char) - 64
    if score in triangular:
        total += 1

print(total)