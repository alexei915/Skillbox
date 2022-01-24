def slicer(seq, element):
    if seq.count(element) == 0:
        return tuple()
    if seq.count(element) == 1:
        return seq[(seq.index(element)):]
    count = 0
    for seq_number, value in enumerate(seq):
        if value == element:
            count += 1
        if count == 2:
            return seq[(seq.index(element)):seq_number + 1]


my_function = slicer((1, 2, 3, 4, 5, 6, 2, 7, 8), 2)
print(my_function)
