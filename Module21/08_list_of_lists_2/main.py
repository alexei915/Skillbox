def flatten(data):
    if not data:
        return data
    if isinstance(data[0], list):
        return flatten(data[0]) + flatten(data[1:])
    return data[:1] + flatten(data[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

my_function = flatten(nice_list)
print(my_function)


