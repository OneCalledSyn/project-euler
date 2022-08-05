with open('../Desktop/67.txt') as file:
    lines = file.readlines()

n = len(lines)

for i in range(n):
    lines[i] = lines[i].replace('\n', '').split()
print(lines)

for j in range(n - 1, 0, -1):
    for k in range(0, j):
        lines[j - 1][k] = int(lines[j - 1][k]) + max(int(lines[j][k]), int(lines[j][k + 1]))

print(lines[0][0])