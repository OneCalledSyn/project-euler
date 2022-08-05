# 2 3 4, 1 4 4 are the only acceptable number of digits

digits = {"1","2","3","4","5","6","7","8","9"}
products = set()

for i in range(1, 10):
    for j in range(1234, 10000):
        prod = i * j
        temp = set()
        i_char = [char for char in str(i)]
        j_char = [char for char in str(j)]
        prod_char = [char for char in str(prod)]

        for m in i_char:
            temp.add(m)
        for k in j_char:
            temp.add(k)
        for l in prod_char:
            temp.add(l)
        
        if temp == digits and prod >= 1000 and prod < 10000:
            print(i, j, prod)
            products.add(prod)

print(products, sum(products))


for i in range(12, 99):
    for j in range(123, 988):
        prod = i * j
        temp = set()
        i_char = [char for char in str(i)]
        j_char = [char for char in str(j)]
        prod_char = [char for char in str(prod)]

        for m in i_char:
            temp.add(m)
        for k in j_char:
            temp.add(k)
        for l in prod_char:
            temp.add(l)
        
        if temp == digits and prod >= 1000 and prod < 10000:
            print(i, j, prod)
            products.add(prod)

print(products, sum(products))
