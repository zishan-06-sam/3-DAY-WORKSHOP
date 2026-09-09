n = 4  

rows = []


for i in range(1, n + 1):
    up = list(range(1, i + 1))
    down = list(range(i - 1, 0, -1))
    row = up + down
    rows.append(row)

for i in range(n - 1, 0, -1):
    rows.append(rows[i - 1])

width = len(" ".join(map(str, rows[n - 1])))  

for row in rows:
    row_str = " ".join(map(str, row))
    print(row_str.center(width))