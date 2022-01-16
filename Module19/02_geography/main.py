def get_country(city_dict):
    for i in city_dict:
        if city in city_dict[i]:
            print('Город {0} расположен в стране {1}.'.format(city, i))
            return True
    return False


city_in_country = dict()
countries_count = int(input('Кол-во стран: '))

for i_country in range(countries_count):
    country = input('{0} страна: '.format(i_country + 1)).split()
    city_in_country[country[0]] = country[1:]

for i_city in range(3):
    city = input('\n{0} город: '.format(i_city + 1))
    if not get_country(city_in_country):
        print('По городу {0} данных нет.'.format(city))
