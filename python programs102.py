n = 4  

rows = []
for i in range(1, n + 1):
    up = [chr(65 + j) for j in range(i)]        
    down = [chr(65 + j) for j in range(i - 2, -1, -1)]  
    row = up + down
    rows.append(" ".join(row))

width = len(rows[-1])  

for row in rows:
    print(row.center(width))