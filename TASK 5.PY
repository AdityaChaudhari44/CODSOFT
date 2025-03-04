import json

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

# Function to search for a contact
def search_contact(contacts, query):
    found_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found with that name or phone number.")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to update a contact's details
def update_contact(contacts):
    name_to_update = input("Enter the name of the contact to update: ")
    contact = next((c for c in contacts if c['name'].lower() == name_to_update.lower()), None)

    if contact:
        print(f"Updating details for {contact['name']}:")
        contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ")
        contact['email'] = input(f"Enter new email (current: {contact['email']}): ")
        contact['address'] = input(f"Enter new address (current: {contact['address']}): ")
        save_contacts(contacts)
        print(f"Contact for {contact['name']} updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ")
    contact = next((c for c in contacts if c['name'].lower() == name_to_delete.lower()), None)

    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        print(f"Contact {contact['name']} deleted successfully!")
    else:
        print("Contact not found.")

# Main function for the contact manager
def contact_manager():
    contacts = load_contacts()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(contacts, query)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the contact manager
contact_manager()
