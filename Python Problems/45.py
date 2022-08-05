triangle = set()
pentagon = set()
hexagon = set()

for i in range(100000):
    tri_temp = (i * (i + 1)) / 2
    pent_temp = (i * (3 * i  - 1)) / 2
    hex_temp = i * (2 * i - 1)
    
    if tri_temp in pentagon and tri_temp in hexagon:
        print(int(tri_temp))
    
    triangle.add(tri_temp)
    pentagon.add(pent_temp)
    hexagon.add(hex_temp)