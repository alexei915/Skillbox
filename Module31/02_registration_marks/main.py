import re


text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

car_number = r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'
taxi_number = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b'

car_list_num = re.findall(car_number, text)
taxi_list_num = re.findall(taxi_number, text)

print('Список номеров частных автомобилей:', car_list_num)
print('Список номеров такси:', taxi_list_num)