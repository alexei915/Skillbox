file = open('C:\\Users\\PC\\Desktop\\Python_Basic\\Module22\\02_zen_of_python\\zen.txt', 'r')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
sym_dict = dict()
sym_count = 0
words_count = 0
str_count = 0

for i_line in file:
    str_count += 1
    if '\n' in i_line:
        i_line = i_line[:-2].split()
    else:
        i_line = i_line.split()
    for word in i_line:
        if word != '--':
            words_count += 1
        for sym in word:
            if sym.lower() in alphabet:
                sym_dict[sym.lower()] = sym_dict.get(sym.lower(), 0) + 1

file.close()
min_frequency = min(sorted(sym_dict.values()))
for i_key, i_value in sym_dict.items():
    sym_count += i_value
    if sym_dict[i_key] == min_frequency:
        rare_letter = i_key

print('Количество букв в файле: {}'.format(sym_count))
print('Количество слов в файле: {}'.format(words_count))
print('Количество строк в файле: {}'.format(str_count))
print('Наиболее редкая буква: {}'.format(rare_letter))




