containers = []
i = 0

containers_count = int(input('Введите кол-во контейнеров: '))

for _ in range(containers_count):
    container_weight = int(input('Введите вес контейнера: '))
    while container_weight % 1 != 0 or container_weight > 200:
        print('Ошибка! Вес контейнера должен быть целым число и не превышать 200 кг!')
        container_weight = int(input('Введите вес контейнера: '))
    containers.append(container_weight)

new_container_weight = int(input('\nВведите вес нового контейнера: '))
while new_container_weight % 1 != 0 or new_container_weight > 200:
    print('Ошибка! Вес контейнера должен быть целым число и не превышать 200 кг!')
    new_container_weight = int(input('Введите вес нового контейнера: '))

while containers[i] >= new_container_weight:
    i += 1
    if i == len(containers):
        break

print(f'\nНомер, куда встанет новый контейнер: {i + 1}')
