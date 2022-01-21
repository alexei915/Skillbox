def tpl_sort(tpl):
    tpl = list(tpl)
    for i in tpl:
        if not isinstance(i, int):
            return tuple(tpl)
    for i_mn in range(len(tpl)):
        for curr in range(i_mn, len(tpl)):
            if tpl[curr] < tpl[i_mn]:
                tpl[curr], tpl[i_mn] = tpl[i_mn], tpl[curr]
    return tpl


print(tpl_sort((6, 3, -1, 8.5, 4, 10, -5)))

# TODO применить рекомендации данные ранее

# TODO переменных в сокращенной форме быть недолжно
# TODO в именовании не используем слова list set dict tuple
