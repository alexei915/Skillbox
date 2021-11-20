people_circle = []
count = 0

people_count = int(input('Кол-во людей: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number} человек')

for num in range(people_count):
    people_circle.append(num + 1)

while len(people_circle) != 1:
    print(f'\nТекущий круг людей: {people_circle}')
    print(f'Начало счёта с номера {people_circle[count]}')
    for i in range(number):
        count += 1
        if count == len(people_circle):
            count = 0
    print(f'Выбывает человек под номером {people_circle[count - 1]}')
    people_circle.remove(people_circle[count - 1])
    if count != 0:
        count -= 1

print(f'\nОстался человек под номером {people_circle[count]}')
