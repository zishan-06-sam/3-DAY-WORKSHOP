n = 4  
for i in range(1, n + 1):
    row = [chr(65 + j) for j in range(i)]
    print(" ".join(row))