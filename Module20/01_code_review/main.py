def get_values(data):
    interests = []
    count = 0
    for i_value in data.values():
        interests.extend(i_value['interests'])
        count += len(i_value['surname'])
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


pairs = []
# TODO рекомендую отказаться от именования с прификсом i_ не несет никакой го смысловой нагрузки
for i_code, i_age in students.items():
    # TODO отднобуквенных переменных в коде быть не должно от слова совсем
    x = (i_code, i_age['age'])
    pairs.append(x)


interests_list = get_values(students)[0]
total_length = get_values(students)[1]

print(f'Список пар "ID студента - Возраст": {pairs}')
print(f'Полный список интересов всех студентов: {interests_list}')
print(f'Общая длина всех фамилий студентов: {total_length}')

