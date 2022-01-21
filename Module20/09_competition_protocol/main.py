def sort(entries_list):
    for i_mn in range(len(entries_list)):
        for curr in range(i_mn, len(entries_list)):
            if int(entries_list[curr][0]) > int(entries_list[i_mn][0]):
                entries_list[curr], entries_list[i_mn] = entries_list[i_mn], entries_list[curr]
    protocol_dict = dict()
    for i in entries_list:
        if not i[1] in protocol_dict:
            protocol_dict[i[1]] = i[0]
    return protocol_dict


entries_count = int(input('Сколько записей вносится в протокол? '))
while entries_count < 3:
    print('Ошибка! Минимальное количество игроков - 3.')
    entries_count = int(input('\nСколько записей вносится в протокол? '))


protocol = []
print('Записи (результат и имя):')
for i_entries in range(entries_count):
    entries = input(f'{i_entries + 1} запись: ').split()
    x = entries[0], entries[1]
    protocol.append(x)


i_top = 1
print('\nИтоги соревнований: ')
for i_player, i_scores in sort(protocol).items():
    print(f'{i_top} место. {i_player} ({i_scores})')
    i_top += 1
    if i_top == 4:
        break

# TODO рекомендации данные ранее применить
