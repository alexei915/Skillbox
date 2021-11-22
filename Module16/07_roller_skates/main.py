skate_size = []
foot_size = []
max_people_count = 0

skate_count = int(input('Кол-во коньков: '))
for i_skate_size in range(skate_count):
    size = int(input(f'Размер {i_skate_size + 1} пары: '))
    skate_size.append(size)

people_count = int(input('\nКол-во людей: '))
for i_foot_size in range(people_count):
    size_people = int(input(f'Размер ноги {i_foot_size + 1} человека: '))
    foot_size.append(size_people)


for _ in range(len(foot_size)):
    if max(skate_size) >= max(foot_size):
        skate_size.remove(max(skate_size))
        foot_size.remove(max(foot_size))
        max_people_count += 1
    else:
        foot_size.remove(max(foot_size))

print(f'Наибольшее кол-во людей, которые могут взять ролики: {max_people_count}')
