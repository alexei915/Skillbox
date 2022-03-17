import random


summ = 0

try:
    while summ <= 777:
        number = int(input('Введите число: '))
        summ += number
        if random.randint(1, 13) == 5:
            raise BaseException
        with open('output.txt', 'a') as file:
            file.write(str(number) + '\n')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
except BaseException:
    print('Вас постигла неудача!')