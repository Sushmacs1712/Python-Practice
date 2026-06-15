num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers cannot be palindrome")
else:
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    print("Reversed Number:", reverse)

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")