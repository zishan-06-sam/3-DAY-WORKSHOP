num = int(input("Enter a number: "))

n = abs(num)
reversed_num = 0
temp = n

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10

if n == reversed_num:
    print(str(num) + " is a palindrome")
else:
    print(str(num) + " is not a palindrome")