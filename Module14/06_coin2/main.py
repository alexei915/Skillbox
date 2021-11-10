import math

print('Введите координаты монетки: ')
x = float(input('x: '))
y = float(input('y: '))
radius = float(input('Введите радиус: '))
length = math.sqrt(x ** 2 + y ** 2)

if length > radius:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')