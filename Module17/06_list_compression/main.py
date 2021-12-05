import random


def remove_null(number):
    numbers.remove(numbers[number])
    numbers.append(0)
    return numbers[number]


n = int(input('Введите кол-во чисел в списке: '))
numbers = [random.randint(0, 10) for _ in range(n)]

numbers = [remove_null(i) if numbers[i] == 0 else numbers[i] for i in range(len(numbers))]
while numbers.count(0) != 0:
    numbers.remove(0)

print(numbers)
