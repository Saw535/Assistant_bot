from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, index, new_phone):
        if 0 <= index < len(self.phones):
            self.phones[index].value = new_phone

    def delete_phone(self, index):
        if 0 <= index < len(self.phones):
            del self.phones[index]

    def __str__(self):
        phones = "\n".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}\nPhones:\n{phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        records = "\n".join(str(record) for record in self.data.values())
        return f"Address Book:\n{records}"


def hello():
    print("How can I help you?")


def add(name, phone):
    phone_number = phone.replace(" ", "")
    name = name.strip()
    record = Record(name)
    record.add_phone(phone_number[-10:])
    address_book.add_record(record)
    print(f"{name}'s phone number ({phone_number[-10:]}) has been added to contacts.")


def change(name, phone):
    if name in address_book.data:
        record = address_book.data[name]
        record.edit_phone(0, phone)
        print(f"{name}'s phone number has been updated to {phone}.")
    else:
        print(f"{name} is not in contacts.")


def delete(name):
    if name in address_book.data:
        del address_book.data[name]
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} is not in contacts.")


def phone(name):
    if name in address_book.data:
        record = address_book.data[name]
        print(f"{record.name}:")
        for phone in record.phones:
            print(phone)
    else:
        print(f"{name} is not in contacts.")


def show_all():
    if address_book.data:
        print(address_book)
    else:
        print("No contacts to show.")


def exit_program():
    print("Goodbye!")
    quit()


def parse_command(command):
    parts = command.split(' ', 2)
    if parts[0].lower() == 'hello':
        hello()
    elif parts[0].lower() == 'add':
        if len(parts) == 3:
            add(parts[1], parts[2])
        else:
            print("Invalid name or phone number format. Please enter your first name and, if desired, your last name with a space, and your phone number without spaces.")
    elif parts[0].lower() == 'change':
        change(parts[1], parts[2])
    elif parts[0].lower() == 'delete':
        delete(parts[1])
    elif parts[0].lower() == 'phone':
        phone(parts[1])
    elif parts[0].lower() == 'show' and parts[1].lower() == 'all':
        show_all()
    elif any(word in parts for word in ['goodbye', 'good', 'bye', 'close', 'exit']):
        exit_program()
    else:
        print(f"Invalid command: {command}")


def main():
    global address_book
    address_book = AddressBook()
    while True:
        command = input("Enter command: ")
        parse_command(command)
        
if __name__ == '__main__': 
    main()