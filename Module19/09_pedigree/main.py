people_count = int(input('Введите количество человек: '))
genealogical_tree = dict()
height = dict()

for i_couple in range(people_count - 1):
    couple = input(f'{i_couple + 1} пара: ').split()
    if i_couple == 0:
        height[couple[1]] = 0
        height[couple[0]] = 1
    else:
        height[couple[0]] = height[couple[1]] + 1


print('\n«Высота» каждого члена семьи:')
for i_height in sorted(height):
    print(i_height, height[i_height])