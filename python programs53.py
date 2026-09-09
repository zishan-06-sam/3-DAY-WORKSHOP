def product_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) * product_of_digits(n // 10)

num = int(input("Enter a number: "))
n = abs(num)

result = product_of_digits(n)
print("Product of digits: " + str(result))