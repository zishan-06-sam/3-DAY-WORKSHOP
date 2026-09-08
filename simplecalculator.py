A = int(input("Enter first number : "))
B = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
if op == "+":
    print("Sum of two numbers is: ", A+B)
elif op == "-":
    print("Difference of two numbers is: ", A-B)
elif op == "*":
    print("Product of two numbers is: ", A*B)
elif op == "/":
    print("Division of two numbers is: ", A/B)
else:
    print("Invalid operation")   
