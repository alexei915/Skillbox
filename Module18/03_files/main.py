file_name = input('Название файла: ')

if file_name.startswith(('@', '№', '$', '^', '&', '*', '(', ')')):
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла.\nОжидалось .txt или .docx')
else:
    print('Файл назван верно')
