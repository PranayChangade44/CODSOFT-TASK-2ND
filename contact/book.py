class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found matching your search.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(name, new_phone or None, new_email or None, new_address or None)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
