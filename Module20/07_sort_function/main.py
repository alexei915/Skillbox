def sort_number(seq):
    seq = list(seq)
    for number in seq:
        if not isinstance(number, int):
            return tuple(seq)
    for minimum in range(len(seq)):
        for curr in range(minimum, len(seq)):
            if seq[curr] < seq[minimum]:
                seq[curr], seq[minimum] = seq[minimum], seq[curr]
    return tuple(seq)


my_sort = sort_number((6, 3, -1, 8, 4, 10, -5))
print(my_sort)
