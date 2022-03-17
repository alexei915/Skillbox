def check_accuracy(data):
    if len(data) < 3:
        raise IndexError
    if not data[0].isalpha():
        raise NameError
    if not '@' in data[1] and not '.' in data[1]:
        raise SyntaxError
    if not 10 < int(data[2]) < 99:
        raise ValueError
    return True


with open('registrations.txt', 'r', encoding='utf-8') as file:
    for i_line in file:
        if i_line.endswith('\n'):
            line = i_line[:-1]
        email = i_line.split()
        try:
            result = check_accuracy(email)
            with open('registrations_good.log', 'a') as good_email:
                good_email.write(' '.join(email) + '\n')
        except IndexError:
            with open('registrations_bad.log', 'a') as bad_email:
                bad_email.write(' '.join(email) + '   ' + 'НЕ присутствуют все три поля\n')
        except NameError:
            with open('registrations_bad.log', 'a') as bad_email:
                bad_email.write(' '.join(email) + '   ' + 'Поле имени содержит НЕ только буквы\n')
        except SyntaxError:
            with open('registrations_bad.log', 'a') as bad_email:
                bad_email.write(' '.join(email) + '   ' + 'Поле емейл НЕ содержит @ и .(точку)\n')
        except ValueError:
            with open('registrations_bad.log', 'a') as bad_email:
                bad_email.write(' '.join(email) + '   ' + 'Поле возраст НЕ является числом от 10 до 99\n')
