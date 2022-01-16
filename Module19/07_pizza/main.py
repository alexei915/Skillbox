orders_count = int(input('Введите кол-во заказов: '))
buyers = dict()

for i_orders in range(orders_count):
    order = input(f'{i_orders + 1} заказ: ').split()
    if not order[0] in buyers:
        buyers[order[0]] = {}
    if order[1] in buyers[order[0]]:
        x = int(order[2]) + int(buyers[order[0]][order[1]])
        buyers[order[0]].update({order[1]: x})
    else:
        buyers[order[0]].update({order[1]: order[2]})


print()
for i_surname in sorted(buyers):
    print(f'{i_surname}:')
    for i_pizza in sorted(buyers[i_surname]):
        print('\t', i_pizza, ':', buyers[i_surname][i_pizza])
