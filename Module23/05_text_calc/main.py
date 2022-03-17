def calculator(data):
    if data[1] == '+':
        return int(data[0]) + int(data[2])
    elif data[1] == '-':
        return int(data[0]) - int(data[2])
    elif data[1] == '*':
        return int(data[0]) * int(data[2])
    elif data[1] == '/':
        return int(data[0]) / int(data[2])
    elif data[1] == '//':
        return int(data[0]) // int(data[2])
    elif data[1] == '%':
        return int(data[0]) % int(data[2])
    elif data[1] == '**':
        return int(data[0]) ** int(data[2])


total_summ = 0

with open('calc.txt', 'r', encoding='utf-8') as file:
    for i_line in file:
        if i_line.endswith('\n'):
            expression_list = i_line[:-1].split()
        else:
            expression_list = i_line.split()
        try:
            result = calculator(expression_list)
            total_summ += result
        except ZeroDivisionError:
            print(f'Ошибка в строке {" ".join(expression_list)}. На ноль делить нельзя!')
        except ValueError:
            print(f'Строку {" ".join(expression_list)} нельзя преобразовать к числу.')
            question = input('Хотите исправить? ')
            if question == 'да':
                corrected_str = input('Введите исправленную строку: ').split()
                total_summ += calculator(corrected_str)
        except TypeError:
            question = input(f'Обнаружена ошибка в строке: {" ".join(expression_list)}   Хотите исправить? ')
            if question == 'да':
                corrected_str = input('Введите исправленную строку: ').split()
                total_summ += calculator(corrected_str)


print('\nСумма результатов: {}'.format(total_summ))
