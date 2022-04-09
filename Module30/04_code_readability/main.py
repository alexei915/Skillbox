from typing import List

# Вариант 1
# prime_numbers: List[int] = list(filter(lambda x: 0 not in [x % y for y in range(2, x)] and x > 1, list(range(0, 1000))))
# print(list(prime_numbers))


# Вариант 2

def get_prime() -> list:
    """ Функция. Возращает список из простых
    чисел от 0 до 1000"""

    is_prime: bool = True
    prime_numbers: List[int] = []

    for number in range(1000):
        for divider in range(2, number):
            if number % divider == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            prime_numbers.append(number)
        else:
            is_prime = True

    return prime_numbers


if __name__ == '__main__':
    get_prime()
