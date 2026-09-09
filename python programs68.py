def largest_smallest_digit(n):
    digits = [int(d) for d in str(abs(n))]
    return max(digits), min(digits)

largest, smallest = largest_smallest_digit(3502891)
print("Largest:", largest)
print("Smallest:", smallest)