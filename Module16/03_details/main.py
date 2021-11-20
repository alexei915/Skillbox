shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('Название детали: ')
count = 0
summ = 0

for i_detail in range(len(shop)):
    if shop[i_detail][0] == detail_name:
        count += 1
        summ += shop[i_detail][1]

print(f'\nКол-во деталей: {count}')
print(f'Общая стоимость: {summ}')