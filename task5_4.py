from functools import wraps

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Після команди add введіть ім'я і номер абонента."
            elif func.__name__ == "change_contact":
                return "Після команди change введіть ім'я і новий номер телефону."    
            elif func.__name__ == "show_phone":
                return "Після команди phone введіть ім'я абонента."  
            else:
                return "Неправильний ввід даних"      
        except KeyError:
            return "Помилка вводу даних."
        except IndexError:
            if func.__name__ == "show_phone":
               return "Не введено абонента."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

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
    else:
        return "Контакт не знайдено."     
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."     

@input_error
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

# 
#     python e:\MyStudy\task5_4.py