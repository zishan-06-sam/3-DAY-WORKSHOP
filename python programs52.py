num = int(input("Enter a number: "))

n = num
seen = []

while n != 1 and n not in seen:
    seen.append(n)
    total = 0
    while n > 0:
        digit = n % 10
        total = total + (digit * digit)
        n = n // 10
    n = total

if n == 1:
    print(str(num) + " is a happy number")
else:
    print(str(num) + " is not a happy number")