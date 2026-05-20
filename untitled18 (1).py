contacts = {}

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Display Contacts\n5. Exit")
    choice = input("Select an option (1-5): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact for {name} added.")
    elif choice == '2':
        name = input("Enter name to search: ")
        print(f"Phone: {contacts[name]}" if name in contacts else "Contact not found.")
    elif choice == '3':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Deleted {name}.")
        else:
            print("Contact not found.")
    elif choice == '4':
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '5':
        break
    else:
        print("Invalid choice.")