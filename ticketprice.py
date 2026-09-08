A = int(input("Enter customer age:"))
if A <=5:
    print("Ticket price is free")
elif A >5 and A <= 12:
    print("Ticket price is $10")
elif A >12 and A <= 60:
    print("Ticket price is $15")
else:
    print("Ticket price is $12")