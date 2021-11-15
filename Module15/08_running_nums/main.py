initial_list = []
shifted_list = []
i = 0

num_count = int(input('Введите кол-во чисел в списке: '))
for _ in range(num_count):
    number = int(input('Введите число: '))
    initial_list.append(number)

shifted = int(input('Сдвиг: '))

while i + shifted < len(initial_list):
    shifted_list.append(initial_list[i + shifted])
    i += 1
while i != len(initial_list):
    i += 1
    shifted_list.append(initial_list[i + shifted - len(initial_list) - 1])

print(f'Изначальный список {initial_list}')
print(f'Сдвинутый список: {shifted_list}')
