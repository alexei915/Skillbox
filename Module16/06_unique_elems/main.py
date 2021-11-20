first_list = []
second_list = []

for num in range(3):
    number = int(input(f'Введите {num + 1} число: '))
    first_list.append(number)

print()
for i_num in range(7):
    numbers = int(input(f'Введите {i_num + 1} число: '))
    second_list.append(numbers)

print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}')
first_list.extend(second_list)

for i in first_list:
    while first_list.count(i) != 1:
        first_list.remove(i)

print(f'Новый первый список с уникальными элементами: {first_list}')
