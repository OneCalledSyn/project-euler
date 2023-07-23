total = 99
bouncy = 0
i = 100

while bouncy / total != 0.99:
    total += 1
    tmp = sorted(str(i))
    ordered = "".join(tmp)
    if str(i) != ordered and str(i) != ordered[::-1]:
        bouncy += 1
    print(f"Ordered: {ordered}, str(i): {str(i)}, Ordered[::-1]: {ordered[::-1]}, Ratio: {bouncy / total}, Bouncy: {bouncy}")
    i += 1
    
print(total)
