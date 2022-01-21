def slicer(seq, element):
    if seq.count(element) == 0:
        return tuple()
    if seq.count(element) == 1:
        return seq[(seq.index(element)):]
    count = 0
    for i, i_value in enumerate(seq):
        if i_value == element:
            count += 1
        if count == 2:
            return seq[(seq.index(element)):i + 1]

# TODO фукнции стараемся не вызывать в принтах
print(slicer((1, 3, 4, 5, 6, 7, 8), 2))
