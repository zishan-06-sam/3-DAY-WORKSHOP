n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1):
    total = total + i

print("Sum of first " + str(n) + " natural numbers = " + str(total))