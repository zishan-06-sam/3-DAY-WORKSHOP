A = int(input("Enter age:"))
if A < 13:
    print("You are a child")
elif A >= 13 and A < 20:
    print("You are a teenager")
elif A >= 20 and A < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")
