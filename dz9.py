CONTACTS = {}


def input_error(handler):

    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except ValueError:
            print('Uncorrect number')
        except KeyError:
            print('No such contact')
        except IndexError:
            print('Enter more information')
    return wrapper


def start_session():
    print('How can I help you?')


@input_error
def add_contact(command):
    words = command.split()
    name = words[1]
    phone = words[2]
    CONTACTS[name] = phone


@input_error
def change_contact(command):
    words = command.split()
    name = words[1]
    if name in CONTACTS:
        phone = words[2]
        CONTACTS[name] = phone
    else:
        print('No such name in your contacts')
    

@input_error
def find_contact(command):
    words = command.split()
    name = words[1]
    print(name, CONTACTS[name])


def show_all_contacts():
    if CONTACTS == {}:
        print('No contacts yet')
    else:
        for key, value in CONTACTS.items():
            print(key, value)


def main():
    
    while True:
        user_command = input("Enter command: ")
        words = user_command.split()
        if words[0] == 'hello':
            start_session()
        elif words[0] == 'add':
            add_contact(user_command)
        elif words[0] == 'change':
            change_contact(user_command)
        elif words[0] == 'phone':
            find_contact(user_command)
        elif words[0] == 'show':
            show_all_contacts()
        elif words[0] in ['good', 'close', 'exit']:
            break
        else:
            print('Wrong command')
            continue
        


if __name__ == '__main__':
    main()
    