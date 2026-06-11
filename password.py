previous_password = "Hello@123"

password = input("Enter password: ")

if password == previous_password:
    print("You cannot reuse your previous password")

elif len(password) < 8:
    print("Password must be at least 8 characters")

elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter")

elif not any(char.islower() for char in password):
    print("Password must contain a lowercase letter")

elif not any(char.isdigit() for char in password):
    print("Password must contain a number")

elif not any(not char.isalnum() for char in password):
    print("Password must contain a special character")

else:
    print("Strong Password")