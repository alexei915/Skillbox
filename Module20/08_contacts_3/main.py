def add_contact():
    initial = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    initial = tuple(initial)
    if initial in phonebook_dict:
        print('Такой человек уже есть в контактах.')
        print(f'Текущий словарь контактов: {phonebook_dict}')
    else:
        phone_number = int(input('Введите номер телефона: '))
        phonebook_dict[initial] = phone_number
        print(f'Текущий словарь контактов: {phonebook_dict}')
    return phonebook_dict


def search_contact():
    surname = input('Введите фамилию для поиска: ').lower()
    for name, age in phonebook_dict.items():
        last_name = name[1].lower()
        if surname in last_name:
            print(name[0], name[1], age)
        else:
            print('Контакт не найден.')
    return phonebook_dict


phonebook_dict = dict()

while True:
    action = int(input('Введите номер действия:\n 1. Добавить контакт\n 2. Найти человека\n'))
    if action == 1:
        add_contact()
    if action == 2:
        search_contact()
