def get_list(index, numbers_list):
    for i_row in range(3):
        for i_col in range(3):
            numbers_list.append(nice_list[index][i_row][i_col])
    return numbers_list


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = []
nice_list[:] = [get_list(i, new_list) for i in range(2)]
print(new_list)
