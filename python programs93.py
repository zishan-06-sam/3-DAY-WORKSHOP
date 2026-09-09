n = 4  

rows = []
for i in range(1, n + 1):
    row = list(range(1, 2*i))  
    rows.append(row)

width = len(" ".join(map(str, rows[-1])))  

for row in rows:
    row_str = " ".join(map(str, row))
    print(row_str.center(width))