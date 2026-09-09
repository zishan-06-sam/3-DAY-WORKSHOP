balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
min_balance = 1000

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif amount > (balance - min_balance):
    print("Withdrawal rejected: insufficient balance (minimum balance of " + str(min_balance) + " must be maintained)")
else:
    balance = balance - amount
    print("Withdrawal approved")
    print("Remaining balance: " + str(balance))