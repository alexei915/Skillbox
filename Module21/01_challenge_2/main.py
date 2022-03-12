def timer(digits):
    if digits == 0:
        return 0
    timer(digits - 1)
    return print(digits)


number = int(input('Введите число: '))
result = timer(number)