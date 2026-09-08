A = int(input("Enter the first side of the triangle: "))
B = int(input("Enter the second side of the triangle: "))   
c = int(input("Enter the third side of the triangle: "))
if A == B and B == c:
    print("The triangle is equilateral.")
elif A == B or B == c or A == c:    
    print("The triangle is isosceles.")     
else:
    print("The triangle is scalene.")