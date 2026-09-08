A = int(input("Enter the first side of the triangle: "))
B = int(input("Enter the second side of the triangle"))
C = int(input("Enter the third side of the triangle"))
if A+B>C and A+C>B and B+C>A:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
