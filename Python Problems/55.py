# First attempt

# total = 0

# for i in range(1, 10000):
#     print(i)
#     counter = 1
#     current = i
#     while counter < 50:
#         current += int(str(current)[::-1])
#         if str(current) == str(current)[::-1]:
#             total += 1
#             break
#         counter += 1

# print(9999 - total)




# Better version

def reverse(n): return int( str(n)[::-1] )

def isLychrel(n):
    for _ in range(50):
        n += reverse(n)
        if n==reverse(n): return 0
    return 1

print(sum(isLychrel(n) for n in range(1, 10000)))