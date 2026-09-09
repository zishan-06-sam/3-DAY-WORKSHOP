n = 4  

sizes = list(range(0, n)) + list(range(n - 2, 0, -1))

for s in sizes:
    if s == 0:
        print("*")
    else:
        right = " ".join("*" * s)
        print("*\t" + right)