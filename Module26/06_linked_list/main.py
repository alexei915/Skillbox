from typing import Any, Optional


class Knot:

    def __init__(self, value: Optional[Any] = None, next_value: Optional['Knot'] = None) -> None:
        self.value = value
        self.next_value = next_value

    def __str__(self) -> str:
        return 'Knot [{value}]'.format(
            value=str(self.value)
        )


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next_value is not None:
                current = current.next_value
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return '[]'

    def append(self, elem: Any) -> None:
        new_knot = Knot(elem)
        if self.head is None:
            self.head = new_knot
            return

        last_knot = self.head
        while last_knot.next_value:
            last_knot = last_knot.next_value
        last_knot.next_value = new_knot
        self.length += 1

    def remove(self, index: int) -> None:
        cur_knot = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_knot is not None:
            if index == 0:
                self.head = cur_knot.next_value
                self.length -= 1
                return

        while cur_knot.next_value is not None:
            prev = cur_knot
            cur_knot = cur_knot.next_value
            cur_index += 1
            if cur_index == index:
                prev.next_value = cur_knot.next_value
                self.length -= 1
                break

    def get(self, index: int) -> None:
        cur_knot = self.head
        cur_index = 0
        if self.length == 0 or self.length < index:
            raise IndexError

        while cur_knot.next_value is not None:
            if cur_index == index:
                return cur_knot.value
            cur_knot = cur_knot.next_value
            cur_index += 1
        return cur_knot.value


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
