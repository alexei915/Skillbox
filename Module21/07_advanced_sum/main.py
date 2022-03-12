def my_summ(*args):
    def flatten(data):
        result = []
        for element in data:
            if isinstance(element, int):
                result.append(element)
            else:
                result.extend(flatten(element))
        return result
    return sum(flatten(args))


print(my_summ([[1, 2, [3]], [1], 3]))
print(my_summ(1, 2, 3, 4, 5))

