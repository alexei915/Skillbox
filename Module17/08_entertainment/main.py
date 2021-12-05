import random

sticks_count = int(input('Кол-во палок: '))
throws_count = int(input('Кол-во бросков: '))

sticks = ['I' for i in range(sticks_count)]
for i in range(throws_count):
    left_border = random.randint(1, 10)
    right_border = random.randint(left_border, 10)
    print(f'Бросок {i + 1}. Сбиты палки с номера {left_border} по номер {right_border}')
    for i_throw in range(10):
        if left_border - 1 <= i_throw <= right_border - 1:
            sticks[i_throw] = '.'

print('Результат:', end=' ')
for i_stick in sticks:
    print(i_stick, end='')
