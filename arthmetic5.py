A = int(input("Enter any number:"))
if A%3==0 and A%5==0:
  print("it is divisible by both 3 and 5")
elif A%3==0 and A%5!=0:
  print("The number is only divisible by 3")
elif A%3!=0 and A%5==0:
  print("The number is only divisible by 5")
else:
  print("The number is not divisible by both 3 and 5")
