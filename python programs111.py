n = 6  

for i in range(n // 2, n, 2):
    print(" " * (n - i) + "*" * i + " " * (n - i) + "*" * i)

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))