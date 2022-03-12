site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth=0):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if depth > 0:
            depth -= 1
            if depth == 0:
                return None
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, depth)
            if result:
                break
    else:
        result = None
    return result


user_key = input('Введите искомый ключ: ')
question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if question == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
    value = find_key(site, user_key, depth=max_depth)
else:
    value = find_key(site, user_key)

print(f'Значение ключа: {value}')
