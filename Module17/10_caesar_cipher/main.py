def check(letter):
    for i_sym in letters:
        if i_sym == letter:
            return True
    return False


letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
           'ж', 'з', 'и', 'й', 'к', 'л', 'м',
           'н', 'о', 'п', 'р', 'с', 'т', 'у',
           'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
           'ы', 'ь', 'э', 'ю', 'я']

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
sym_list = list(message)

print('Зашифрованное сообщение: ', end='')
for i in range(len(sym_list)):
    if check(sym_list[i]):
        if letters.index(sym_list[i]) + shift < len(letters):
            sym_list[i] = letters[letters.index(sym_list[i]) + shift]
            print(sym_list[i], end='')
        else:
            sym_list[i] = letters[letters.index(sym_list[i]) + shift - len(letters)]
            print(sym_list[i], end='')
    else:
        print(sym_list[i], end='')
