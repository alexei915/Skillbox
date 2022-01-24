import random

numbers = [random.randint(0, 100) for _ in range(10)]
# new_numbers = [] (1-ый вариант)
#
# for seq_number in range(0, 9, 2):
#     pairs = numbers[seq_number], numbers[seq_number + 1]
#     new_numbers.append(pairs)
#
# print(new_numbers)

new_numbers = [tuple(numbers[(index * len(numbers) // 5):((index * len(numbers) // 5) + 2)]) for index in range(5)]
print(new_numbers)
