import view

phone_book = []


def get_phone_book():
    global phone_book
    return phone_book


def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book


def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)


def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y, n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False


def change_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    temp = view.input_new_contact()
    confirm = input(f'Вы действительно хотите изменить контакт {name}? (y, n)')
    if confirm.lower() == 'y':
        phone_book[id - 1] = temp
        return True
    return False


def search_contact(search_string):
    global phone_book
    found = []
    for contact in phone_book:
        for item in contact:
            if item.count(search_string):
                found.append(contact)
    return found
