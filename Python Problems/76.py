# https://mathworld.wolfram.com/PartitionFunctionP.html
# Use generating function (line 11)

#Dynamic programming method

target = 100
nums = [x for x in range(1,100)]
ways = [1] + [0] * target

for num in nums:
    for i in range(num, target + 1):
        ways[i] += ways[i - num]
    print(ways)

print(ways[target])