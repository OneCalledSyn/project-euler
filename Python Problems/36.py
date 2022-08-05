pal_10 = [num for num in range(1, 1000001) if str(num) == str(num)[::-1]]
pal_both = [num for num in pal_10 if bin(num)[2:] == (bin(num)[2:])[::-1]]
print(pal_10)
print(pal_both, sum(pal_both))