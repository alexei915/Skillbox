class Student:

    def __init__(self, names, group_number, grades):
        self.names = names
        self.group_number = group_number
        self.grades = grades

    def print_info(self):
        print('Student: {}\nGroup: {}\nGrades: {}\n'.format(
            self.names, self.group_number, self.grades))

    def middle_count(self):
        return sum(self.grades) / 5


students = [Student('Ivan Ivanov', 1511, [8, 9, 9, 10, 7]),
            Student('Nikita Petrov', 1512, [7, 7, 8, 9, 7]),
            Student('Nina Latina', 1510, [6, 6, 9, 5, 7]),
            Student('Dima Kurochkin', 1459, [10, 9, 9, 10, 10]),
            Student('Ilya Andreev', 1513, [7, 7, 7, 7, 7]),
            Student('Alex Vertinskiy', 1456, [8, 9, 9, 8, 8]),
            Student('Olga Vargan', 1245, [4, 5, 5, 8, 6]),
            Student('Darya Saberi', 1125, [4, 4, 4, 4, 5]),
            Student('Masha Dulina', 1458, [6, 6, 6, 6, 7]),
            Student('Egor Pupkin', 1512, [5, 5, 6, 6, 7])
]


sorted_grade = sorted(students, key=lambda elem: elem.middle_count())
for i in range(len(sorted_grade)):
    sorted_grade[i].print_info()
