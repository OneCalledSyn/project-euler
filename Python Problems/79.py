# Idea: Make a dictionary where the keys are the single digits 0-9 and the values are the numbers which
# appear after them in the successful logins

# 0: None
# 1: 0,2,6,8,9
# 2: 0,8,9
# 3: 0,1,2,6,8,9
# 4: None
# 5: None
# 6: 0,2,8,9
# 7: 0,1,2,3,6,8,9
# 8: 0,9
# 9: 0

# Build the passcode from the bottom up, starting with the shortest value

# Idea 2: Build a directed graph and perform topological sort to return the passcode