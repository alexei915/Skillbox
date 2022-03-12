def fibonacci(number):
    if number < 3:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
my_function = fibonacci(num_pos)
print('Число: {}'.format(my_function))
