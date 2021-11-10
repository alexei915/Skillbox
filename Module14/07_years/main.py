first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print(f'Года от {first_year} до {second_year} с тремя одинаковыми цифрами:')
for number in range(first_year, second_year + 1):
    first_digit = number // 1000
    second_digit = number // 100 % 10
    third_digit = number % 100 // 10
    fourth_digit = number % 10
    if (first_digit == second_digit == third_digit) and (first_digit != fourth_digit):
        print(number)
    elif (first_digit == second_digit == fourth_digit) and (first_digit != third_digit):
        print(number)
    elif (first_digit == third_digit == fourth_digit) and (first_digit != second_digit):
        print(number)
    elif (second_digit == third_digit == fourth_digit) and (second_digit != first_digit):
        print(number)