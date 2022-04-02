from typing import Optional, Any


class Date:
    """ Класс Дата.

     Methods:
     from_string() : конвертирует строку даты в объект класса Date
     is_date_valid() : проверяет числа даты на корректность
     """

    def __init__(self, day: Optional[Any] = None, month: Optional[Any] = None, year: Optional[Any] = None) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return 'День: {}\tМесяц: {}\tГод: {}'.format(self.day, self.month, self.year)

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        date_lst = date_str.split('-')
        result = Date(int(date_lst[0]), int(date_lst[1]), int(date_lst[2]))
        return result

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        date_lst = date_str.split('-')
        if 0 < int(date_lst[0]) <= 31 and 0 < int(date_lst[1]) <= 12 and 0 < int(date_lst[2]) <= 3000:
            return True
        else:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
