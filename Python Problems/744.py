# Ex 1: 13 envelopes, 50% chance expert is right, 6 points to win
# First pull: 1/13 chance to halt, 12/13 to continue, 0% to win
# Second pull: 1/12 chance to halt, 11/12 to continue, 0% to win
# Third pull: 1/11 chance to halt, 10/11 to continue, 0% to win
# Fourth pull: 1/10 chance to halt, 9/10 to continue, 0% to win
# Fifth pull: 1/9 chance to halt, 8/9 to continue, 0% to win
# Sixth pull: 1/8 chance to halt, 7/8 to continue, 2 * 1(this is 6 choose 0) * 0.5^6 or 3.125% chance to win 
# (64 possible arrangements of points, 2 ways to win, audience or experts 6-0)
# Seventh pull: 1/7 chance to halt, 6/7 to continue, 2 * 6(this is 6 choose 1) * 0.5^6 * 0.5^1 or 9.375% chance to win
# (Can only win 6-1 either way, but there are 6 different spots the one loss can be in 
# For the nth round there are n-1 spots the loss can be present in since have to win final point
#  Eighth pull: 1/6 chance to halt, 5/6 to continue, 2 * 21(this is 7 choose 2) * 0.5^6 * 0.5^2 or 16.40625% chance to win
# Ninth pull: 1/5 chance to halt, 4/5 to continue, 2 * 56(this is 8 choose 3) * 0.5^6 * 0.5^3 or 21.875% chance to win
# Tenth pull: 1/4 chance to halt, 3/4 to continue, 2 * 126(9 choose 4) * 0.5^6 * 0.5^4 or 24.609375% chance to win
# Eleventh pull: 1/3 chance to halt, 2/3 chance to continue, win is guaranteed if 2n - 1 pulls occur when n points are needed to win
# (12/13) * (11/12) * (10/11) * (9/10) * (8/9) * (7/8) * (6/7) * (5/6) * (4/5) * (3/4) * (2/3)