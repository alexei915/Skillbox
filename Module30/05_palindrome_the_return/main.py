from collections import Counter


def can_be_poly(text) -> bool:
    """ Функция. Принимает на вход строку и проверяет,
     можно ли получить из неё палиндром.
    """

    letters_count = Counter(text)
    count = 0
    for i in letters_count.values():
        if i % 2 != 0:
            count += 1
    if count > 1:
        return False
    return True


if __name__ == '__main__':
    print(can_be_poly('ababc'))
    print(can_be_poly('abbbc'))