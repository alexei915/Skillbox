def my_zip(type_1, type_2):
    if len(type_1) > len(type_2):
        amount_len = len(type_2)
    else:
        amount_len = len(type_1)
    gen = ((type_1[num], type_2[num]) for num in range(amount_len))
    return gen


seq = [2, 9, 18, 28]
names = ["Дима", "Марина", "Андрей", "Никита"]

my_function = my_zip(seq, names)

print(my_function)
for element in my_function:
    print(element)

# TODO нейминг в питоне пишем развернуто сокращений быть не должно
