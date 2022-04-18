import itertools


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

for code in itertools.product(numbers, numbers, numbers, numbers):
    print(code)
    count += 1

print('\nКоличество возможных комбинаций: {}'.format(count))