cell_efficiency = []

cell_count = int(input('Введите количество клеток: '))

for i_efficiency in range(cell_count):
    efficiency = int(input(f'Введите эффективность {i_efficiency + 1} клетки: '))
    cell_efficiency.append(efficiency)

print(f'Неподходящие значения:', end=' ')
for i in range(len(cell_efficiency)):
    if cell_efficiency[i] < i:
        print(cell_efficiency[i], end=' ')