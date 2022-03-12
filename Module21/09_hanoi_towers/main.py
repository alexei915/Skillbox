def tower_of_hanoi(n, x, y, z):
    if n == 1:
        print('Переложить диск 1 со стержня номер {} на стержень номер {}'.format(x, z))
        return
    tower_of_hanoi(n - 1, x, z, y)
    print('Переложить диск {} со стержня номер {} на стержень номер {}'.format(n, x, z))
    tower_of_hanoi(n - 1, y, x, z)


disks_count = int(input('Введите количество дисков: '))
tower_of_hanoi(disks_count, 1, 2, 3)
