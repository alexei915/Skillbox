word = input('Введите слово: ')
symbol = list(word)

count = 0
unique_letter_count = 0

for i in word:
    for sym in symbol:
        if sym != i:
            count += 1
    if count == len(symbol) - 1:
        unique_letter_count += 1
    count = 0

print(f'Кол-во уникальных букв: {unique_letter_count}')
