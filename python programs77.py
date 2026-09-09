def increasing_decreasing(n):
    if n <= 0:
        return
    print(n, end=" ")           
    increasing_decreasing(n - 1)
    print(n, end=" ")           

increasing_decreasing(5)
