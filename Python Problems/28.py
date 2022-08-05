# 1 3 13 31

#Lower right diag
 
step_LR = 2
total_LR, current_LR = 1, 1

for i in range(500):
    current_LR += step_LR
    total_LR += current_LR
    step_LR += 8

print(total_LR)

step_LL = 4
total_LL, current_LL = 1, 1

for i in range(500):
    current_LL += step_LL
    total_LL += current_LL
    step_LL += 8

print(total_LL)

step_UL = 6
total_UL, current_UL = 1, 1

for i in range(500):
    current_UL += step_UL
    total_UL += current_UL
    step_UL += 8

print(total_UL)

step_UR = 8
total_UR, current_UR = 1, 1

for i in range(500):
    current_UR += step_UR
    total_UR += current_UR
    step_UR += 8

print(total_UR)

# The initial value 1 is counted in all 4 loops, so subtract 3 to correct for this
print(total_LR + total_LL + total_UL + total_UR - 3)


# For a 2n+1 by 2n+1 square, the sum of the diagonals is

# 8n(n+1)(2n+1)/3 + 2n(n+1) + 4n + 1