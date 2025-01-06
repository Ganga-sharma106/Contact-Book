# Contact Book1

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = phone
        print("Contact added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found!")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")