string = input('Введите слова через пробел: ').split()

words_length = [len(word) for word in string]
count = max(words_length)
largest_word = string[words_length.index(count)]

print(f'Самое длинное слово - {largest_word}, его длина - {count} букв')