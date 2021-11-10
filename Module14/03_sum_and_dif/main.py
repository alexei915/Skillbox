def summ_number(n) -> object:
    figure = 0
    summ = 0
    while n != 0:
        figure = n
        figure %= 10
        summ += figure
        n //= 10
    return summ


def num_count(n):
    count = 0
    temp = n
    while temp > 0:
        temp //= 10
        count += 1
    return count


n = int(input('Введите число: '))
mySumm = summ_number(n)
myCount = num_count(n)
print('Сумма цифр:', summ_number(n))
print('Кол=во цифр в числе:', num_count(n))
print('Разность суммы и кол-ва цифр:', mySumm - myCount)
