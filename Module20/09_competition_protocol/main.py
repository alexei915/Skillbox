def sort(entries_list):
    for minimum in range(len(entries_list)):
        for curr in range(minimum, len(entries_list)):
            if int(entries_list[curr][0]) > int(entries_list[minimum][0]):
                entries_list[curr], entries_list[minimum] = entries_list[minimum], entries_list[curr]
    protocol_dict = dict()
    for pairs in entries_list:
        if not pairs[1] in protocol_dict:
            protocol_dict[pairs[1]] = pairs[0]
    return protocol_dict


entries_count = int(input('Сколько записей вносится в протокол? '))
while entries_count < 3:
    print('Ошибка! Минимальное количество игроков - 3.')
    entries_count = int(input('\nСколько записей вносится в протокол? '))


protocol = []
print('Записи (результат и имя):')
for number in range(entries_count):
    entries = input(f'{number + 1} запись: ').split()
    players_points = entries[0], entries[1]
    protocol.append(players_points)


top = 1
print('\nИтоги соревнований: ')
for player, scores in sort(protocol).items():
    print(f'{top} место. {player} ({scores})')
    top += 1
    if top == 4:
        break
