def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(msg):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return msg
            except IndexError:
                return msg
            except KeyError as name:
                return f"Contact with name {name} not found"
        
        return inner
    return decorator

@input_error("Give me name and phone please.")
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error("Give me name and new phone please.")
def change_contact(args, contacts):
    name, phone = args
    old_phone = contacts[name]
    contacts[name] = phone
    return "Contact updated."

@input_error("Give me name please.")
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all(contacts):
    res = []
    for name, phone in contacts.items():
        res.append(f"{name}: {phone}")
    return "\n".join(res)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()