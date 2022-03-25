class Person:

    def __init__(self, name, surname, age):
        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)

    def __str__(self):
        return 'Имя: {}\tФамилия: {}\tВозраст: {}\n'.format(
            self.__name, self.__surname, self.__age
        )

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя должно состоять только из букв.')

    def set_surname(self, surname):
        if surname.isalpha():
            self.__surname = surname
        else:
            raise Exception('Фамилия должно состоять только из букв.')

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            raise Exception('Возраст должен быть в диапазоне от 0 до 120.')


class Employee(Person):

    def calculation(self):
        pass


class Manager(Employee):
    __salary = 13000

    def __str__(self):
        info = super().__str__()
        info = info + 'Зарплата: {}\n'.format(self.__salary)
        return info


class Agent(Employee):
    __wage = 5000

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.sales = sales
        self.__salary = self.__wage + 0.05 * self.sales

    def __str__(self):
        info = super().__str__()
        info = info + 'Зарплата: {}\n'.format(self.__salary)
        return info


class Worker(Employee):
    __rate = 100

    def __init__(self, name, surname, age, hour_count):
        super().__init__(name, surname, age)
        self.hour_count = hour_count
        self.__salary = self.__rate * self.hour_count

    def __str__(self):
        info = super().__str__()
        info = info + 'Зарплата: {}\n'.format(self.__salary)
        return info


employee_list = [
    Manager(name='Ihar', surname='Tompson', age=40),
    Manager(name='Bob', surname='Phillips', age=35),
    Manager(name='Alex', surname='Hurgada', age=26),
    Agent(name='Vlad', surname='Petrov', age=19, sales=12500),
    Agent(name='Nikita', surname='Jango', age=30, sales=9880),
    Agent(name='Alesya', surname='Gunich', age=38, sales=14540),
    Worker(name='Tanya', surname='Rudz', age=33, hour_count=171),
    Worker(name='Daniil', surname='Melnik', age=22, hour_count=140),
    Worker(name='John', surname='Lock', age=50, hour_count=168)
]

print('Данные по сотрудникам компании:\n')
for info in employee_list:
    print(info)