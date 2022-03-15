file = open('zen.txt', 'r', encoding='utf-8')
str_list = []

for i_line in file:
    str_list.append(i_line)

file.close()
revers_str = str_list[::-1]
revers_str[0] += '\n'

for string in revers_str:
    print(string, end='')
