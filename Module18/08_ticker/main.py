fst_string = input('Первая строка: ')
sec_string = input('Вторая строка: ')
shift = len(fst_string) - sec_string.index(fst_string[0])

char_index = sec_string.find(fst_string[0])
sec_string = sec_string[char_index:] + sec_string[:char_index]
if fst_string == sec_string:
    print(f'Первая строка получается из второй со сдвигом {shift}')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
