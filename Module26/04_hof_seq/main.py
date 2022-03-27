from collections.abc import Iterator


class MyIterator:

    def __init__(self, array: list) -> None:
        self.__counter = 0
        self.numbers = array
        if self.numbers[0] != 1 or self.numbers[1] != 1:
            raise StopIteration

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__counter > 2:
            self.numbers.insert(self.__counter - 1,
                                self.numbers[(self.__counter - self.numbers[self.__counter - 2] - 1)] +
                                self.numbers[(self.__counter - self.numbers[self.__counter - 3] - 1)])
            return self.numbers[self.__counter - 1]
        return self.numbers[self.__counter - 1]


q_hofstadter = MyIterator([1, 1])
for number in q_hofstadter:
    print(number)