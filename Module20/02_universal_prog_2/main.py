def is_prime(index):
    if index < 2:
        return False
    for divider in range(2, index):
        if index % divider == 0:
            return False
    return True


def crypto(data):
    return [value for num, value in enumerate(data) if is_prime(num)]


my_function = crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(my_function)

# TODO num это сокращение
