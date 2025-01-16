class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Adds a new contact to the list."""
        self.contacts.append(contact)

    def display_contacts(self):
        """Displays all contacts in the list."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)
