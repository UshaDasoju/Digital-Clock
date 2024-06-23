class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")
        else:
            print("Contact list is empty")

# Example usage:
contact1 = Contact("John Doe", "1234567890", "john.doe@example.com")
contact2 = Contact("Jane Smith", "0987654321", "jane.smith@example.com")

contact_list = ContactList()
contact_list.add_contact(contact1)
contact_list.add_contact(contact2)

contact_list.display_contacts()
