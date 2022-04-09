import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
res_2: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
res_3: float = timeit.timeit('"-".join(map(lambda x: str(x), list(range(1, 100))))', number=10000)

print('Время работы с использованием генератора: {time}'.format(time=res))
print('Время работы с использованием list comprehensions: {time}'.format(time=res_2))
print('Время работы с использованием функции map: {time}'.format(time=res_3))