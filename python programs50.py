num = int(input("Enter a number: "))

n = abs(num)
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10

if num < 0:
    reversed_num = -reversed_num

print("Reversed number: " + str(reversed_num))