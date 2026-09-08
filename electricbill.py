A = int(input("Enter electricity bill amount: "))
if A > 100:
    print("You have to pay a surcharge of 10% in addition to your bill.")
    surcharge = A * 0.10
    total_amount = A + surcharge
    print("Total amount to be paid: ", total_amount)
else:
    print("No surcharge applicable.")
    print("Total amount to be paid: ", A)
