CONTACTS = {}


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except ValueError:
            return 'Uncorrect number'
        except IndexError:
            return 'Give me name and phone please'
        except KeyError:
            return 'No such contac'
        else:
            return handler(*args, **kwargs)
    return wrapper


def hello():
    return 'How can I help you?'


@input_error
def add_contact(command):
    words = command.split()
    name = words[1].lower()
    phone = int(words[2])
    CONTACTS[name] = phone
    return 'Contact is added'


@input_error
def change_contact(command):
    words = command.split()
    name = words[1].lower()
    if name in CONTACTS:
        CONTACTS[name] = int(words[2])
    else:
        return 'No such name in your contacts'
    return 'Contact is changed'
        

@input_error
def find_contact(command):
    words = command.split()
    name = words[1].lower()
    return CONTACTS[name]


def show_all_contacts():
    if CONTACTS == {}:
        return 'No contacts yet'
    else:
        contacts_str = ''
        for key, value in CONTACTS.items():
            contacts_str += f'{key}  {value} \n'
        return contacts_str


def main():
    
    while True:
        user_command = input("Enter command: ")
        words = user_command.split()
        command = words[0].lower()
        if command == 'hello':
            print(hello())
        elif command == 'add':
            print(add_contact(user_command))
        elif command == 'change':
            print(change_contact(user_command))
        elif command == 'phone':
            print(find_contact(user_command))
        elif command == 'show':    
            print(show_all_contacts())
        elif command in ['good', 'close', 'exit']:
            break
        else:
            print('Wrong command')
            continue
        


if __name__ == '__main__':
    main()