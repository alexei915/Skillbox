class File:
    """ Контекст-менеджер «Файл». При попытке открыть
     несуществующий файл автоматически создаёт и
     открывает этот файл в режиме записи

     :arg
     file_name (str): название файла
     reading_mode (str): режим чтения файла
     file (None): файловый объект
     """

    def __init__(self, file_name: str, reading_mode: str) -> None:
        self.file_name = file_name
        self.reading_mode = reading_mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        if exc_type is (FileExistsError, FileNotFoundError,
                        IsADirectoryError):
            return True


with File('new_file', 'r') as obj:
    obj.write('123')


