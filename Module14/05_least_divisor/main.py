number = int(input('Введите число: '))
while number < 1:
    print('Ошибка ввода. Число дожно быть больше единицы!')
    number = int(input('Введите число: '))

for divider in range(2, number + 1):
    if number % divider == 0:
        break
    print('Наименьший делитель, отличный от единицы:', divider)
