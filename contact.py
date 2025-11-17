class Contact:
    def __init__(self, name, phone, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, email={self.email}, address={self.address})"
