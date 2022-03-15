def quicksort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i[1] <= pivot[1]]
        greater = [i for i in data[1:] if i[1] > pivot[1]]

    return quicksort(greater) + [pivot] + quicksort(less)


file = open('text.txt', 'w')
text = input('Введите текст: ')
file.write(text)
file.close()

file = open('text.txt', 'r', encoding='utf-8')
histogram = dict()
sym_count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('\nСодержимое файла text.txt:')
for i_line in file:
    print(i_line, end='')
    for sym in i_line:
        if sym in alphabet:
            sym_count += 1
            histogram[sym.lower()] = histogram.get(sym.lower(), 0) + 1

file.close()

for i_key, i_value in histogram.items():
    histogram[i_key] = round(i_value / sym_count, 3)


sorted_keys = sorted(histogram.items())
amount_sorted = quicksort(sorted_keys)
new_file = open('analysis.txt', 'w')

for letter_share in amount_sorted:
    new_file.write(letter_share[0] + ' ' + str(letter_share[1]) + '\n')

new_file.close()
new_file = open('analysis.txt', 'r', encoding='utf-8')

print('\n\nСодержимое файла analysis.txt:')
for i_line in new_file:
    print(i_line, end='')

new_file.close()

