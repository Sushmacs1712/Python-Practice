message = input("Enter a message: ")

encoded = ""

for ch in message:
    encoded += chr(ord(ch) + 1)

print("Encoded Message:", encoded)