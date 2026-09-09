n = 4
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        if j % 2 == 0:
            row += "1 "
        else:
            row += "0 "
    print(row.strip())