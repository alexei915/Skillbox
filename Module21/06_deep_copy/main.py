import copy
from pprint import pprint


def site_construct(struct, number, sites_ready=dict()):
    if number == 0:
        return 1
    products_name = input('Введите название продукта для нового сайта: ')
    site_copy = copy.deepcopy(struct)
    sites_ready[f'Сайт для {products_name}'] = site_copy
    site_copy['html']['head']['title'] = f'Куплю/продам {products_name} недорого'
    site_copy['html']['body'] = f'У нас самая низкая цена на {products_name}'
    for keys in sites_ready:
        print(f'{keys}:')
        pprint(sites_ready[keys])
    return site_construct(struct, number - 1)


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

sites_count = int(input('Сколько сайтов? '))
my_function = site_construct(site, sites_count)
