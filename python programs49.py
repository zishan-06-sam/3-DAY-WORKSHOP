num = int(input("Enter a number: "))

n = abs(num)
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits: " + str(total))