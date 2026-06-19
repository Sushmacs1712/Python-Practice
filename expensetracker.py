expenses = []

while True:
    amount = input("Enter expense (or 'q' to quit): ")

    if amount.lower() == 'q':
        break

    expenses.append(float(amount))

print("Total Expenses:", sum(expenses))
print("Number of Expenses:", len(expenses))

if expenses:
    print("Highest Expense:", max(expenses))
    print("Lowest Expense:", min(expenses))