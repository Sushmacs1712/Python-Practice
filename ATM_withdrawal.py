balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Enter a valid amount")

elif amount > balance:
    print("Insufficient Balance")

else:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)