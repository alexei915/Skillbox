violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_time = 0
songs_count = int(input('Сколько песен выбрать? '))

for i_song in range(songs_count):
    title = input('Название {0} песни: '.format(i_song + 1))
    total_time += violator_songs[title]

print('\nОбщее время звучания песен: {0}'.format(round(total_time)))