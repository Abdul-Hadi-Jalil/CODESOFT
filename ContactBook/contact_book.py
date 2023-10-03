class Contact:
    def __init__(self, name, phone_no, email=None, address=None):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_no}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = set()

    def add_contact(self, contact):
        self.contacts.add(contact)

    def search_contact(self, name=None, phone_no=None, email=None, address=None):
        matching_contacts = []

        for contact in self.contacts:
            if (name is None or name.lower() in contact.name.lower()) and \
                    (phone_no is None or phone_no.lower() in contact.phone_no.lower()) and \
                    (email is None or email.lower() in contact.email.lower()) and \
                    (address is None or address.lower() in contact.address.lower()):
                matching_contacts.append(contact)

        return matching_contacts

    def delete_contact(self, name=None, phone_no=None, email=None, address=None):
        matching_contacts = self.search_contact(name, phone_no, email, address)

        if matching_contacts:
            for contact_to_remove in matching_contacts:
                self.contacts.discard(contact_to_remove)
            return True
        else:
            return False

    def update_contact(self, name=None, phone_no=None, email=None, address=None, new_contact=None):
        # Find and delete the old contact based on the specified parameters
        if self.delete_contact(name=name, phone_no=phone_no, email=email, address=address):
            # Add the new contact
            self.add_contact(new_contact)
            return True
        else:
            return False

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)
