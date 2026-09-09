def sum_even_odd(n):
    even_sum = 0
    odd_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum

even_total, odd_total = sum_even_odd(10)
print("Even sum:", even_total)
print("Odd sum:", odd_total)