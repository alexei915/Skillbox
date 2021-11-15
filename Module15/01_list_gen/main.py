numbers_list = []
number = int(input('Введите число: '))

for i in range(1, number + 1):
    if i % 2 != 0:
        numbers_list.append(i)
print(numbers_list)
