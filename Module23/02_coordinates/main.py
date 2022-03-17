import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nums_list = line.split()
        with open('result.txt', 'a') as file_2:
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                sorted_num = sorted([res1, res2, number])
                for elem in sorted_num:
                    file_2.write(str(elem) + ' ')
                file_2.write('\n')
            except ZeroDivisionError:
                file_2.write('На ноль делить нельзя!\n')
            except (ValueError, TypeError):
                file_2.write('Нельзя преобразовать в число.\n')