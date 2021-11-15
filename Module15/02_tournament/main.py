names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_names_list = []

for i in range(1, len(names_list) + 1):
    if i % 2 == 0:
        new_names_list.append(names_list[i - 1])

print(new_names_list)
