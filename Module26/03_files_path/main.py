import os
from collections.abc import Iterable


def gen_files_path(catalog: str, directory: str) -> Iterable[str]:
    for i_elem in os.listdir(directory):
        path = os.path.join(directory, i_elem)
        if i_elem == catalog:
            print(path, 'Found!!!!')
            return True
        if os.path.isdir(path):
            yield from gen_files_path(catalog, path)
        if os.path.isfile(path):
            yield path


catalog_name = input('Введите название каталога: ')
directory_path = input('Пожалуйста, введите путь до директории: ')
for file_path in gen_files_path(catalog_name, directory_path):
    print(file_path)

