from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str, default = None):
        for itm in self.phones:
            if str(itm) == phone:
                return itm
        return default

    def remove_phone(self, phone:str):
        itm = self.find_phone(phone)
        if itm:
            self.phones.remove(itm)

    def edit_phone(self, old, new):
        phone = self.find_phone(old)
        if phone:
            phone.value = new

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[str(rec.name)] = rec

    def find(self, name: str, default = None):
        return self.data.get(name, default)
    
    def delete(self, name: str):
        self.data.pop(name)

    def __str__(self):
        return "\n".join(map(lambda x: str(x), self.data.values()))
    

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    print(book)
