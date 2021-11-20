amn_class = []
first_class = []
second_class = []
i = 0
count = 0

for i_height in range(160, 177, 2):
    first_class.append(i_height)

for i_height_2 in range(162, 181, 3):
    second_class.append(i_height_2)

amn_class.extend(first_class)
amn_class.extend(second_class)

for num in range(len(amn_class)):
    for element in range(len(amn_class)):
        if amn_class[num] < amn_class[element]:
            amn_class[element], amn_class[num] = amn_class[num], amn_class[element]

print(f'Отсортированный список: {amn_class}')
