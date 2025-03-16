class ContactsManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name: str, phone_number: str):
        if len(name.strip())==0:
            raise ValueError("contact name cannot be empty")
        if name in self.contacts:
            raise ValueError("contact already exists")
        self.contacts[name] = {name, phone_number}

    def get_contact(self, name):
        return self.contacts[name]
