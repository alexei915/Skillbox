numbers_list = []
count = 0
i = 0

num_count = int(input('Введите кол-во чисел в списке: '))
for _ in range(num_count):
    number = int(input('Введите число: '))
    numbers_list.append(number)

print(f'\nИзначальный список: {numbers_list}')

for num in numbers_list:
    for element in numbers_list:
        if element < num:
            count += 1
    numbers_list[i] = numbers_list[count]
    numbers_list[count] = num
    count = 0
    i += 1

print(f'\nОтсортированный список: {numbers_list}')

