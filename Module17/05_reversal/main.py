string = input('Введите строку: ')

sym_list = list(string)
left_border = sym_list.index('h')
right_border = len(sym_list) - sym_list[::-1].index('h')
print('Обратная последовательность символов между первой и последней "h":')
for i in sym_list[left_border + 1:right_border - 1][::-1]:
    print(i, end='')
