n = 4  

rows = []
for i in range(1, n + 1):
    row = " ".join(chr(65 + j) for j in range(i))
    rows.append(row)

width = len(rows[-1])  

for row in rows:
    print(row.rjust(width))