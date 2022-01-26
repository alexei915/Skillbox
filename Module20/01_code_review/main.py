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


pairs_id_age = []
for code, age in students.items():
    pairs = (code, age['age'])
    pairs_id_age.append(pairs)


students_interests = get_values(students)[0]
total_length = get_values(students)[1]

print(f'Список пар "ID студента - Возраст": {pairs_id_age}')
print(f'Полный список интересов всех студентов: {students_interests}')
print(f'Общая длина всех фамилий студентов: {total_length}')


