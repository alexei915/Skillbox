import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day(day_number):
    karm_count = random.randint(1, 7)
    with open('errors.log', 'a') as file:
        try:
            if random.randint(1, 10) == 5:
                karm_count = 0
                raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        except KillError:
            file.write('День {}. Сегодня кого-то убили...\n'.format(day_number))
        except DrunkError:
            file.write('День {}. Сегодня напился...\n'.format(day_number))
        except CarCrashError:
            file.write('День {}. Сегодня разбил машину...\n'.format(day_number))
        except GluttonyError:
            file.write('День {}. Сегодня объелся...\n'.format(day_number))
        except DepressionError:
            file.write('День {}. Сегодня впал в депрессию...\n'.format(day_number))
        finally:
            return karm_count


karma = 0
day = 0

while True:
    if karma >= 500:
        print('Накоплено необходимое количество очков кармы!')
        break
    else:
        day += 1
        karm_scores = one_day(day)
        karma += karm_scores
        print('День: {}. +{} к карме. Уже накоплено {} очков кармы.'.format(day, karm_scores, karma))
