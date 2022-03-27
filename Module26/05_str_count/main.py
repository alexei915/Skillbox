import os


def gen_string(directory):
    for i_elem in os.listdir(directory):
        path = os.path.join(directory, i_elem)
        if os.path.isdir(path):
            yield from gen_string(path)
        if os.path.isfile(path):
            if path.endswith('.py'):
                with open(path, 'r', encoding='utf-8') as file:
                    for i_line in file:
                        if not i_line.isspace() and '#' not in i_line:
                            yield 1


directory_path = input('Введите путь к директории: ')
print(sum(gen_string(directory_path)))
