def sum_of_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total

print(sum_of_factorials(5))  