entrance_file = open('numbers.txt', 'r', encoding='utf-8')
output_file = open('answer.txt', 'w')
summ = 0

print('Содержимое файла numbers.txt')
for i_line in entrance_file:
    print(i_line, end='')
    for sym in i_line:
        if sym != ' ' and sym != '\n':
            summ += int(sym)

output_file.write(str(summ))
output_file = open('answer.txt', 'r')

print('\nСодержимое файла answer.txt')
print(output_file.read())
entrance_file.close()
output_file.close()