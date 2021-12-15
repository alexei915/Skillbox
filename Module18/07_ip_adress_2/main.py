def check_ip_address(ip):
    for i in ip:
        if len(ip) < 4:
            print('Адрес - это четыре числа, разделенные точками')
            return False
        elif not i.isdigit():
            print(f'{i} - не целое число')
            return False
        elif int(i) > 255:
            print(f'{int(i)} превышает 255')
            return False
        elif int(i) < 0:
            print(f'{int(i)} меньше 0')
            return False
    return True


ip_address = input('Введите IP: ').split('.')

if check_ip_address(ip_address):
    print('IP-адрес корректен')


