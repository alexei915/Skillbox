number_of_pairs = int(input('Введите количество пар слов: '))
words_synonyms = dict()

for i_pairs in range(number_of_pairs):
    pairs = input(f'{i_pairs + 1} пара: ').lower().split(' - ')
    words_synonyms[pairs[0]] = pairs[1]
    words_synonyms[pairs[1]] = pairs[0]

word = input('\nВведите слово: ').lower()
while not words_synonyms.get(word):
    print('Такого слова в словаре нет.')
    word = input('Введите слово: ').lower()
else:
    print(f'Синоним: {words_synonyms[word]}')
