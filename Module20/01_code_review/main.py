def get_values(data):
    interests = []
    count = 0
    for value in data.values():
        interests.extend(value['interests'])
        count += len(value['surname'])
    return interests, count


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


pairs_list = []
for code, age in students.items():
    pairs = (code, age['age'])
    pairs_list.append(pairs)


interests_list = get_values(students)[0]
total_length = get_values(students)[1]

print(f'Список пар "ID студента - Возраст": {pairs_list}')
print(f'Полный список интересов всех студентов: {interests_list}')
print(f'Общая длина всех фамилий студентов: {total_length}')

# TODO list set dict tuple в именовании переменных не указываем
