file = open('first_tour.txt', 'r', encoding='utf-8')
scores_count = int(file.readline())
second_tour = dict()

print(f'Содрежимое файла first_tour.txt:\n{scores_count}')
for i_line in file:
    print(i_line, end='')
    str_list = i_line.split()
    if int(str_list[2]) > scores_count:
        player = str_list[1], str_list[0]
        second_tour[player] = int(str_list[2])

file.close()

sorted_keys = sorted(second_tour, key=second_tour.get, reverse=True)
new_file = open('second_tour.txt', 'w')
new_file.write(str(len(sorted_keys)) + '\n')
position = 1

for i_name in sorted_keys:
    new_file.write(str(position) + ') ' + i_name[0][0] + '. ' + i_name[1] + ' ' + str(second_tour[i_name]) + '\n')
    position += 1

new_file.close()
new_file = open('second_tour.txt', 'r', encoding='utf-8')

print('\n\nСодержимое файла second_tour.txt:')
for line in new_file:
    print(line, end='')

new_file.close()
