def is_guest_exist(name, guests_list):
    for i_name in guests_list:
        if i_name == name:
            return True
    return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guests_action = ''

while guests_action != 'Пора спать':
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    guests_action = input('Гость пришёл или ушёл? ')
    if guests_action == 'пришёл':
        guest_name = input('Имя гостя: ')
        if len(guests) < 6:
            print(f'Привет, {guest_name} !')
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    if guests_action == 'ушёл':
        guest_name = input('Имя гостя: ')
        if is_guest_exist(guest_name, guests):
            print(f'Пока, {guest_name} !')
            guests.remove(guest_name)
        else:
            print('Такого гостя нет на вечеринке!')
    print()

print('Вечеринка закончилась, все легли спать.')