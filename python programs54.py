num = int(input("Enter a number: "))

n = abs(num)
divisor = 1

while divisor <= n // 10:
    divisor = divisor * 10

while divisor > 0:
    digit = n // divisor
    print(digit)
    n = n % divisor
    divisor = divisor // 10