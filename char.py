A = input("Enter any character:")
B = ord(A)
if B >= 65 and B <= 90:
    print("The character is an uppercase letter")
elif B >= 97 and B <= 122:
    print("The character is a lowercase letter")
elif B >= 48 and B <= 57:
    print("The character is a digit")
elif B >= 32 and B <= 47 or B >= 58 and B <= 64 or B >= 91 and B <= 96 or B >= 123 and B <= 126:
    print("The character is a special character")
else:
    print("The character is not a letter")
