# Bottom up dynamic programming approach
# Build the possibilities that each coin adds from smallest value to largest

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0] * target
#print(ways, len(ways))

for coin in coins:
    for i in range(coin, target + 1):
        ways[i] += ways[i - coin]
    print(ways)

print(ways[target])