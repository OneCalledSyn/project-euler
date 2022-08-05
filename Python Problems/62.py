cubes = dict()
solutions = []

for i in range(100, 10000):
    curr = ''.join(sorted(str(i ** 3)))
    print(curr)
    
    if curr not in cubes.keys():
        cubes[curr] = list()
    
    cubes[curr].append(i)
    
    if len(cubes[curr]) == 5:
        solutions.append(cubes[curr])
    
    if len(cubes[curr]) == 6:
        solutions.remove(cubes[curr])


#print(i, curr, cubes[curr])
print(solutions, solutions[0][0] ** 3)