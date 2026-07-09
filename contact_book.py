contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = phone
        print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print(f"Phone Number: {contacts[name]}")
    else:
        print("Contact not found.")

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please try again.")