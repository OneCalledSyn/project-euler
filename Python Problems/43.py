# pandigital = []
# digits = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# for num in range(1023456797, 9876543210, 17):
#     print(num)
#     temp = [char for char in str(num)]
#     if set(temp) == digits:
#         if int(temp[6:9]) % 13 == 0:
#             if int(temp[5:8]) % 11 == 0:
#                 if int(temp[4:7]) % 7 == 0:
#                     if int(temp[3:6]) % 5 == 0:
#                         if int(temp[2:5]) % 3 == 0:
#                             if int(temp[1:4]) % 2 == 0:
#                                 pandigital.append(num)
#     continue
# print(pandigital, sum(pandigital))


# div_17 = []
# for i in range(123, 988):
#     if i % 17 == 0:
#         temp = {}
#         for char in str(i):
#             if char not in temp:
#                 temp.add(char)
#                 if 
            
                
#             div_17.append(i)
# print(div_17)

import itertools

perms = itertools.permutations('0123456789')
total = 0

for perm in perms:
    if int(''.join(perm)[7:10]) % 17 == 0 and int(''.join(perm)[6:9]) % 13 == 0 and int(''.join(perm)[5:8]) % 11 == 0 and int(''.join(perm)[4:7]) % 7 == 0 and int(''.join(perm)[3:6]) % 5 == 0 and int(''.join(perm)[2:5]) % 3 == 0 and int(''.join(perm)[1:4]) % 2 == 0:
        total += int(''.join(perm))

print(total)