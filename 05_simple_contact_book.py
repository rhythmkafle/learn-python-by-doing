import sys

contacts = []

def menu():
    print("\n--- Contact Book ---")
    print("1. View all contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    return input("What would you like to do?: ")

def add():
    name = input("Enter name: ").strip().title()
    try:
        phno = int(input("Enter phone number: ").strip())
    except ValueError:
        print("Phone number must be digits only.")
        return
    email = input("Enter email: ").strip()
    addr = input("Enter address: ").strip().title()

    if name and phno and email and addr:
        contact = {
            "Name": name,
            "Phone": phno,
            "Email": email,
            "Address": addr
        }
        contacts.append(contact)
        print("Contact added successfully.")
    else:
        print("All fields are required.")

def view():
    if not contacts:
        print("No contacts to display.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"\nContact {i}:")
            for key, value in contact.items():
                print(f"{key}: {value}")

def search(name=None):
    if name is None:
        name = input("Enter name to search: ").strip().title()
    for contact in contacts:
        if contact["Name"] == name:
            print("Contact found:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            return contact
    print("No contact found.")
    return None

def update():
    name = input("Enter name of the contact to update: ").strip().title()
    contact = search(name)
    if contact:
        field = input("Which field do you want to update? (Name/Phone/Email/Address): ").strip().title()
        if field in contact:
            if field == "Phone":
                try:
                    new_value = int(input(f"Enter new {field}: ").strip())
                except ValueError:
                    print("Phone number must be digits only.")
                    return
            else:
                new_value = input(f"Enter new {field}: ").strip().title()
            contact[field] = new_value
            print(f"{field} updated successfully.")
        else:
            print("Invalid field.")
    else:
        print("Update failed. Contact not found.")

def delete():
    name = input("Enter name of the contact to delete: ").strip().title()
    for i, contact in enumerate(contacts):
        if contact["Name"] == name:
            confirm = input(f"Are you sure you want to delete contact '{name}'? (Y/N): ").strip().lower()
            if confirm == 'y':
                contacts.pop(i)
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Contact not found.")

def exit_program():
    print("Exiting Contact Book. Goodbye!")
    sys.exit()

# Main loop
while True:
    choice = menu()
    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        exit_program()
    else:
        print("Invalid choice. Please select from 1 to 6.")
