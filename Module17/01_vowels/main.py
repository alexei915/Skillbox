text = input('Введите текст: ')

vowel_letters = [letter for letter in text if letter == 'а' or letter == 'о'
                 or letter == 'у' or letter == 'ы' or letter == 'э'
                 or letter == 'и' or letter == 'е' or letter == 'ё'
                 or letter == 'ю' or letter == 'я']

print(f'Список гласных букв: {vowel_letters}')
print(f'Длина списка: {len(vowel_letters)}')