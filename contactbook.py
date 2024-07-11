# Contact Book Program

contact_book = {}

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found!")

def search_contact():
    name = input("Enter name of contact to search: ")
    if name in contact_book:
        print(f"Contact {name} found!")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
    else:
        print(f"Contact {name} not found!")

def display_all_contacts():
    if contact_book:
        print("All Contacts:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts in the contact book!")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        display_all_contacts()
    elif choice == "5":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Please try again!")
