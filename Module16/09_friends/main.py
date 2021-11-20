friends_balance = []

friends_count = int(input('Кол-во друзей: '))
iou_count = int(input('Долговых расписок: '))

for i in range(1, friends_count + 1):
    friends_balance.append(list(range(i, -1, -i)))

for i_iou in range(iou_count):
    print(f'\n{i_iou + 1} расписка')
    recipient = int(input('Кому: '))
    source = int(input('От кого: '))
    summ = int(input('Сколько: '))
    friends_balance[recipient - 1][1] -= summ
    friends_balance[source - 1][1] += summ

print('\nБаланс друзей: ')
for i_friends in range(len(friends_balance)):
    print(friends_balance[i_friends][0], ':', friends_balance[i_friends][1])