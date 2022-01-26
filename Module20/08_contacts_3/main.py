def add_contact():
    initial = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    initial = tuple(initial)
    if initial in phonebook:
        print('Такой человек уже есть в контактах.')
        print(f'Текущий словарь контактов: {phonebook}')
    else:
        phone_number = int(input('Введите номер телефона: '))
        phonebook[initial] = phone_number
        print(f'Текущий словарь контактов: {phonebook}')
    return phonebook


def search_contact():
    surname = input('Введите фамилию для поиска: ').lower()
    for name, age in phonebook.items():
        last_name = name[1].lower()
        if surname in last_name:
            print(name[0], name[1], age)
        else:
            print('Контакт не найден.')
    return phonebook


phonebook = dict()

while True:
    action = int(input('Введите номер действия:\n 1. Добавить контакт\n 2. Найти человека\n'))
    if action == 1:
        add_contact()
    if action == 2:
        search_contact()
