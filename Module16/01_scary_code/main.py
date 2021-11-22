amn_list = [1, 5, 3]
first_list = [1, 5, 1, 5]
second_list = [1, 3, 1, 5, 3, 3]

amn_list.extend(first_list)
print(f'Кол-во цифр 5 при первом объединении: {amn_list.count(5)}')

for i_num in amn_list:
    if i_num == 5:
        amn_list.remove(i_num)

amn_list.extend(second_list)
print(f'Кол-во цифр 3 при втором объединении: {amn_list.count(3)}')
print(f'Итоговый список: {amn_list}')

