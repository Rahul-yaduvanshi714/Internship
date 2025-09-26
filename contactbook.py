import json
import os

class ContactManager:
    def _init_(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts yet.")
        else:
            for c in self.contacts:
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                return contact
        return None

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            contact["phone"] = new_phone
            contact["email"] = new_email
            self.save_contacts()
            print("Contact updated successfully!")
        else:
            print("Contact not found.")


def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Search contact")
        print("5. View all contacts")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to update: ")
            manager.update_contact(name)

        elif choice == "3":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)

        elif choice == "4":
            name = input("Enter name to search: ")
            contact = manager.search_contact(name)
            if contact:
                print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")

        elif choice == "5":
            manager.view_contacts()

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Please choose a valid option (1-6).")


if __name__ == "_main_":
    main()