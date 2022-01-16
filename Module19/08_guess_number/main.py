max_number = int(input('Введите максимальное число: '))
nums_1 = {i for i in range(1, max_number + 1)}


while True:
    str_list = input('\nНужное число есть среди вот этих чисел: ')
    if str_list == 'Помогите!':
        print('Артём мог загадать следующие числа: ', end='')
        for i_num in nums_1:
            print(i_num, end=' ')
        break
    answer = input('Ответ Артёма: ')
    numbers_list = [int(x) for x in str_list.split()]
    nums_2 = set(numbers_list)
    if answer == 'Да':
        nums_1 &= nums_2
    elif answer == 'Нет':
        nums_1 -= nums_2
