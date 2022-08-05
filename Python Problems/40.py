# Pencil and paper method:

# 1-9:  9 digits * 1 = 9 digits
# 10-99: 90 digits * 2 = 180 digits
# 100-999: 900 digits * 3 = 2,700 digits
# 1000-9,999: 9,000 digits * 4 = 36,000 digits
# 10,000-99,999: 90,000 digits * 5 = 450,000 digits
# 100,000-999,999: 900,000 digits * 6 = 5,400,000 digits

# d1 =  1
# d10 = (10 - 9) // 2 = 1 number, 9 + 1 = 10, remainder 1 so 10th digit is the first digit in 10: 1
# d100 = (100 - 9) // 2 = 45 numbers, 9 + 45 = 54, remainder 1 so 100th digit is the first digit in 55: 5
# d1000 = (1,000 - 180 - 9) // 3 = 270 numbers, 99 + 270 = 369, remainder 1 so 1000th digit is the first digit in 370: 3
# d10000 = (10,000 - 2700 - 180 - 9) // 4 = 1777 numbers, 999 + 1777 = 2776, remainder 3 so 10000th digit is third digit in 2777: 7
# d100000 = (100,000 - 36,000 - 2,700 - 180 - 9) // 5 = 12222 numbers, 9999 + 12222 = 22221, remainder 1 so 100000th digit is first in 222222: 2
# d1000000 = (1,000,000 - 450,000 - 36,000 - 2,700 - 180 -9) // 6 = 85185 numbers, 99999 + 85185 = 185184, remainder 1 so 1mth is first in 185185: 1
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000 = 1 * 1 * 5 * 3 * 7 * 2 * 1 = 210

# Brute force programming:

champ = ''
for num in range(1, 185186):
    champ += str(num)
prod = int(champ[0]) * int(champ[9]) * int(champ[99]) * int(champ[999]) * int(champ[9999]) * int(champ[99999]) * int(champ[999999])
print(prod, champ[0], champ[9], champ[99], champ[999], champ[9999], champ[99999], champ[999999])