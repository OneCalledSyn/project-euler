x = 85
y = 120
target = 1000000000000

while y < target:
    # print(y)
    x, y = (3*x + 2*y - 2), (4*x + 3*y - 3)

print(x, y)

# Quadratic Diophantine equation solver: https://www.alpertron.com.ar/ENGLISH.HTM 
# OEIS A011900: Members of Diophantine pairs