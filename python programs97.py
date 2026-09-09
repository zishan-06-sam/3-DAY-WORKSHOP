n = 4  

for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(j % 2))
    print(" ".join(row))