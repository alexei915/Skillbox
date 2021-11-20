violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

add_songs = []
song_duration = 0

songs_count = int(input('Сколько песен выбрать? '))
while 1 > songs_count > 9:
    print('Ошибка! Количество песен должно быть от 1 до 9.')
    songs_count = int(input('Сколько песен выбрать? '))

for i_song in range(songs_count):
    song_name = input(f'Название {i_song + 1} песни: ')
    add_songs.append(song_name)

for i_violator_songs in range(9):
    for i_add_songs in range(len(add_songs)):
        if add_songs[i_add_songs] == violator_songs[i_violator_songs][0]:
            song_duration += violator_songs[i_violator_songs][1]

print(f'\nОбщее время звучания песен: {round(song_duration, 2)} минут')