def check_digits(text):
    count = 0
    for sym in text:
        if sym.isdigit():
            count += 1
    if count >= 3:
        return False
    return True


def check_big_letter(text):
    for letter in text:
        if letter.isupper():
            return False
    return True


while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif check_digits(password):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif check_big_letter(password):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
