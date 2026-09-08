A = int(input("enter the time period"))
if A >= 0 and A < 12:
    print("Good Morning")
elif A >= 12 and A < 16:
    print("Good Afternoon")
elif A >= 16 and A < 20:
    print("Good Evening")
else:
    print("Good Night")