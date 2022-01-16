goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

amount_dict = dict()

for i_goods in goods:
    amount_dict[i_goods] = 0
    amount_dict['Стоимость'] = 0
    for i_store in store[goods[i_goods]]:
        amount_dict[i_goods] += i_store['quantity']
        amount_dict['Стоимость'] += i_store['quantity'] * i_store['price']
    print('{0} - {1} шт, стоимость - {2} руб'.format(i_goods, amount_dict[i_goods], amount_dict['Стоимость']))
