def my_zip(*args):
    min_element = min([len(value) for value in args])
    new_data = [(((list(element)[number]) for element in args) for number in range(min_element))]
    return new_data


# data_1 = [1, 2, 3, 4, 5]
# data_2 = {1: ‘s’, 2: ‘q’, 3: 4}
# data_3 = (1, 2, 3, 4, 5)
#
# my_function = my_zip(data_1, data_2, data_3)
# print(my_function)

