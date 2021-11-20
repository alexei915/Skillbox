numbers = []
count = 0

num_count = int(input('Кол-во чисел: '))

for _ in range(num_count):
    num = int(input('Число: '))
    numbers.append(num)

print('Последовательность: ', end='')
for i_num in numbers:
    print(i_num, end=' ')

if numbers[num_count - 1] == numbers[num_count - 2]:
    for i in range(len(numbers) - 2):
        numbers.append(numbers[i])
        count += 1
else:
    for i in range(len(numbers)):
        if numbers[i] != numbers[len(numbers) - i - 1]:
            numbers.insert(len(numbers) - i, numbers[i])
            count += 1

print(f'\nНужно приписать чисел: {count}')
print('Сами числа: ', end=' ')
for i_digits in range(num_count, len(numbers)):
    print(numbers[i_digits], end=' ')
