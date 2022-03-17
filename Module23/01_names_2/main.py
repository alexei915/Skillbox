line_number = 0
total_length = 0

with open('people.txt', 'r', encoding='utf-8') as file:
    for i_line in file:
        line_number += 1
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        try:
            if length < 3:
                raise BaseException
        except BaseException:
            with open('errors.log', 'a') as mistakes:
                mistakes.write('Ошибка: менее трёх символов в строке {}.\n'.format(line_number))
                print('Ошибка: менее трёх символов в строке {}.'.format(line_number))
        total_length += length
    print('Общее количество символов: {}.'.format(total_length))
