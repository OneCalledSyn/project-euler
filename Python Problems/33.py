fractions = []
for i in range(10, 99):
    for j in range(i + 1, 100):
        temp = i / j
        i_char = [char for char in str(i)]
        j_char = [char for char in str(j)]
        
        if "0" in i_char or "0" in j_char:
            continue
        if set(i_char) == set(j_char):
            continue
        
        # if i_char[0] == j_char[0]:
        #     if int(i_char[1]) / int(j_char[1]) == temp:
        #         fractions.append((i,j, temp))
        
        # if i_char[0] == j_char[1]:
        #     if int(i_char[1]) / int(j_char[0]) == temp:
        #         fractions.append((i,j, temp))
        
        if i_char[1] == j_char[0]:
            if int(i_char[0]) / int(j_char[1]) == temp:
                fractions.append((i,j, temp))
        
        # if i_char[1] == j_char[1]:
        #     if int(i_char[0]) / int(j_char[0]) == temp:
        #         fractions.append((i, j, temp))
print(fractions)

# 1 * 1 * 1 * 1 /
# 4 * 5 * 5 * 1
# 1/ 100