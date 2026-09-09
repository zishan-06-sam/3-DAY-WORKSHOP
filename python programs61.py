def harmonic_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total

print(harmonic_sum(5))  