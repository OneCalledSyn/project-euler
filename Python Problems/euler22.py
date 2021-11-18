score = 0

with open('p022_names.txt', 'r') as f:
    names = f.read()

names = names.split(',')

names = [x[1:-1] for x in names]

names.sort()

def calculate_score(name):
    values = [ord(x) - 64 for x in list(name)]
    return sum(values)


for i in range(len(names)):
    score += calculate_score(names[i]) * (i+1)

print(score)
