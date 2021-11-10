def conversely_number(number):
    revers_number = 0
    num_count = 0
    temp = number
    figure = number
    while temp > 0:
        temp //= 10
        num_count += 1
    while figure > 0:
        number %= 10
        revers_number += number * (10 ** (num_count - 1))
        figure //= 10
        number = figure
        num_count -= 1
    return revers_number


def fractional_part(number):
    count = 0
    the_whole_part = int(number)
    while number % 1 != 0:
        number *= 10
        count += 1
    fraction = number - the_whole_part * (10 ** count)
    x = conversely_number(fraction)
    x /= 10 ** count
    return x


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
the_whole_part_first = int(first_number)
the_whole_part_second = int(second_number)
first_fractional_part = fractional_part(first_number)
second_fractional_part = fractional_part(second_number)
first_revers = conversely_number(the_whole_part_first)
second_revers = conversely_number(the_whole_part_second)


print('Первое число наоборот:', first_fractional_part + first_revers)
print('Второе число наоборот:', second_fractional_part + second_revers)
print('Сумма:', first_fractional_part + first_revers + second_fractional_part + second_revers)