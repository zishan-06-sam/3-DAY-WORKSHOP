def is_perfect(n):
    if n < 2:
        return False
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

print(is_perfect(28))  
print(is_perfect(12))  