from functools import wraps

def input_errorParse(parse_input):
    def inner(*args, **kwargs):
        try:
            return parse_input(*args, **kwargs)
        except ValueError:
            return "Помилка введення параметрів."

    return inner

def input_error(add):
    def inner(*args, **kwargs):
        try:
            return add(*args, **kwargs)
        except ValueError:
            return "Після команди add введіть ім'я і номер телефону абонента."

    return inner

def input_errorCh(change):
    def inner(*args, **kwargs):
        try:
            return change(*args, **kwargs)
        except ValueError:
            return "Після команди change введіть ім'я і новий номер телефону."
        except KeyError:
            return "Ім'я неправильне."
        except IndexError:
            return "Не введено абонента."

    return inner

def input_errorShow(show):
    def inner(*args, **kwargs):
        try:
            return show(*args, **kwargs)
        except ValueError:
            return "Після команди phone введіть ім'я абонента."
        except IndexError:
            return "Не введено абонента."

    return inner

def input_errorAll(all):
    def inner(*args, **kwargs):
        try:
            return all(*args, **kwargs)
        except ValueError:
            return "Неправильні параметри."
        except IndexError:
            return "Неправильний ввід."

    return inner


@input_errorParse
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_errorCh
def change_contact(args, contacts):
    name, phone = args
    if str(args[0]).strip() in contacts:
        contacts[name] = phone
    else:
        return "Контакт не знайдено."     
    return "Contact updated."

@input_errorShow
def show_phone(args, contacts):
    name = args[0]
    if str(args[0]).strip() in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."     

@input_errorAll
def all(contacts):
    return contacts.items() 

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
             print(all(contacts))         
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

# python e:\MyStudy\task5_4.py    