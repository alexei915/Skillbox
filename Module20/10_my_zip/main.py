def my_zip(type_1, type_2):
    if len(type_1) > len(type_2):
        amount_len = len(type_2)
    else:
        amount_len = len(type_1)
    gen = ((type_1[i], type_2[i]) for i in range(amount_len))
    return gen


string = [2, 9, 18, 28]
tpl = ["Дима", "Марина", "Андрей", "Никита"]

print(my_zip(string, tpl))
for x in my_zip(string, tpl):
    print(x)


