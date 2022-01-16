def histogram(text):
    sym_dict = dict()
    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def inverted(frequency_dict):
    invented_dict = dict()
    for sym in frequency_dict:
        if not invented_dict.get(hist[sym]):
            invented_dict[hist[sym]] = [sym]
        else:
            invented_dict[hist[sym]].append(sym)
    return invented_dict


string = input('Введите текст: ')
hist = histogram(string)

print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

print('\nИнвертированный словарь частот:')
for i_frequency in inverted(hist):
    print(i_frequency, ':', inverted(hist)[i_frequency])

