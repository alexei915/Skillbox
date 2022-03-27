def squares_gen(data_1, data_2):
    for x in data_1:
        for y in data_2:
            print(x, y, x * y)
            yield x * y


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for number in squares_gen(list_1, list_2):
    if number == to_find:
        print('Found!!!')
        break
