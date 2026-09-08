A = int(input("Enter any number:"))
B = int(input("Enter bit position value:")) 
if A & (1 << B):
    print("The bit is set")
else:
    print("The bit is not set")
    