import os


text = input('Введите строку: ')
save_file = input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
path = os.path.abspath(os.path.join(os.path.sep, '/'.join(save_file)))

while not os.path.exists(path):
    print('Ошибка! Указанного пути не существует.')
    save_file = input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
    path = os.path.abspath(os.path.join(os.path.sep, '/'.join(save_file)))


file_name = input('\nВведите имя файла: ')
new_path = os.path.join(path, file_name + '.txt')

if os.path.exists(new_path):
    question = input('Вы действительно хотите перезаписать файл? ')
    if question == 'да':
        file = open(new_path, 'w')
        file.write(text)
        file.close()
        print('Файл успешно перезаписан!')
    else:
        print('Ок')
else:
    file = open(new_path, 'w')
    file.write(text)
    file.close()
    print('Файл успешно сохранён!')


print('***************')
file = open(new_path, 'r', encoding='utf-8')
print('Содержимое файла:')
for i_line in file:
    print(i_line, end='')
file.close()