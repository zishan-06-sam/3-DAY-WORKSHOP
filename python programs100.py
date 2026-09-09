n = 4  
for i in range(n, 0, -1):
    row = [chr(65 + j) for j in range(i)]
    print(" ".join(row))