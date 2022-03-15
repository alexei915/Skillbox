import os


def get_data(user_path, data_catalog=dict()):
    for i_elem in os.listdir(user_path):
        path = os.path.join(user_path, i_elem)
        if os.path.isdir(path):
            data_catalog['Количество подкаталогов'] = data_catalog.get('Количество подкаталогов', 0) + 1
            get_data(path)
        if os.path.isfile(path):
            data_catalog['Количество файлов'] = data_catalog.get('Количество файлов', 0) + 1
            data_catalog['Размер каталога'] = data_catalog.get('Размер каталога', 0) + os.path.getsize(user_path)
    return data_catalog


path = input('Пожалуйста, введите путь до директории: ')
data = get_data(path)

for i_key, i_value in data.items():
    if i_key == 'Размер каталога':
        print('Размер каталога (в Кб):', data[i_key] / 1024)
    else:
        print(i_key, ':', i_value)

