films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favourite_films = []
flag = True

film_name = input('Введите название фильма: ')

while film_name != 'end':
    for film in films:
        if film_name == film:
            favourite_films.append(film)
            flag = False
            break
    if flag:
        print('Ошибка! На данный фильм нет рецензии.')
    film_name = input('Введите название фильма: ')
    flag = True

print('Список любимых фильмов: ', favourite_films)
