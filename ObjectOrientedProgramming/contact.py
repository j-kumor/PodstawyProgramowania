class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        """Returns the string representation of the contact."""
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"
