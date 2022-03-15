import zipfile

voyna_i_mir = zipfile.ZipFile('C:\\Users\\PC\\Desktop\\'
                              'Python_Basic\\Module22\\09_war_and_peace\\voyna-i-mir.zip')
voyna_i_mir.extract('voyna-i-mir.txt', 'C:\\Users\\PC\\Desktop\\Python_Basic\\Module22\\09_war_and_peace')
voyna_i_mir.close()


def quicksort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i[1] <= pivot[1]]
        greater = [i for i in data[1:] if i[1] > pivot[1]]

    return quicksort(greater) + [pivot] + quicksort(less)


histogram_ru_letters = dict()
histogram_en_letters = dict()
sym_count = 0
english_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

voyna_i_mir = open('voyna-i-mir.txt', 'r', encoding='utf-8')

for i_line in voyna_i_mir:
    for sym in i_line:
        if sym in russian_alphabet:
            sym_count += 1
            histogram_ru_letters[sym] = histogram_ru_letters.get(sym, 0) + 1
        if sym in english_alphabet:
            sym_count += 1
            histogram_en_letters[sym] = histogram_en_letters.get(sym, 0) + 1

voyna_i_mir.close()

for i_key, i_value in histogram_en_letters.items():
    histogram_en_letters[i_key] = round(i_value / sym_count, 6)


for i_key_2, i_value_2 in histogram_ru_letters.items():
    histogram_ru_letters[i_key_2] = round(i_value_2 / sym_count, 6)

sorted_keys_ru = sorted(histogram_ru_letters.items())
sorted_keys_en = sorted(histogram_en_letters.items())
amount_sorted_ru = quicksort(sorted_keys_ru)
amount_sorted_en = quicksort(sorted_keys_en)

new_file = open('analysis.txt', 'w')

new_file.write('Частотный анализ букв английского алфавита (по убыванию):\n')
for letter_share in amount_sorted_en:
    new_file.write(letter_share[0] + ' ' + str(letter_share[1]) + '\n')

new_file.write('\nЧастотный анализ букв русского алфавита (по убыванию):\n')
for letter_share_2 in amount_sorted_ru:
    new_file.write(letter_share_2[0] + ' ' + str(letter_share_2[1]) + '\n')

new_file.close()
new_file = open('analysis.txt', 'r', encoding='windows-1251')

print('\n\nСодержимое файла analysis.txt:')
for i_line in new_file:
    print(i_line, end='')

new_file.close()