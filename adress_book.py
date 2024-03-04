from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other    

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Phone number must be a 10-digit string.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []    

    def add_phone(self, phone): 
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(Phone(phone))

    def find_phone(self, phone):
        if phone in self.phones:
            return phone    

    def edit_phone(self, existing_phone, new_phone):
        try:
            exist_index = self.phones.index(existing_phone)
            self.phones[exist_index] = Phone(new_phone)
        except ValueError:
            print("Unable to find existing phone: " + existing_phone)
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            print("Unable to find record for name: " + name)  

    def delete(self, name):
        self.data.pop(name)
