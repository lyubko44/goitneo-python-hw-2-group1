def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact for entered name does not exist."
        except IndexError:
            return "Contact list is empty."         

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone for contact {name} has been changed."
    else:
        raise KeyError

@input_error
def display_all(contacts):
    if len(contacts) == 0:
        raise IndexError
    else:
        return '\n'.join([name + " - " + phone for name, phone in contacts.items()])

@input_error
def display_phone(args, contacts):
    name = ''.join(args)
    return contacts[name]

def main():
    contacts = {'Lucas': '91679333'}
    #contacts = {}
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
        elif command == "all":
            print(display_all(contacts))
        elif command == "phone":
            print(display_phone(args, contacts))          
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()