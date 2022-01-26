def sort(entries):
    for minimum in range(len(entries)):
        for current in range(minimum, len(entries)):
            if int(entries[current][0]) > int(entries[minimum][0]):
                entries[current], entries[minimum] = entries[minimum], entries[current]
    competition_protocol = dict()
    for pairs in entries:
        if not pairs[1] in competition_protocol:
            competition_protocol[pairs[1]] = pairs[0]
    return competition_protocol


entries_count = int(input('Сколько записей вносится в протокол? '))
while entries_count < 3:
    print('Ошибка! Минимальное количество игроков - 3.')
    entries_count = int(input('\nСколько записей вносится в протокол? '))


protocol = []
print('Записи (результат и имя):')
for number in range(entries_count):
    entry = input(f'{number + 1} запись: ').split()
    players_points = entry[0], entry[1]
    protocol.append(players_points)


top = 1
print('\nИтоги соревнований: ')
for player, scores in sort(protocol).items():
    print(f'{top} место. {player} ({scores})')
    top += 1
    if top == 4:
        break
