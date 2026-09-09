n = 4
count = 1
for i in range(1, n + 1):
    row = [str(count + j) for j in range(i)]
    print(' '.join(row))
    count += i