# Can only be 5 or lower half of 6 digits at most, any more and the sum of digits cannot possibly reach the target

total = 0
for num in range (2, 500000):
    temp = str(num)
    current = 0
    for char in temp:
        current += int(char) ** 5
    if current == num:
        print(current)
        total += current
print(total)