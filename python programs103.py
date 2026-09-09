n = 4  


for i in range(1, n + 1):
    left = "*" * i
    spaces = " " * (2 * (n - i))
    right = "*" * i
    print(left + spaces + right)


for i in range(n - 1, 0, -1):
    left = "*" * i
    spaces = " " * (2 * (n - i))
    right = "*" * i
    print(left + spaces + right)