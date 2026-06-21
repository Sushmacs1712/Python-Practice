import random

rolls = int(input("How many times do you want to roll the dice? "))

total = 0

for i in range(rolls):
    dice = random.randint(1, 6)
    total += dice
    print(f"Roll {i + 1}: {dice}")

print("\nTotal Score:", total)
print("Average Score:", round(total / rolls, 2))