total_bill = float(input("Enter Total Bill Amount: "))
people = int(input("Enter Number of People: "))

share = total_bill / people

print("Each Person Pays:", round(share, 2))