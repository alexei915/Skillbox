import random

numbers = [random.randint(0, 100) for _ in range(10)]
# new_numbers = [] (1-ый вариант)
#
# for i in range(0, 9, 2):
#     pairs = numbers[i], numbers[i + 1]
#     new_numbers.append(pairs)
#
#
# print(new_numbers)

new_numbers = [tuple(numbers[(i * len(numbers) // 5):((i * len(numbers) // 5) + 2)]) for i in range(5)]
print(new_numbers)

