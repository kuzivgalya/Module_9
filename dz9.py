CONTACTS = {}


def input_error(handler):
    def wrapper():
        try:
            handler()
        except ValueError:
            print('Uncorrect number')
        except KeyError:
            print('No such contact')
    return wrapper


def start_session():
    print('How can I help you?')


@input_error
def add_contact():
    name = input("Enter name: ")
    phone = int(input("Enter phone: "))
    CONTACTS[name] = phone


@input_error
def change_contact():
    name = input('Enter contact name: ')
    if name in CONTACTS:
        phone = int(input('Enter new phone: '))
        CONTACTS[name] = phone
    else:
        print('No such name in your contacts')
    

@input_error
def find_contact():
    name = input('Enter contact name: ')
    print(name, CONTACTS[name])


def show_all_contacts():
    if CONTACTS == {}:
        print('No contacts yet')
    else:
        for key, value in CONTACTS.items():
            print(key, value)


def main():
    commands = {
        'hello': start_session,
        'add': add_contact,
        'change': change_contact,
        'phone': find_contact,
        'show all': show_all_contacts,
        'good bye': quit,
        'close': quit,
        'exit': quit
    }

    while True:
        user_command = input("Enter command: ")
        if user_command not in commands:
            print("Unknown command. Please try again.")
            continue
        commands[user_command]()


if __name__ == '__main__':
    main()
    