class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        tax = self.worth / 1000
        return tax


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        tax = self.worth / 200
        return tax


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        tax = self.worth / 500
        return tax


while True:
    money = int(input('Введите кол-во денег: '))
    property_view = input('Введите вид имущества (Apartment, Car, CountryHouse): ')
    property_cost = int(input('Введите стоимость имущества: '))
    if property_view.lower() == 'apartment':
        print('Величина налога: {}'.format(Apartment(property_cost).tax_calculation()))
        total_price = property_cost + Apartment(property_cost).tax_calculation()
    elif property_view.lower() == 'car':
        print('Величина налога: {}'.format(Car(property_cost).tax_calculation()))
        total_price = property_cost + Car(property_cost).tax_calculation()
    elif property_view.lower() == 'countryhouse':
        print('Величина налога: {}'.format(CountryHouse(property_cost).tax_calculation()))
        total_price = property_cost + CountryHouse(property_cost).tax_calculation()
    else:
        print('Ошибка. Такого вида имущества нет.')
        continue
    if money > total_price:
        print('Успешно приобретено!')
    else:
        lack = total_price - money
        print('Не хватает для покупки: {}'.format(lack))
