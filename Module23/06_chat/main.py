user_name = input('Введите имя пользователя: ')

while True:
    action = input('Выберите действие (1. Посмотреть текущий текст чата 2. Отправить сообщение): ')
    if action == '1':
        try:
            with open('history_chat.txt', 'r', encoding='cp1251') as chat:
                print()
                history = chat.readlines()
                print(''.join(history))
        except FileNotFoundError:
            print('Пока чат пуст...')
    elif action == '2':
        with open('history_chat.txt', 'a') as chat:
            user_message = input('Введите сообщение: ')
            chat.write('{name}: {message}\n'.format(name=user_name, message=user_message))
            print()
    else:
        print('Ошибка. Необходимо ввести 1 или 2.')
