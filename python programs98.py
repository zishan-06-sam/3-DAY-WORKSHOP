n = 4  
for i in range(n):
    letter = chr(65 + i)  
    row = (letter + " ") * (i + 1)
    print(row.strip())