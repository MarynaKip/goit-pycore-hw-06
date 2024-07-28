from collections import UserList

class WrongPhoneNumber(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone = None):
        self.phone = phone
        self.validate_phone()

    def validate_phone(self):
        if len(self.phone) != 10 or not self.phone.isdigit():
            raise WrongPhoneNumber("Wrong phone number!")

class Record:
    def __init__(self, name, phones = []):
        self.name = name
        self.phones = phones
        self.contact = {name: phones}

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
    
    def add_phone(self, args):
        name, phone = args
        self.phones.append(phone)
        self.contact[name].append(phone)
        return "Contact added."
    
    def remove_phone(self, args):
        name, phone = args
        if name not in list(self.contact.keys()):
            raise IndexError('There is no such contact in the contacts!')
        else:
            self.phones = list(filter(lambda number: number == phone, self.phones))
            self.contact[name] = self.phones
            return "Contact removed."

    def edit_phone(self, args):
        phone = args[0]
        self.phones = [phone]
        self.contact[self.name] = self.phones
        return "Contact updated."

    def find_phone(self, args):
        name = args[0]
        return self.contact[name]

class AddressBook(UserList):
    def add_record(self, record: Record):
           self.data.append(record)
           return "Contact added."

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError('The contact was not found. Please try again!')

    def delete(self, name):
        self.data = [i for i in self.data if not (i['name'] == name)]
        return "The contact was removed."

