video_cards_list = []
new_video_cards_list = []

video_cards_count = int(input('Кол-во видеокарт: '))
for i in range(video_cards_count):
    video_card = int(input(f'{i + 1} видеокарта: '))
    video_cards_list.append(video_card)

for i_card in range(5):
    if max(video_cards_list) > video_cards_list[i_card]:
        new_video_cards_list.append(video_cards_list[i_card])

print(f'\nСтарый список видеокарт: {video_cards_list}')
print(f'Новый список видеокарт: {new_video_cards_list}')
